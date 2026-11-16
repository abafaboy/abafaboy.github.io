"""Shared figure style for the paper. Import and call apply() before plotting.

Palette and mark specs follow a validated, colorblind-safe categorical order
(adjacent-pair CVD checked). Rules the figures must follow:
  - assign series colors in the fixed order of SERIES; never cycle or reuse
  - one y-axis per panel (no twin axes); use small multiples instead
  - 2px lines, markers >= 8px with a surface-colored ring, hairline solid grid
  - text is ink-colored, never series-colored; legend for >= 2 series
  - label selectively (endpoints / the key value), not every point
"""
import matplotlib as mpl

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
# fixed categorical order: blue, orange, aqua, yellow, magenta, green, violet, red
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = SERIES
# sequential single-hue ramp (light -> dark) for ordered quantities
SEQ = ["#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
REFERENCE = "#898781"   # theory / reference lines: muted gray, dashed is fine for a reference


def apply():
    mpl.rcParams.update({
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "figure.dpi": 110, "savefig.dpi": 200, "savefig.bbox": "tight", "savefig.pad_inches": 0.08,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
        "font.size": 10, "axes.titlesize": 11, "axes.labelsize": 10,
        "axes.titleweight": "bold", "axes.titlelocation": "left", "axes.titlepad": 8,
        "text.color": INK, "axes.labelcolor": INK2, "axes.titlecolor": INK,
        "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
        "xtick.labelsize": 9, "ytick.labelsize": 9,
        "axes.edgecolor": AXIS, "axes.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "grid.linestyle": "-",
        "axes.axisbelow": True,
        "lines.linewidth": 2.0, "lines.markersize": 7, "lines.solid_capstyle": "round",
        "lines.markeredgecolor": SURFACE, "lines.markeredgewidth": 1.5,
        "axes.prop_cycle": mpl.cycler(color=SERIES),
        "legend.frameon": False, "legend.fontsize": 9,
        "svg.fonttype": "none", "mathtext.fontset": "dejavusans",
    })


def save(fig, path_without_ext):
    """Save both SVG (for the web page) and PNG (fallback / PDF)."""
    fig.savefig(str(path_without_ext) + ".svg")
    fig.savefig(str(path_without_ext) + ".png")
