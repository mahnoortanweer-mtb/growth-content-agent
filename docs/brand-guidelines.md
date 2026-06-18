# Brand Guidelines: Taleemabad & Rumi

**Status:** Partial — hex codes to be confirmed from Canva Pro brand kit
**Last Updated:** 2026-06-18

Use this doc when generating images for LinkedIn posts. Apply these guidelines to both matplotlib data viz and Canva branded graphics.

---

## Taleemabad Brand

### Identity
- **Full name:** Taleemabad
- **Tagline:** "Transforming Education Across Pakistan"
- **Mission:** "We believe everyone can be extraordinary"
- **Voice:** Optimistic, empowering, mission-driven
- **Audience:** Educators, ed-sector partners, investors, policymakers

### Visual Style
- Modern, clean, professional
- Data-forward (charts, numbers, outcomes)
- Photography: real educators/students (not stock)
- Layout: structured, left-aligned, generous whitespace

### Colors
| Role | Description | Hex |
|------|-------------|-----|
| Primary | Dark navy | #1A3C5E |
| Accent | Warm orange | #F5821F |
| Background | White | #FFFFFF |
| Text | Near-black | #1C1C1C |
| Text muted | Gray | #6B7280 |

> Note: Confirm exact hex codes against Canva Pro brand kit — update if different.

### Typography
- **Headings:** Bold, modern sans-serif (confirm exact font from Canva)
- **Body:** Clean, readable sans-serif
- **Numbers/Data:** Extra-bold, large, high contrast

---

## Rumi Brand

### Identity
- **Full name:** Rumi (hellorumi.ai)
- **Tagline:** "You're not teaching alone"
- **Voice:** Conversational, teacher-centric, warm, accessible
- **Audience:** Teachers, school admins, ed-tech practitioners

### Visual Style
- Minimalist, flat design
- Clean card layouts
- Lots of whitespace
- Simple iconography

### Colors
| Role | Description | Hex |
|------|-------------|-----|
| Primary accent | Coral/red | #E85D3F |
| Secondary | Blue | #2E86DE |
| Background | White | #FFFFFF |
| Text | Dark | #1C1C1C |
| Text muted | Gray | #6B7280 |
| Divider | Light gray | #E5E7EB |

> Note: Confirm exact hex codes against Canva Pro brand kit — update if different.

### Typography
- **Brand font:** Clean sans-serif (confirm from Canva)
- **Data/Numbers:** Bold, high contrast
- **Body:** Regular weight, comfortable line height

---

## LinkedIn Post Image Specs

| Format | Dimensions | Use Case |
|--------|-----------|----------|
| Landscape | 1200 × 628 px | Standard feed post |
| Square | 1080 × 1080 px | Carousel, standalone image |

---

## Which Brand to Use Per Post

| Post Author | Brand to Apply |
|-------------|----------------|
| Growth PMs (product metrics) | Rumi brand (product-focused) |
| Partnership Manager | Taleemabad brand (org-level) |
| Marketing Manager | Taleemabad brand (audience-facing) |
| Mission/impact posts | Taleemabad brand |
| Feature/product posts | Rumi brand |

---

## Template Specs (3 Canva Templates)

### Template 1: Stat Card
- **Use:** Posts with a headline metric (e.g., "45% adoption in 7 days")
- **Layout:** Big number top-center → short context line → logo bottom-right
- **Brand:** Rumi (data/product) or Taleemabad (impact metrics)
- **Dimensions:** Both 1200×628 and 1080×1080 variants

### Template 2: Quote Card
- **Use:** Pull quotes from the post, teacher testimonials, opinion-led posts
- **Layout:** Large quote text center → author name small → brand bar at bottom
- **Brand:** Rumi (teacher voice) or Taleemabad (mission voice)
- **Dimensions:** 1080×1080 (square preferred for quotes)

### Template 3: Announcement Card
- **Use:** Feature launches, partnerships, milestones
- **Layout:** Bold headline → short subtext → brand color bar → logo
- **Brand:** Match post author's team (product → Rumi, org → Taleemabad)
- **Dimensions:** 1200×628 (landscape preferred for announcements)

---

## Setup Checklist (Canva Pro)

Before using image generation in the agent workflow, complete these in Canva:

- [ ] Add Taleemabad logo to brand kit
- [ ] Add Rumi logo to brand kit
- [x] Create Template 1: Stat Card (1200x628) — output/posts/images/template-stat-card.png
- [x] Create Template 2: Quote Card (1080x1080) — output/posts/images/template-quote-card.png
- [x] Create Template 3: Announcement Card (1200x628) — output/posts/images/template-announcement-card.png
- [x] matplotlib confirmed available (Python 3.12, matplotlib 3.11)
- [ ] Confirm hex codes vs Canva Pro brand kit — update if different
- [ ] Set correct fonts in Canva (current templates use DejaVu Sans as placeholder)
- [ ] If Canva MCP available: recreate templates with actual brand fonts/logo

---

## Getting Hex Codes

To get exact hex codes from your Canva Pro brand kit:
1. Open Canva Pro → Brand Hub → Your brand
2. Click any color swatch → copy the hex code
3. Update the "Hex (confirm from Canva)" column above
4. Also update the hex values in the matplotlib color constants in `skills/image-generation.md`
