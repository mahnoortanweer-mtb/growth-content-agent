# Image Generation Skill — Design Specification

**Project:** LinkedIn Content Agent — Image Generation Add-on
**Date:** 2026-06-17
**Owner:** Mahnoor Tanweer
**Status:** Design approved, awaiting implementation

---

## 1. Purpose

Add image generation to the LinkedIn Content Agent so every post is accompanied by a visual. LinkedIn posts with images get 2-3x more engagement.

## 2. Two Image Types

### Type A: Data Visualization (metric-heavy posts)
- **Tool:** Python + matplotlib
- **When:** Post leads with Rumi metrics (adoption rates, retention curves, growth trends)
- **Output:** Chart/graph as PNG
- **Examples:** Retention curve, feature adoption bar chart, week-over-week growth line

### Type B: Branded Canva Graphic (team wins, milestones, commentary)
- **Tool:** Canva MCP
- **When:** Post is about team wins, feature launches, partnerships, industry commentary
- **Output:** Branded card as PNG
- **Examples:** Stat card, quote card, announcement card

---

## 3. Decision Logic

Agent auto-picks image type based on post content:

```
Post has metrics/data?
  YES → Data visualization (matplotlib)
  NO  → Canva branded graphic

Post has BOTH metrics AND milestone angle?
  → Data viz + branded stat card (two images)
```

---

## 4. Output & Delivery

Both image types:
1. **Saved** to `output/posts/images/YYYY-MM-DD-[author]-[topic].png`
2. **Attached** to Slack approval thread alongside the post draft

Team member sees image in Slack during review → approves or requests change → downloads when posting on LinkedIn.

---

## 5. Brand Guidelines

### Taleemabad
- **Tagline:** "Transforming Education Across Pakistan"
- **Style:** Modern, clean, professional, data-driven
- **Tone:** Optimistic, empowering
- **Key message:** "We believe everyone can be extraordinary"
- **Visual:** Structured layouts, data visualizations, educator photography

### Rumi
- **Tagline:** "You're not teaching alone"
- **Style:** Minimalist, clean, flat design
- **Tone:** Conversational, teacher-centric, accessible
- **Colors:** White background, dark text, coral/red accent, blue secondary
- **Logo:** Rumi wordmark with coral/red icon

### Colors to Use in Images
- **Primary background:** White
- **Primary text:** Dark (near black)
- **Accent:** Coral/red (Rumi brand)
- **Secondary:** Blue (data, charts)
- **Confirm exact hex codes:** Ask Mahnoor to share from Canva brand kit once set up

---

## 6. Canva Templates (3 to Create)

| Template | Use Case | Layout |
|----------|----------|--------|
| **Stat Card** | Big metric posts | Large number + context text + Rumi logo |
| **Quote Card** | Pull quote from post | Quote text + author name + brand bar |
| **Announcement Card** | Feature launch / partnership | Bold headline + subtext + brand bar |

All templates:
- LinkedIn dimensions: 1200x628px (landscape) for feed posts
- Square variant: 1080x1080px for carousel/standalone
- Consistent: Rumi logo bottom right, brand colors, clean fonts

---

## 7. Files to Create

```
skills/
└── image-generation.md        # New skill: how to generate images for posts

docs/
└── brand-guidelines.md        # Taleemabad + Rumi brand reference

output/
└── posts/
    └── images/                # Generated images saved here (already created)
```

---

## 8. Integration with Existing Workflow

Updated post generation flow:
```
1. rumi-analysis.md     → Find insight
2. post-generation.md   → Write post draft
3. image-generation.md  → Generate matching image  ← NEW
4. slack-integration.md → Send post + image to Slack for approval
5. performance-tracking.md → Track engagement
```

---

## 9. Implementation Steps

1. **Set up Canva branding** — Add Taleemabad/Rumi colors, fonts, logo to Canva Pro account
2. **Create 3 Canva templates** — Stat card, quote card, announcement card
3. **Write image-generation.md skill** — Decision logic, how to generate each type
4. **Write brand-guidelines.md doc** — Colors, fonts, logo usage reference
5. **Update slack-integration.md** — Include image attachment in Slack messages
6. **Update CLAUDE.md** — Add image generation to quick reference

---

## 10. Open Items

- [ ] Confirm exact hex codes for Taleemabad + Rumi (check Canva Pro account)
- [ ] Create 3 LinkedIn templates in Canva Pro
- [ ] Confirm matplotlib is available in Claude Code environment
- [ ] Confirm Canva MCP authentication (mcp__claude_ai_Canva available)
