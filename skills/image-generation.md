# Skill: Image Generation for LinkedIn Posts

## Purpose
Generate a matching image for every LinkedIn post draft. Images are saved locally and attached to the Slack approval thread so team members can download and use them when posting on LinkedIn.

## Prerequisites
- Post draft is ready (from post-generation.md skill)
- Brand guidelines: see docs/brand-guidelines.md
- Canva MCP connected (registered as claude.ai Canva — authenticate if needed)
- Output directory: `output/posts/images/` (create if missing)

---

## Step 1: Decide Which Image Type to Generate

Read the post draft and apply this decision logic:

```
Does the post lead with a specific number or metric?
  YES → Generate a DATA VISUALIZATION (Type A: matplotlib)

Does the post announce a feature, partnership, or milestone?
  YES → Generate a BRANDED GRAPHIC (Type B: Canva)

Does the post have BOTH a key metric AND a milestone angle?
  YES → Generate BOTH (two images — one of each type)

Is the post opinion/commentary with no data?
  YES → Generate a BRANDED GRAPHIC (Type B: Canva — quote card)
```

---

## Type A: Data Visualization (matplotlib)

Use when the post is data-led (adoption rates, growth trends, outcome metrics).

### What to Generate

| Post Metric | Chart Type |
|-------------|-----------|
| Week-over-week growth | Line chart |
| Feature adoption comparison | Bar chart (horizontal) |
| Before/after improvement | Side-by-side bars |
| Distribution / breakdown | Simple bar or pie |
| Single headline number | Stat card (text-based, no chart) |

### Code Template

When generating matplotlib images, write a Python script and run it via Bash:

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Brand colors (update hex codes once confirmed from Canva brand kit)
RUMI_ACCENT = "#E8533A"      # coral/red — TBD confirm
RUMI_BLUE = "#2B7CE9"        # blue secondary — TBD confirm
TALEEMABAD_PRIMARY = "#1A7A5E"  # teal/green — TBD confirm
BG_WHITE = "#FFFFFF"
TEXT_DARK = "#1A1A1A"
TEXT_MUTED = "#666666"

fig, ax = plt.subplots(figsize=(12, 6.28))  # 1200x628 ratio
fig.patch.set_facecolor(BG_WHITE)
ax.set_facecolor(BG_WHITE)

# [Chart code here — varies by type]

# Branding footer
fig.text(0.5, 0.04, 'hellorumi.ai', ha='center',
         fontsize=11, color=TEXT_MUTED, style='italic')

# Title
ax.set_title('[Post headline or metric]', fontsize=18, fontweight='bold',
             color=TEXT_DARK, pad=20)

plt.tight_layout()
plt.savefig('output/posts/images/YYYY-MM-DD-[author]-[topic].png',
            dpi=150, bbox_inches='tight', facecolor=BG_WHITE)
plt.close()
print("Saved: output/posts/images/YYYY-MM-DD-[author]-[topic].png")
```

### Bar Chart Example (Feature Adoption)

```python
features = ['Lesson Plans', 'Coaching', 'Quizzes', 'Assessments']
adoption = [45, 32, 61, 28]
colors = [RUMI_ACCENT if v == max(adoption) else RUMI_BLUE for v in adoption]

bars = ax.barh(features, adoption, color=colors, height=0.5)
ax.set_xlabel('Adoption Rate (%)', color=TEXT_MUTED)
ax.set_xlim(0, 80)

for bar, val in zip(bars, adoption):
    ax.text(val + 1, bar.get_y() + bar.get_height()/2,
            f'{val}%', va='center', fontweight='bold', color=TEXT_DARK)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

### Line Chart Example (Week-over-Week)

```python
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
values = [120, 185, 210, 267]

ax.plot(weeks, values, color=RUMI_ACCENT, linewidth=3, marker='o',
        markersize=8, markerfacecolor=RUMI_ACCENT)
ax.fill_between(range(len(weeks)), values, alpha=0.1, color=RUMI_ACCENT)

for i, (w, v) in enumerate(zip(weeks, values)):
    ax.annotate(f'{v}', (i, v), textcoords="offset points",
                xytext=(0, 10), ha='center', fontweight='bold', color=TEXT_DARK)

ax.set_xticks(range(len(weeks)))
ax.set_xticklabels(weeks)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

### Output Naming Convention
```
output/posts/images/YYYY-MM-DD-[author-initials]-[topic-slug]-chart.png
# Example: output/posts/images/2026-06-18-pm1-lesson-plans-adoption-chart.png
```

---

## Type B: Branded Canva Graphic

Use when the post is about a win, launch, partnership, or opinion — where the image should feel brand-forward, not data-forward.

### Prerequisites
1. Canva MCP must be authenticated (use `/mcp` → select "claude.ai Canva")
2. Brand templates must exist in Canva Pro (see docs/brand-guidelines.md for setup)

### Available Templates

Once templates are created in Canva Pro, record their IDs here:

| Template | Canva Template ID | Use Case |
|----------|------------------|----------|
| Stat Card (1200×628) | [ADD AFTER CREATING] | Big metric headline |
| Stat Card (1080×1080) | [ADD AFTER CREATING] | Square metric post |
| Quote Card (1080×1080) | [ADD AFTER CREATING] | Pull quote, teacher voice |
| Announcement Card (1200×628) | [ADD AFTER CREATING] | Feature launch, partnership |

### How to Generate a Canva Image

1. Identify which template fits the post (see table above)
2. Extract the key visual elements from the post:
   - **Stat card:** Headline number + 1-line context
   - **Quote card:** Pull quote (max 20 words) + author name
   - **Announcement card:** Bold headline + subtext (max 15 words)
3. Use Canva MCP to create a design from the template
4. Download the image
5. Save to `output/posts/images/` with the naming convention below

### Output Naming Convention
```
output/posts/images/YYYY-MM-DD-[author-initials]-[topic-slug]-card.png
# Example: output/posts/images/2026-06-18-pm2-q4-growth-milestone-card.png
```

### Fallback (if Canva MCP unavailable)
If Canva MCP is not authenticated or throws an error:
- Generate a clean text-based matplotlib image using the brand colors
- Use a simple card layout: white background, dark headline text, accent color bar at top/bottom, Rumi/Taleemabad wordmark
- Note in the Slack message: "Canva graphic unavailable — using matplotlib card as substitute"

---

## Step 2: Generate the Image

Run the Python script (Type A) or call Canva MCP (Type B).

For Type A, use Bash to execute:
```bash
python output/posts/images/generate_[date]_[slug].py
```

Or write and execute inline Python code directly.

---

## Step 3: Verify the Output

After generating:
- [ ] File exists in `output/posts/images/`
- [ ] File size > 0 (not empty/corrupt)
- [ ] Image matches the post's key message
- [ ] Brand colors are applied correctly
- [ ] Text is readable (not too small, not overflowing)
- [ ] Logo/branding is present

If anything looks wrong, regenerate before sending to Slack.

---

## Step 4: Pass to Slack Integration

After image is verified, hand off to `slack-integration.md` with:
- Post draft text
- Image file path: `output/posts/images/[filename].png`
- Image type (chart or branded card)

The Slack message will include the image as an attachment in the approval thread.

---

## Common Mistakes & How to Avoid

| Mistake | Fix |
|---------|-----|
| Using unverified data in chart labels | Only use numbers directly from Rumi query results |
| Chart has no title or axis labels | Always include descriptive title + axis labels |
| Colors don't match brand | Check hex codes against docs/brand-guidelines.md |
| Image too small to read on mobile | Minimum 1200×628px, font size ≥ 14pt in chart |
| Canva MCP not authenticated | Use matplotlib fallback, note in Slack message |
| Forgetting to save the file | Always confirm `plt.savefig()` ran, check file exists |
| Generating image before post is finalized | Image should match the APPROVED post, not a draft |

---

## Decision Examples

**Post:** "45% of teachers adopted Lesson Plans in the first week — 3x faster than any previous feature"
→ **Type A** (bar chart showing feature adoption comparison, Lesson Plans highlighted)

**Post:** "We just crossed 10,000 coaching sessions. Here's what we've learned."
→ **Type B** (Stat card: "10,000 coaching sessions" + "and counting")

**Post:** "While 87% of districts lack AI policies, we built ours first. Here's why."
→ **Type B** (Quote card with the key tension as the pull quote)

**Post:** "Quiz completion rates jumped 28% this month. Teachers are using assessments differently."
→ **Type A + Type B** (line chart showing the trend + stat card for the milestone)

---

## Notes
- Images are owned by the team member posting — they download from Slack and upload to LinkedIn
- Agent never posts to LinkedIn directly
- Always generate AFTER the post draft is written (image should reinforce the post's core message)
- Update Canva template IDs in the table above once templates are created in Canva Pro
