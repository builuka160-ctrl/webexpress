#!/usr/bin/env python3
"""Veo video generation (long running). Manifest: JSON list of jobs.
job = {"out":"clip.mp4","prompt":"...","ratio":"16:9","image":"first.png","lastFrame":"last.png","model":"veo-3.1-fast-generate-preview"}
"""
import base64, json, mimetypes, os, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

KEY = os.environ.get("GEMINI_API_KEY", "")
API = "https://generativelanguage.googleapis.com/v1beta"

def post(url, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)

def img(path):
    return {"bytesBase64Encoded": base64.b64encode(open(path, "rb").read()).decode(),
            "mimeType": mimetypes.guess_type(path)[0] or "image/png"}

def run(job):
    out = job["out"]
    if os.path.exists(out) and not job.get("force"):
        return f"SKIP {out}"
    model = job.get("model", "veo-3.1-fast-generate-preview")
    inst = {"prompt": job["prompt"]}
    if job.get("image"):
        inst["image"] = img(job["image"])
    if job.get("lastFrame"):
        inst["lastFrame"] = img(job["lastFrame"])
    params = {"aspectRatio": job.get("ratio", "16:9")}
    if job.get("resolution"):
        params["resolution"] = job["resolution"]
    if job.get("negativePrompt"):
        params["negativePrompt"] = job["negativePrompt"]
    try:
        op = post(f"{API}/models/{model}:predictLongRunning?key={KEY}",
                  {"instances": [inst], "parameters": params})
    except urllib.error.HTTPError as e:
        return f"FAIL {out} :: start HTTP {e.code} {e.read().decode()[:300]}"
    name = op.get("name")
    if not name:
        return f"FAIL {out} :: no op name {json.dumps(op)[:200]}"
    for _ in range(90):
        time.sleep(10)
        with urllib.request.urlopen(f"{API}/{name}?key={KEY}", timeout=60) as r:
            st = json.load(r)
        if st.get("done"):
            if "error" in st:
                return f"FAIL {out} :: {json.dumps(st['error'])[:300]}"
            resp = st.get("response", {})
            samples = (resp.get("generateVideoResponse", {}).get("generatedSamples")
                       or resp.get("generatedSamples") or resp.get("videos") or [])
            if not samples:
                return f"FAIL {out} :: no samples {json.dumps(resp)[:400]}"
            s = samples[0]
            uri = (s.get("video", {}) or {}).get("uri") or s.get("uri")
            if not uri:
                return f"FAIL {out} :: no uri {json.dumps(s)[:300]}"
            os.makedirs(os.path.dirname(out), exist_ok=True)
            req = urllib.request.Request(uri + ("&" if "?" in uri else "?") + "key=" + KEY)
            with urllib.request.urlopen(req, timeout=600) as r, open(out, "wb") as f:
                f.write(r.read())
            return f"OK   {out} ({os.path.getsize(out)//1024}KB)"
    return f"FAIL {out} :: timeout"

if __name__ == "__main__":
    jobs = json.load(open(sys.argv[1]))
    with ThreadPoolExecutor(max_workers=int(sys.argv[2]) if len(sys.argv) > 2 else 2) as ex:
        for line in ex.map(run, jobs):
            print(line, flush=True)
