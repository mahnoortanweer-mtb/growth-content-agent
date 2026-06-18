# Project: LinkedIn Content Agent

Automate daily LinkedIn posts for the growth team. Agent researches Rumi data, 
generates authentic content, coordinates via Slack for review and approval.

## Current Focus
- MVP launch: Rumi connection, daily post generation, Slack workflow
- External dashboards: Phase 2
- Team member feedback integration: Week 2+

## Team Roster
- **Mahnoor Tanweer Butt** `U0AUB6PTGE8` — Owner/Approver. Tagged on EVERY post.
- **Waqas Tanveer** `U0ATVUT1RRU` — Growth Manager
- **Zeest Qureshi** `U0AUHKZCXL0` — Senior Growth Manager
- **Junaid Ali** `U0ATENTNF1D` — Growth Manager
- **Amina Tayyub** `U0AV1PKR3NV` — Product Growth Manager
- **Gul Perwasha** `U0AUA6DG415` — Growth Manager

## Daily Schedule
5-day rotation (started 2026-06-16):
- Day 1: Waqas Tanveer
- Day 2: Zeest Qureshi
- Day 3: Junaid Ali
- Day 4: Amina Tayyub
- Day 5: Gul Perwasha
- (Then repeat — day = days_since_2026-06-16 % 5)

## Key Rules
1. **Authenticity:** Posts sound like they're written by the team member, not generic AI
2. **Data-backed:** Every post must reference substantial data from Rumi
3. **Relevance:** Mix trending topics + team wins, BTS, product updates, features
4. **Approval:** Always tag Mahnoor + assigned team member in Slack
5. **No auto-posting:** Team members post manually on LinkedIn (agent doesn't post)
6. **Performance:** Track engagement to optimize future posts

## Rumi Connection
- Status: ✅ CONNECTED via MCP (registered as rumi-db)
- Host: aws-1-ap-southeast-1.pooler.supabase.com:6543
- Database: postgres (PostgreSQL via Supabase)
- Access: Read-only
- Tables: 82 total, 37 relevant for posts
- Schema: see docs/rumi-schema.md

## Key Rumi Tables for Posts
- User growth: `users`, `students`
- Feature adoption: `user_feature_first_use`, `lesson_plans`, `lesson_plan_requests`
- Engagement: `coaching_sessions`, `quiz_sessions`, `attendance_sessions`
- Outcomes: `reading_assessments`, `exam_submissions`, `student_video_feedback`
- Community: `feature_suggestions`

## Slack Connection
- Status: ✅ CONNECTED via MCP (registered as slack-rumi)
- Workspace: Taleemabad (taleemabad-talk.slack.com)
- Team ID: T0AGB7ATAE7
- Bot: growth_content_agent (User ID: U0BBGU4H2R0)
- Channel: C0ATPQZV27M (#growth)
- Verified: 2026-06-17 — test message delivered successfully

## Quick Reference
- Rumi analysis: see skills/rumi-analysis.md
- Post generation: see skills/post-generation.md
- Image generation: see skills/image-generation.md
- Slack workflow: see skills/slack-integration.md
- Performance tracking: see skills/performance-tracking.md
- Internet research: see skills/internet-research.md
- Team info: see docs/team-roster.md
- Trending topics: see docs/trending-topics.md
- Post examples: see docs/post-templates.md
- EdTech insights: see docs/internet-insights.md
- Brand guidelines: see docs/brand-guidelines.md
