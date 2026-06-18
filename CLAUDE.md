# Project: LinkedIn Content Agent

Automate daily LinkedIn posts for the growth team. Agent researches Rumi data, 
generates authentic content, coordinates via Slack for review and approval.

## Current Focus
- MVP launch: Rumi connection, daily post generation, Slack workflow
- External dashboards: Phase 2
- Team member feedback integration: Week 2+

## Team Roster
- **Mahnoor Tanweer** (Owner/Approver) — All posts reviewed by Mahnoor
- **Growth Product Manager 1** (Expertise: product adoption, feature launches)
- **Growth Product Manager 2** (Expertise: product metrics, engagement)
- **Growth Partnership Manager** (Expertise: integrations, partnerships)
- **Growth Marketing Manager** (Expertise: campaigns, brand, audience growth)

## Daily Schedule
Posts rotate through team members:
- Day 1: Growth Product Manager 1
- Day 2: Growth Product Manager 2
- Day 3: Growth Partnership Manager
- Day 4: Growth Marketing Manager
- (Then repeat)

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

## Quick Reference
- Rumi analysis: see skills/rumi-analysis.md
- Post generation: see skills/post-generation.md
- Slack workflow: see skills/slack-integration.md
- Performance tracking: see skills/performance-tracking.md
- **Internet research:** see skills/internet-research.md (NEW: add context from global EdTech trends)
- Team info: see docs/team-roster.md
- Trending topics: see docs/trending-topics.md
- Post examples: see docs/post-templates.md
- **EdTech insights:** see docs/internet-insights.md (NEW: verified market trends, educator sentiment, Taleemabad positioning)
