import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

os.makedirs("output/posts/images", exist_ok=True)

# Brand Colors (approximate — confirm hex codes from Canva Pro brand kit)
RUMI_CORAL        = "#E85D3F"  # coral/red accent
RUMI_BLUE         = "#2E86DE"  # blue secondary
TALEEMABAD_ORANGE = "#F5821F"  # warm orange
TALEEMABAD_NAVY   = "#1A3C5E"  # dark navy
BG                = "#FFFFFF"
TEXT_DARK         = "#1C1C1C"
TEXT_MUTED        = "#6B7280"
DIVIDER           = "#E5E7EB"

OUT = "output/posts/images"

# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE 1: STAT CARD  (1200 x 628)
# Layout: top accent bar | big number | context | brand tag
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6.28))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 12)
ax.set_ylim(0, 6.28)
ax.axis('off')

ax.add_patch(patches.Rectangle((0, 5.88), 12, 0.4, color=RUMI_CORAL, zorder=3))

ax.text(6, 4.0, "45%", ha='center', va='center',
        fontsize=96, fontweight='bold', color=RUMI_CORAL, fontfamily='DejaVu Sans')

ax.text(6, 2.7, "of teachers adopted Lesson Plans in the first week",
        ha='center', va='center', fontsize=20, color=TEXT_DARK, fontfamily='DejaVu Sans')

ax.text(6, 2.1, "3x faster than any previous feature launch",
        ha='center', va='center', fontsize=14, color=TEXT_MUTED,
        fontfamily='DejaVu Sans', style='italic')

ax.plot([0.5, 11.5], [0.85, 0.85], color=DIVIDER, linewidth=1)

ax.text(11.6, 0.45, "hellorumi.ai", ha='right', va='center',
        fontsize=12, color=RUMI_CORAL, fontweight='bold', fontfamily='DejaVu Sans')

ax.text(0.4, 0.45, "Rumi  |  Product Insights", ha='left', va='center',
        fontsize=12, color=TEXT_MUTED, fontfamily='DejaVu Sans')

plt.tight_layout(pad=0)
path1 = f"{OUT}/template-stat-card.png"
fig.savefig(path1, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Saved: " + path1)


# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE 2: QUOTE CARD  (1080 x 1080 square)
# Layout: top brand bar | big quote | author | bottom nav bar
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10.8, 10.8))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 10.8)
ax.set_ylim(0, 10.8)
ax.axis('off')

ax.add_patch(patches.Rectangle((0, 9.8), 10.8, 1.0, color=RUMI_CORAL))
ax.text(5.4, 10.3, "RUMI  |  TEACHER VOICE", ha='center', va='center',
        fontsize=13, color='white', fontweight='bold', fontfamily='DejaVu Sans')

ax.text(1.2, 8.5, "“", ha='center', va='center',
        fontsize=120, color=RUMI_CORAL, alpha=0.15, fontfamily='DejaVu Sans')

quote = "While 87% of districts lack AI policies,\nwe built ours first.\nHere’s why."
ax.text(5.4, 6.2, quote, ha='center', va='center',
        fontsize=28, color=TEXT_DARK, fontfamily='DejaVu Sans',
        linespacing=1.6, fontweight='bold')

ax.plot([3.5, 7.3], [4.3, 4.3], color=RUMI_CORAL, linewidth=2)

ax.text(5.4, 3.6, "Growth Marketing Manager  |  Taleemabad",
        ha='center', va='center', fontsize=15, color=TEXT_MUTED, fontfamily='DejaVu Sans')

ax.add_patch(patches.Rectangle((0, 0), 10.8, 1.1, color=TALEEMABAD_NAVY))
ax.text(5.4, 0.55, "Transforming Education Across Pakistan  |  taleemabad.com",
        ha='center', va='center', fontsize=13, color='white', fontfamily='DejaVu Sans')

plt.tight_layout(pad=0)
path2 = f"{OUT}/template-quote-card.png"
fig.savefig(path2, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Saved: " + path2)


# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE 3: ANNOUNCEMENT CARD  (1200 x 628)
# Layout: left navy panel with headline | right white panel with stats
# ─────────────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 6.28))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(0, 12)
ax.set_ylim(0, 6.28)
ax.axis('off')

ax.add_patch(patches.Rectangle((0, 0), 5.2, 6.28, color=TALEEMABAD_NAVY))

badge = patches.FancyBboxPatch((0.4, 5.3), 1.4, 0.5,
    boxstyle="round,pad=0.05", facecolor=TALEEMABAD_ORANGE, edgecolor='none')
ax.add_patch(badge)
ax.text(1.1, 5.55, "NEW", ha='center', va='center',
        fontsize=13, color='white', fontweight='bold', fontfamily='DejaVu Sans')

ax.text(2.6, 3.5, "Lesson Plans\nis Live", ha='center', va='center',
        fontsize=42, color='white', fontweight='bold', fontfamily='DejaVu Sans',
        linespacing=1.2)

ax.text(2.6, 2.0, "Draft  |  Iterate  |  Share", ha='center', va='center',
        fontsize=16, color=TALEEMABAD_ORANGE, fontfamily='DejaVu Sans', fontweight='bold')

ax.text(2.6, 0.55, "hellorumi.ai", ha='center', va='center',
        fontsize=13, color='white', alpha=0.6, fontfamily='DejaVu Sans')

ax.text(8.6, 5.2, "What teachers said:", ha='center', va='center',
        fontsize=14, color=TEXT_MUTED, fontfamily='DejaVu Sans', style='italic')

stats = [("45%", "adopted in week 1"), ("3 days", "avg. time to first plan"), ("2x", "more time in Rumi")]
y_positions = [4.1, 3.0, 1.9]
for (num, label), y in zip(stats, y_positions):
    ax.text(7.0, y + 0.25, num, ha='left', va='center',
            fontsize=30, fontweight='bold', color=RUMI_CORAL, fontfamily='DejaVu Sans')
    ax.text(7.0, y - 0.2, label, ha='left', va='center',
            fontsize=13, color=TEXT_MUTED, fontfamily='DejaVu Sans')
    ax.plot([7.0, 11.5], [y - 0.5, y - 0.5], color=DIVIDER, linewidth=0.8)

ax.text(11.6, 0.35, "#EdTech #Rumi", ha='right', va='center',
        fontsize=11, color=TEXT_MUTED, fontfamily='DejaVu Sans', style='italic')

plt.tight_layout(pad=0)
path3 = f"{OUT}/template-announcement-card.png"
fig.savefig(path3, dpi=150, bbox_inches='tight', facecolor=BG)
plt.close()
print("Saved: " + path3)

print("\nAll 3 templates generated successfully.")
