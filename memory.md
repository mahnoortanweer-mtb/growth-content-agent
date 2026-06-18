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
- **Status:** ✅ Skill built — `skills/image-generation.md` written
- **Brand guidelines:** ✅ `docs/brand-guidelines.md` written
- **Design doc:** docs/superpowers/specs/2026-06-17-image-generation-design.md
- **Two types:** Data viz (matplotlib) for metric posts, Canva branded graphics for wins/milestones
- **Canva MCP:** Authentication attempted — tools not yet available in session (try fresh session)
- **Remaining blocker:** Create 3 Canva templates (stat card, quote card, announcement card) in Canva Pro + fill in template IDs in skills/image-generation.md

### Brand Colors (Confirm & Update)
- Hex codes TBD — check Canva Pro brand kit, update in:
  - `docs/brand-guidelines.md` (color table)
  - `skills/image-generation.md` (matplotlib color constants)

### MCPs Connected
- **Rumi:** rumi-db (PostgreSQL via Supabase, 82 tables, 37 post-relevant)
- **Slack:** slack-rumi (Taleemabad workspace, #growth channel C0ATPQZV27M, bot U0BBGU4H2R0)
- **Canva:** Authenticated via /mcp — confirm tools available in fresh session

### GitHub
- Repo: https://github.com/mahnoortanweer-mtb/growth-content-agent
- Branch: main

### Next Steps
1. Open fresh Claude Code session → confirm Canva MCP tools are available
2. Get hex codes from Canva Pro brand kit → update brand-guidelines.md + image-generation.md
3. Create 3 Canva templates (stat card, quote card, announcement card)
4. Add Canva template IDs to skills/image-generation.md template table
5. Fill in real team member names + Slack IDs in docs/team-roster.md
6. Run first real post end-to-end (Rumi query → post draft → image → Slack)
