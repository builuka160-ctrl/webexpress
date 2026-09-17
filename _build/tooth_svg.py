#!/usr/bin/env python3
"""Vector implant for the dental hero: molar crown + titanium abutment + screw.

The earlier 3D render read as a mushroom — the crown was about three times the
width of a stubby post. This draws the real proportions instead: a cusped molar
crown, a short tapered abutment and a threaded screw roughly as long as the
crown is tall.
"""
import math, os, sys

W, H = 560, 900
CX = 280

# ── crown ──────────────────────────────────────────────────────────────────
CROWN_TOP, CROWN_NECK = 92, 402          # occlusal surface .. gum line
CROWN_HALF, NECK_HALF = 148, 104         # widest point .. neck
CUSPS = 4

def crown_path():
    """Bell silhouette whose top edge is a row of cusps."""
    shoulder = CROWN_TOP + 46            # where the cusps meet the side walls
    waist = CROWN_TOP + 150              # widest point of the crown
    d = [f'M {CX - NECK_HALF} {CROWN_NECK}']
    # left wall, neck -> waist -> shoulder
    d.append(f'C {CX - CROWN_HALF + 4} {CROWN_NECK - 34} {CX - CROWN_HALF} {waist + 40} {CX - CROWN_HALF} {waist}')
    d.append(f'C {CX - CROWN_HALF} {waist - 44} {CX - CROWN_HALF + 20} {shoulder + 18} {CX - CROWN_HALF + 40} {shoulder}')
    # cusped occlusal edge, left -> right
    span = 2 * (CROWN_HALF - 40)
    step = span / CUSPS
    x = CX - CROWN_HALF + 40
    for i in range(CUSPS):
        # outer cusps sit a little lower than the two middle ones
        lift = 30 if i in (0, CUSPS - 1) else 40
        peak_x = x + step / 2
        nx = x + step
        d.append(f'Q {peak_x} {shoulder - lift} {nx} {shoulder - (0 if i == CUSPS - 1 else 8)}')
        x = nx
    # right wall, shoulder -> waist -> neck
    d.append(f'C {CX + CROWN_HALF - 20} {shoulder + 18} {CX + CROWN_HALF} {waist - 44} {CX + CROWN_HALF} {waist}')
    d.append(f'C {CX + CROWN_HALF} {waist + 40} {CX + CROWN_HALF - 4} {CROWN_NECK - 34} {CX + NECK_HALF} {CROWN_NECK}')
    d.append('Z')
    return ' '.join(d)

def fissures():
    """Central groove with a branch running into each cusp valley."""
    y0, y1 = CROWN_TOP + 62, CROWN_TOP + 188
    out = [f'<path d="M {CX} {y0} L {CX} {y1}" stroke="rgba(108,126,138,.5)" '
           f'stroke-width="7" stroke-linecap="round" fill="none"/>']
    for sign in (-1, 1):
        for k, depth in ((0.62, 0.42), (1.0, 0.72)):
            ex = CX + sign * CROWN_HALF * 0.66 * k
            ey = y0 + (y1 - y0) * depth
            out.append(f'<path d="M {CX} {ey} Q {CX + sign * 44 * k} {ey - 22} {ex} {y0 + 30}" '
                       f'stroke="rgba(108,126,138,.36)" stroke-width="5.5" '
                       f'stroke-linecap="round" fill="none"/>')
    return ''.join(out)

# ── abutment and screw ─────────────────────────────────────────────────────
ABUT_TOP, ABUT_BOT = 402, 496
ABUT_HALF_TOP, ABUT_HALF_BOT = 86, 70
SCREW_TOP, SCREW_TIP = 496, 806
SCREW_HALF_TOP, SCREW_HALF_TIP = 64, 26

def screw_outline():
    return (f'M {CX - SCREW_HALF_TOP} {SCREW_TOP} L {CX + SCREW_HALF_TOP} {SCREW_TOP} '
            f'L {CX + SCREW_HALF_TIP} {SCREW_TIP - 26} '
            f'Q {CX} {SCREW_TIP + 16} {CX - SCREW_HALF_TIP} {SCREW_TIP - 26} Z')

def threads():
    """Slanted ridges following the taper, so the screw reads as threaded."""
    out, y, pitch = [], SCREW_TOP + 16, 23
    while y < SCREW_TIP - 30:
        t = (y - SCREW_TOP) / float(SCREW_TIP - SCREW_TOP)
        half = SCREW_HALF_TOP + (SCREW_HALF_TIP - SCREW_HALF_TOP) * t
        out.append(
            f'<path d="M {CX - half:.1f} {y:.1f} L {CX + half:.1f} {y - 8:.1f}" '
            f'stroke="rgba(28,44,56,.32)" stroke-width="3.4" stroke-linecap="round"/>'
            f'<path d="M {CX - half:.1f} {y + 3.6:.1f} L {CX + half:.1f} {y - 4.4:.1f}" '
            f'stroke="rgba(255,255,255,.55)" stroke-width="1.6" stroke-linecap="round"/>')
        y += pitch
    return ''.join(out)

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Керамическая коронка на титановом имплантате">
<defs>
  <linearGradient id="enamel" x1="0.12" y1="0" x2="0.86" y2="1">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset=".26" stop-color="#FCFDFE"/>
    <stop offset=".58" stop-color="#F2F5F7"/>
    <stop offset=".84" stop-color="#E2E8EC"/>
    <stop offset="1" stop-color="#CBD5DB"/>
  </linearGradient>
  <linearGradient id="occlusal" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#C7D4DC" stop-opacity=".55"/>
    <stop offset="1" stop-color="#C7D4DC" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="gloss" cx=".32" cy=".22" r=".62">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".95"/>
    <stop offset=".55" stop-color="#ffffff" stop-opacity=".25"/>
    <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="enamelEdge" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".85"/>
    <stop offset=".45" stop-color="#ffffff" stop-opacity="0"/>
    <stop offset="1" stop-color="#94A6B1" stop-opacity=".45"/>
  </linearGradient>
  <linearGradient id="steel" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#5E6B75"/>
    <stop offset=".16" stop-color="#C9D3DA"/>
    <stop offset=".34" stop-color="#F2F6F8"/>
    <stop offset=".52" stop-color="#9FAEB9"/>
    <stop offset=".72" stop-color="#E6ECF0"/>
    <stop offset=".88" stop-color="#7C8A95"/>
    <stop offset="1" stop-color="#48555F"/>
  </linearGradient>
  <linearGradient id="collar" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#6B7883"/>
    <stop offset=".2" stop-color="#EEF3F6"/>
    <stop offset=".5" stop-color="#93A2AD"/>
    <stop offset=".8" stop-color="#E4EAEE"/>
    <stop offset="1" stop-color="#5A666F"/>
  </linearGradient>
  <radialGradient id="shadow" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#1D3A4D" stop-opacity=".3"/>
    <stop offset="1" stop-color="#1D3A4D" stop-opacity="0"/>
  </radialGradient>
  <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur stdDeviation="9"/>
  </filter>
  <clipPath id="screwClip"><path d="{screw_outline()}"/></clipPath>
</defs>

<ellipse cx="{CX}" cy="846" rx="132" ry="22" fill="url(#shadow)"/>

<!-- screw -->
<path d="{screw_outline()}" fill="url(#steel)"/>
<g clip-path="url(#screwClip)">{threads()}</g>

<!-- abutment -->
<path d="M {CX - ABUT_HALF_TOP} {ABUT_TOP} L {CX + ABUT_HALF_TOP} {ABUT_TOP} L {CX + ABUT_HALF_BOT} {ABUT_BOT} L {CX - ABUT_HALF_BOT} {ABUT_BOT} Z" fill="url(#steel)"/>
<rect x="{CX - ABUT_HALF_BOT - 6}" y="{ABUT_BOT - 12}" width="{2 * ABUT_HALF_BOT + 12}" height="14" rx="6" fill="url(#collar)"/>

<!-- collar where the crown seats on the abutment -->
<path d="M {CX - 100} {ABUT_TOP - 16} Q {CX} {ABUT_TOP + 20} {CX + 100} {ABUT_TOP - 16} L {CX + 100} {ABUT_TOP} Q {CX} {ABUT_TOP + 36} {CX - 100} {ABUT_TOP} Z" fill="url(#collar)"/>

<!-- crown -->
<path d="{crown_path()}" fill="url(#enamel)"/>
<path d="{crown_path()}" fill="url(#enamelEdge)" opacity=".75"/>
<path d="{crown_path()}" fill="url(#occlusal)" opacity=".85"/>
{fissures()}
<path d="{crown_path()}" fill="url(#gloss)"/>

<!-- specular highlights -->
<path d="M {CX - 78} {CROWN_TOP + 70} Q {CX - 104} {CROWN_TOP + 140} {CX - 96} {CROWN_TOP + 208} Q {CX - 90} {CROWN_TOP + 254} {CX - 66} {CROWN_TOP + 284}" stroke="rgba(255,255,255,.85)" stroke-width="24" stroke-linecap="round" fill="none" filter="url(#soft)" opacity=".7"/>
<ellipse cx="{CX + 62}" cy="{CROWN_TOP + 96}" rx="24" ry="40" fill="#fff" opacity=".5" filter="url(#soft)" transform="rotate(18 {CX + 62} {CROWN_TOP + 96})"/>
<path d="M {CX - 118} {CROWN_NECK - 36} Q {CX} {CROWN_NECK + 8} {CX + 118} {CROWN_NECK - 36}" stroke="rgba(90,108,120,.22)" stroke-width="10" fill="none" filter="url(#soft)"/>
</svg>
'''

dest = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'demo/dental/assets/hero-implant.svg')
open(dest, 'w').write(svg)
print('svg written', len(svg), 'bytes ->', dest)
