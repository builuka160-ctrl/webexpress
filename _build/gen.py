#!/usr/bin/env python3
"""Batch image generation via Gemini API. Manifest: JSON list of jobs.

job = {"out": "path.png", "prompt": "...", "ratio": "16:9",
       "model": "gemini-3.1-flash-image", "ref": "input.png" (optional)}
"""
import base64, json, mimetypes, os, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

KEY = os.environ.get("GEMINI_API_KEY", "")
DEF_MODEL = "gemini-3.1-flash-image"

def call(job):
    model = job.get("model", DEF_MODEL)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={KEY}"
    parts = []
    for ref in job.get("refs", []) or ([job["ref"]] if job.get("ref") else []):
        mime = mimetypes.guess_type(ref)[0] or "image/png"
        parts.append({"inlineData": {"mimeType": mime,
                                     "data": base64.b64encode(open(ref, "rb").read()).decode()}})
    parts.append({"text": job["prompt"]})
    body = {"contents": [{"parts": parts}],
            "generationConfig": {"responseModalities": ["IMAGE"],
                                 "imageConfig": {"aspectRatio": job.get("ratio", "16:9")}}}
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=420) as r:
        return json.load(r)

def run(job):
    out = job["out"]
    if os.path.exists(out) and not job.get("force"):
        return f"SKIP {out}"
    for attempt in range(1, 4):
        try:
            data = call(job)
            for p in data["candidates"][0]["content"]["parts"]:
                if "inlineData" in p:
                    os.makedirs(os.path.dirname(out), exist_ok=True)
                    open(out, "wb").write(base64.b64decode(p["inlineData"]["data"]))
                    return f"OK   {out} ({os.path.getsize(out)//1024}KB)"
            last = "no image part: " + json.dumps(data)[:200]
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code} {e.read().decode()[:200]}"
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
        time.sleep(4 * attempt)
    return f"FAIL {out} :: {last}"

if __name__ == "__main__":
    jobs = json.load(open(sys.argv[1]))
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for line in ex.map(run, jobs):
            print(line, flush=True)
