# Memory: LinkedIn Content Agent

## Post History

### Post #1 (2026-06-16)
- Author: Growth Product Manager 1
- Topic: Feature launch (Lesson Plans)
- Data used: 45% adoption, 3-day TTU, 2x session time increase
- Posted URL: https://www.linkedin.com/posts/growth-pm-1/lesson-plans-launch/ (simulated)
- Date posted: 2026-06-16
- Status: Awaiting engagement data
- Engagement tracking date: 2026-06-23 (check in 7 days)

**Notes:** First post generated and approved via Slack. Process worked smoothly. 
Post sounded authentic, data was current, team member approved without tweaks.

## Performance Patterns
(To be filled after first week of posts)

## Team Feedback
(Document team member preferences as they emerge)

## Rumi Data Notes
(Record any quirks, update frequencies, or gotchas with the database)

## Trending Topics & Themes
(Track what resonates with audience)

## Continuous Improvements
(Document iterations and learnings)

## In Progress (2026-06-18)

### Image Generation Skill
- **Status:** ✅ COMPLETE — all files built and templates generated
- **Skill:** `skills/image-generation.md`
- **Brand guidelines:** `docs/brand-guidelines.md`
- **Templates generated (matplotlib):**
  - `output/posts/images/template-stat-card.png` (1200x628)
  - `output/posts/images/template-quote-card.png` (1080x1080 square)
  - `output/posts/images/template-announcement-card.png` (1200x628)
- **Generator script:** `output/generate_templates.py`
- **Brand colors used (approximate — confirm vs Canva Pro):**
  - Rumi coral: #E85D3F | Rumi blue: #2E86DE
  - Taleemabad navy: #1A3C5E | Taleemabad orange: #F5821F

### MCPs Connected
- **Rumi:** rumi-db (PostgreSQL via Supabase, 82 tables, 37 post-relevant)
- **Slack:** slack-rumi (Taleemabad workspace, #growth channel C0ATPQZV27M, bot U0BBGU4H2R0)
- **Canva:** Authenticated via /mcp — confirm tools available in fresh session

### GitHub
- Repo: https://github.com/mahnoortanweer-mtb/growth-content-agent
- Branch: main

### Next Steps
1. Fill in real team member names + Slack IDs in docs/team-roster.md
2. Run first real post end-to-end in Claude Code (Rumi query → post draft → image → Slack)
3. Optional: confirm brand hex codes vs Canva Pro → update in brand-guidelines.md + image-generation.md
4. Optional: if Canva MCP becomes available in a session, recreate templates with brand fonts/logos
