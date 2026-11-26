"""Draws the CJW Apps, CJW Entertainment and CJW Business logos as SVG files in assets/brand, traced from the design
sheet of 26 Nov 2026 (navy #0F1720, white, blue #78BDEF; measured from the sheet).

    python3 tools/make_logos.py
    # then the PNG icons (needs rsvg-convert):
    rsvg-convert -w 32 assets/brand/cjw-apps-icon.svg -o assets/icons/favicon-32.png
    rsvg-convert -w 180 assets/brand/cjw-apps-icon.svg -o assets/icons/apple-touch-icon.png
    rsvg-convert -w 512 assets/brand/cjw-apps-icon.svg -o assets/brand/cjw-apps-icon-512.png
"""
import math, os

NAVY, WHITE, BLUE = "#0F1720", "#FFFFFF", "#78BDEF"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "brand")
os.makedirs(OUT, exist_ok=True)

# Pointy-top hexagon in a 100 x 100 box
R, CX, CY = 48, 50, 50
def hexpts(r=R, cx=CX, cy=CY):
    return [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in (-90, -30, 30, 90, 150, 210)]
def poly(pts, fill, extra=""):
    return f'<polygon points="{" ".join(f"{x:.2f},{y:.2f}" for x, y in pts)}" fill="{fill}"{extra}/>'

def edge_y_top(x):      # y on the two upper edges at x
    return 2 + abs(x - 50) * math.tan(math.radians(30))
def edge_y_bottom(x):   # y on the two lower edges at x
    return 98 - abs(x - 50) * math.tan(math.radians(30))

# ---------------------------------------------------------------- the CJW mark (parent)
# Traced from the design sheet (zoomed 9x: x 45..705, y 18..705), then fitted into the 100 x 100 box.
def _fit(pts, x0=375, y0=361.5, k=96 / 687):
    return [((x - x0) * k + 50, (y - y0) * k + 50) for x, y in pts]

def mark_apps(fg=WHITE, blue=BLUE):
    C = [(300, 65), (45, 195), (45, 520), (190, 600), (190, 505), (125, 470), (125, 250), (215, 200), (215, 285), (300, 245)]
    J = [(330, 160), (415, 195), (415, 690), (375, 705), (215, 620), (215, 450), (300, 410), (300, 560), (330, 575)]
    DOT = [(340, 35), (375, 18), (410, 38), (410, 145), (340, 108)]
    W = [(455, 70), (535, 105), (535, 430), (580, 350), (625, 430), (625, 170), (705, 205), (705, 540), (615, 565),
         (580, 490), (455, 660)]
    return poly(_fit(C), fg) + poly(_fit(J), fg) + poly(_fit(DOT), blue) + poly(_fit(W), blue)

# ---------------------------------------------------------------- rings
def half_rings(r_out, width, left, right):
    """A hexagon ring as two filled halves (white left, blue right) with a thin navy split at top and bottom."""
    o = hexpts(r_out)
    i = hexpts(r_out - width / math.cos(math.radians(30)))
    top, ur, lr, bot, ll, ul = o
    itop, iur, ilr, ibot, ill, iul = i
    gap = 0.9
    L = [(top[0] - gap, top[1] + 0.5), ul, ll, (bot[0] - gap, bot[1] - 0.5), (ibot[0] - gap, ibot[1]), ill, iul, (itop[0] - gap, itop[1])]
    R_ = [(top[0] + gap, top[1] + 0.5), ur, lr, (bot[0] + gap, bot[1] - 0.5), (ibot[0] + gap, ibot[1]), ilr, iur, (itop[0] + gap, itop[1])]
    return poly(L, left) + poly(R_, right)

# ---------------------------------------------------------------- the Entertainment mark
def mark_entertainment(fg=WHITE, blue=BLUE):
    s = [half_rings(47, 8.5, fg, blue)]
    # the book's cover: a band under the pages, white left, blue right
    s.append(poly([(49.2, 41), (16.5, 34), (16.5, 81), (49.2, 92)], fg))
    s.append(poly([(50.8, 41), (83.5, 34), (83.5, 81), (50.8, 92)], blue))
    s.append(poly([(48.4, 40.5), (19, 34.5), (19, 78.5), (48.4, 88)], NAVY))
    s.append(poly([(51.6, 40.5), (81, 34.5), (81, 78.5), (51.6, 88)], NAVY))
    # pages
    s.append(poly([(47.6, 42), (20.5, 36), (20.5, 77), (47.6, 86)], fg))
    s.append(poly([(52.4, 42), (79.5, 36), (79.5, 77), (52.4, 86)], blue))
    # fanned pages above the book
    for i in range(3):
        y = 33 - i * 5
        s.append(poly([(48.4, 39 - i * 2.2), (23 + i * 4, y), (23 + i * 4, y + 3.2), (48.4, 41.6 - i * 2.2)], blue if i == 1 else fg))
        s.append(poly([(51.6, 39 - i * 2.2), (77 - i * 4, y), (77 - i * 4, y + 3.2), (51.6, 41.6 - i * 2.2)], fg if i == 1 else blue))
    # the sound wave: a line right across, with bars on each page
    s.append(f'<path d="M4.5,57.5 H95.5" stroke="{NAVY}" stroke-width="2"/>')
    s.append(f'<path d="M4.5,57.5 H13" stroke="#3A4654" stroke-width="2"/><path d="M87,57.5 H95.5" stroke="#3A4654" stroke-width="2"/>')
    bars = [4, 8, 14, 18, 12, 7, 3]
    for n, h in enumerate(bars):
        for x in (26.5 + n * 2.6, 73.5 - n * 2.6):
            s.append(f'<path d="M{x:.2f},{57.5 - h / 2:.2f} V{57.5 + h / 2:.2f}" stroke="{NAVY}" stroke-width="1.5"/>')
    return "".join(s)

# ---------------------------------------------------------------- the Business mark
def mark_business(fg=WHITE, blue=BLUE):
    s = [half_rings(47, 9, fg, blue)]
    # navy breaks in the outer ring where the circuit nodes sit
    s.append(f'<rect x="1" y="44" width="14" height="12" fill="{NAVY}"/><rect x="85" y="44" width="14" height="12" fill="{NAVY}"/>')
    # inner ring: blue, with a white cap at the top
    s.append(half_rings(33, 7, blue, blue))
    t = hexpts(33)
    for sign in (1, -1):  # white caps at the top and the bottom
        y0 = 50 - sign * 33
        s.append(poly([(50, y0), (50 - 15, y0 + sign * 8.66), (50 - 15 + 4.2, y0 + sign * 8.66 + sign * 5.4), (50, y0 + sign * 8.1),
                       (50 + 15 - 4.2, y0 + sign * 8.66 + sign * 5.4), (50 + 15, y0 + sign * 8.66)], fg))
    # nodes and their lines
    s.append(f'<path d="M14,50 H22" stroke="{fg}" stroke-width="2.6"/><path d="M78,50 H86" stroke="{blue}" stroke-width="2.6"/>')
    s.append(f'<rect x="5.5" y="45.5" width="9" height="9" fill="{NAVY}" stroke="{fg}" stroke-width="2.8"/>')
    s.append(f'<rect x="85.5" y="45.5" width="9" height="9" fill="{NAVY}" stroke="{blue}" stroke-width="2.8"/>')
    # the cube: blue top, white left face, blue right face, navy outline, a navy window on each side
    c, a = 50, 15
    tp = [(c, 33.5), (c + a, 42), (c, 50.5), (c - a, 42)]
    lf = [(c - a, 42), (c, 50.5), (c, 67.5), (c - a, 59)]
    rf = [(c, 50.5), (c + a, 42), (c + a, 59), (c, 67.5)]
    st = f' stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"'
    s.append(poly([(c, 30), (c + a + 3.5, 40), (c + a + 3.5, 61), (c, 71), (c - a - 3.5, 61), (c - a - 3.5, 40)], NAVY))
    s.append(poly(tp, blue, st) + poly(lf, fg, st) + poly(rf, blue, st))
    s.append(poly([(c - 10, 50), (c - 4.5, 53), (c - 4.5, 61), (c - 10, 58)], NAVY))
    s.append(poly([(c + 4.5, 53), (c + 10, 50), (c + 10, 58), (c + 4.5, 61)], NAVY))
    return "".join(s)

# ---------------------------------------------------------------- the lettering (a small squared, rounded stroke font)
G = {  # glyph: (width, path on a 10-high cap grid, baseline y=10, x-height y=3)
    "C": (8.6, "M8.6,0 H2.4 Q0,0 0,2.4 V7.6 Q0,10 2.4,10 H8.6"),
    "J": (7.6, "M7.6,0 V7.6 Q7.6,10 5.2,10 H2.4 Q0,10 0,7.6 V6.6"),
    "W": (12.4, "M0,0 L3,10 L6.2,1.4 L9.4,10 L12.4,0"),
    "A": (9, "M0,10 L4.5,0 L9,10 M1.8,6.4 H7.2"),
    "p": (6.8, "M0,13.2 V3 H4.6 Q6.8,3 6.8,5.2 V7.8 Q6.8,10 4.6,10 H0"),
    "s": (6.2, "M6.2,3 H1.7 Q0,3 0,4.75 Q0,6.5 1.7,6.5 H4.5 Q6.2,6.5 6.2,8.25 Q6.2,10 4.5,10 H0"),
    "E": (7.4, "M7.4,0 H0 V10 H7.4 M0,5 H6.4"),
    "n": (6.6, "M0,10 V3 H4.4 Q6.6,3 6.6,5.2 V10"),
    "t": (4.4, "M1.4,0.6 V7.8 Q1.4,10 3.6,10 H4.4 M0,3 H4.4"),
    "e": (6.8, "M0.1,6.6 H6.8 V5.2 Q6.8,3 4.6,3 H2.2 Q0,3 0,5.2 V7.8 Q0,10 2.2,10 H6.4"),
    "r": (4.8, "M0,10 V5.2 Q0,3 2.2,3 H4.8"),
    "a": (6.6, "M0.4,3 H4.4 Q6.6,3 6.6,5.2 V10 H1.8 Q0,10 0,8.3 Q0,6.6 1.8,6.6 H6.6"),
    "i": (0, "M0,3.2 V10 M0,0.2 V1.4"),
    "m": (9.8, "M0,10 V3 H7.6 Q9.8,3 9.8,5.2 V10 M4.9,3 V10"),
    "B": (7.8, "M0,0 H5.3 Q7.3,0 7.3,2.3 Q7.3,4.7 5.3,4.7 H0 M0,4.7 H5.6 Q7.8,4.7 7.8,7.35 Q7.8,10 5.6,10 H0 V0"),
    "u": (6.6, "M0,3 V7.8 Q0,10 2.2,10 H6.6 V3"),
}
def word(text, x, y_base, cap, stroke, colour, gap=2.1):
    """One word: cap = cap height in px; returns (svg, width)."""
    k = cap / 10
    out, cx = [], x
    for ch in text:
        w, d = G[ch]
        out.append(f'<path transform="translate({cx:.2f},{y_base - cap:.2f}) scale({k:.4f})" d="{d}" fill="none" stroke="{colour}" '
                   f'stroke-width="{stroke / k:.3f}" stroke-linecap="butt" stroke-linejoin="round" vector-effect="none"/>')
        cx += (w + gap) * k + (stroke if w == 0 else 0)
    return "".join(out), cx - x - gap * k

# ---------------------------------------------------------------- whole logos
def logo(kind, fg, blue, bg=None, name=None):
    mark = {"apps": mark_apps, "entertainment": mark_entertainment, "business": mark_business}[kind](fg, blue)
    tx = 118
    if kind == "apps":
        a, wa = word("CJW", tx, 44, 32, 7.0, fg, gap=2.4)
        b, wb = word("App" + "s", tx, 90, 32, 7.0, blue, gap=2.2)
        width = tx + max(wa, wb) + 8
    else:
        sub = {"entertainment": "Entertainment", "business": "Business"}[kind]
        a, wa = word("CJW", tx, 50, 32, 7.0, fg, gap=2.4)
        b, wb = word(sub, tx, 82, 18, 3.4, blue, gap=1.9)
        width = tx + max(wa, wb) + 8
    height = 100
    body = (f'<rect width="{width:.0f}" height="{height}" fill="{bg}"/>' if bg else "") + f"<g>{mark}</g>" + a + b
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height}" width="{width * 2:.0f}" height="{height * 2}" '
            f'role="img" aria-label="{name}">{body}</svg>')

def mark_svg(kind, fg=WHITE, blue=BLUE, bg=None, pad=0, radius=0, name=""):
    mark = {"apps": mark_apps, "entertainment": mark_entertainment, "business": mark_business}[kind](fg, blue)
    size = 100 + 2 * pad
    back = f'<rect width="{size}" height="{size}" rx="{radius}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" role="img" aria-label="{name}">{back}'
            f'<g transform="translate({pad},{pad})">{mark}</g></svg>')

NAMES = {"apps": "CJW Apps", "entertainment": "CJW Entertainment", "business": "CJW Business"}
for kind in NAMES:
    open(f"{OUT}/cjw-{kind}-logo.svg", "w").write(logo(kind, WHITE, BLUE, name=NAMES[kind]))           # for dark backgrounds
    open(f"{OUT}/cjw-{kind}-logo-light.svg", "w").write(logo(kind, NAVY, "#2F86CF", name=NAMES[kind]))  # for light backgrounds
    open(f"{OUT}/cjw-{kind}-mark.svg", "w").write(mark_svg(kind, name=NAMES[kind]))
    open(f"{OUT}/cjw-{kind}-icon.svg", "w").write(mark_svg(kind, bg=NAVY, pad=14, radius=26, name=NAMES[kind]))
print("Logos written to", OUT)
