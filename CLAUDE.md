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
- Status: ⏳ PENDING MCP SETUP (see instructions below)
- Access: Read-only (no write access)
- Key metrics: User growth, engagement, retention, feature adoption
- Schema: see docs/rumi-schema.md

### MCP Setup Instructions
In Claude Code, ask:
```
"Can you please set up an MCP for me? We need to connect to the Rumi database. 
Please read the documentation online on how to set up an MCP connection. Let me know when you're ready."
```

The agent will:
1. Ask for Rumi database credentials (host, port, database name, username, password)
2. Configure the MCP connection
3. Test by querying tables
4. Document the schema in docs/rumi-schema.md

## Quick Reference
- Rumi analysis: see skills/rumi-analysis.md
- Post generation: see skills/post-generation.md
- Slack workflow: see skills/slack-integration.md
- Performance tracking: see skills/performance-tracking.md
- Team info: see docs/team-roster.md
- Trending topics: see docs/trending-topics.md
- Post examples: see docs/post-templates.md
