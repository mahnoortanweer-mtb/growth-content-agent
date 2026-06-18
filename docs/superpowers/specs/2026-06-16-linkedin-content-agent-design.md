# LinkedIn Content Agent — Design Specification

**Project:** MTB's Growth Team LinkedIn Content Automation  
**Date:** 2026-06-16  
**Owner:** Mahnoor Tanweer  
**Status:** Approved for Implementation

---

## 1. Purpose & Success Criteria

### Purpose
Build an AI agent that automates LinkedIn content creation for the growth team. The agent researches team wins, analyzes product data from Rumi, generates authentic posts tailored to each team member's expertise, and coordinates review/approval via Slack before team members post manually on their own LinkedIn accounts.

### Success Criteria
- **Content Quality:** Posts sound like they're written by the team member, not generic AI
- **Data-Backed:** Every post references substantial data from Rumi or dashboards
- **Relevance:** Posts cover trending topics + team wins, BTS, product updates, features
- **Engagement:** High LinkedIn engagement (likes, comments, shares)
- **Team Satisfaction:** Growth team finds posts valuable and time-saving
- **Consistency:** Content velocity improves (daily posts instead of ad-hoc)
- **Insights:** Posts surface meaningful data patterns

---

## 2. System Architecture

### High-Level Flow

```
Agent Daily Loop:
  1. Retrieve data from Rumi database (product metrics, wins, features)
  2. Identify team member assigned to today's post (rotation)
  3. Generate draft post tailored to their expertise
  4. Send to Slack, tag Mahnoor + team member
  5. Team member reviews, tweaks, posts on LinkedIn
  6. Agent tracks post performance over time
```

### Core Components

#### 2.1 Agent Entry Point (CLAUDE.md)
- Project overview
- Team roster with expertise areas (Product Growth Managers, Partnership Manager, Marketing Manager)
- Current focus and workflow
- Pointers to skills and memory files
- Slack & Rumi connection details
- Key rules for content generation (authentic voice, data-backed, trending + wins)

#### 2.2 Data Layer: Rumi Database Connection
- Connect via MCP (Model Context Protocol) to Rumi database
- Skills define:
  - How to query product metrics (user growth, engagement, adoption, retention)
  - How to find recent wins and features shipped
  - How to extract meaningful numbers for posts
  - Database schema overview

#### 2.3 Content Generation Engine
- Skills define templates and prompts for:
  - Product-focused posts (for growth product managers)
  - Partnership-focused posts (for partnership manager)
  - Marketing-focused posts (for marketing manager)
  - Trending topic integration (what's hot in growth/SaaS right now)
- Posts should:
  - Sound like team member's voice (not corporate AI)
  - Lead with data/numbers
  - Include takeaway or insight
  - Be LinkedIn-native (length, tone, hashtags)

#### 2.4 Slack Integration
- Skills define:
  - How to send formatted message to Slack with draft post
  - How to tag Mahnoor (owner/approver) and assigned team member
  - How to include context (which data was used, why this topic was chosen)
  - How to prompt for approval/revision
- Agent monitors Slack responses (threaded approval workflow)

#### 2.5 Performance Tracking
- Skills define:
  - What metrics to track (likes, comments, shares, reach if available)
  - How to store post metadata (date, author, topic, data points used)
  - How to analyze what types of posts perform best
  - Memory file grows with post history and performance data

---

## 3. Data Flow & Workflow

### Daily Automated Post (Scheduled)

```
Time: [User-configured, e.g., 9 AM daily]
    ↓
Determine Team Member: Rotate through roster (day 1 = person A, day 2 = person B, etc.)
    ↓
Query Rumi: Fetch recent metrics, wins, feature launches
    ↓
Analyze Trends: What's trending in growth/SaaS this week?
    ↓
Generate Draft: Craft post tailored to team member's expertise
    ↓
Send to Slack: Message to #growth channel, tag Mahnoor + team member
    ↓
Wait for Approval: Team member reviews, optionally tweaks
    ↓
Team Posts: Team member posts on their own LinkedIn (agent does NOT post)
    ↓
Track Performance: Agent records post metadata, later collects engagement stats
```

### On-Demand Post (Manual Trigger)

```
User asks: "Generate a post about [topic]"
    ↓
Agent clarifies: "For which team member? Or should I pick based on expertise?"
    ↓
Generate: Same process as daily, but topic-specific
    ↓
Send to Slack: Same notification flow
    ↓
Rest of workflow continues
```

---

## 4. Team Member Expertise Mapping

| Team Member Role | Expertise Focus | Post Themes |
|---|---|---|
| Growth Product Manager (2 people) | Product features, adoption, engagement metrics | Feature launches, user adoption rates, engagement trends |
| Growth Partnership Manager | Partnerships, integrations, expansion | Partnership wins, integration announcements, ecosystem growth |
| Growth Marketing Manager | Marketing campaigns, brand, audience | Campaign results, audience insights, brand announcements |

**Routing Logic:** Agent generates posts aligned with each person's assigned day and expertise area. When generating on-demand, agent asks which team member it should tailor to.

---

## 5. File & Folder Structure

```
linkedin-content-agent/
├── CLAUDE.md                          # Agent entry point (< 100 lines)
├── memory.md                          # Learnings, post history, performance data
├── skills/
│   ├── rumi-analysis.md              # Querying Rumi database
│   ├── post-generation.md            # Content templates and prompts
│   ├── slack-integration.md          # Slack messaging and approval workflow
│   └── performance-tracking.md       # Analytics and metrics tracking
├── docs/
│   ├── team-roster.md                # Team members and expertise areas
│   ├── trending-topics.md            # Current industry trends (manually updated)
│   ├── rumi-schema.md                # Rumi database structure (auto-generated on first run)
│   └── post-templates.md             # Example posts for each expertise area
├── output/
│   └── posts/                        # Generated post drafts (dated files)
└── superpowers/
    └── specs/
        └── 2026-06-16-linkedin-content-agent-design.md (this file)
```

---

## 6. Memory System

### CLAUDE.md (Agent Entry Point, <100 lines)
```markdown
# Project: LinkedIn Content Agent

Automate daily LinkedIn posts for the growth team. Agent researches Rumi data, 
generates content, coordinates via Slack.

## Current Focus
- Building MVP: Rumi connection, daily post generation, Slack approval workflow
- External dashboards: Coming later

## Team Roster
- Mahnoor Tanweer (Owner/Approver)
- Growth Product Manager 1 (Expertise: product)
- Growth Product Manager 2 (Expertise: product)
- Growth Partnership Manager (Expertise: partnerships)
- Growth Marketing Manager (Expertise: marketing)

## Key Rules
1. Posts must sound like they're written by the team member, not generic AI
2. Every post must reference substantial data from Rumi
3. Combine trending topics + team wins/features/BTS
4. Always tag Mahnoor + assigned team member in Slack
5. Team members post on LinkedIn manually (agent doesn't post)
6. Track post performance for future optimization

## Quick Reference
- Rumi analysis: see skills/rumi-analysis.md
- Post generation: see skills/post-generation.md
- Slack workflow: see skills/slack-integration.md
- Team info: see docs/team-roster.md
```

### memory.md (Grows Over Time)
Tracks:
- Post history (date, author, topic, data used, performance)
- What types of posts get best engagement
- Team member feedback on drafts
- Trending topics that resonated
- Rumi data quirks or updates
- Lessons learned

Example entries:
```markdown
## Post Performance Patterns
- Product launch posts get 15-20% higher engagement
- Partnership announcements average 8-12 comments
- Data-heavy posts (with numbers) outperform narrative-only posts

## Team Feedback
- Mahnoor prefers posts that lead with numbers, then narrative
- Partnership manager wants more specific deal metrics
- Product managers like before/after comparisons

## Rumi Data Notes
- Weekly retention updated Tuesday mornings
- Feature adoption data lags by 1-2 days
```

### Skills (Procedural Knowledge)
Each skill is a markdown file with step-by-step instructions for specific tasks. See Section 7.

---

## 7. Core Skills (MVP)

### 7.1 skill/rumi-analysis.md
**Purpose:** Query Rumi database for post-worthy data

**Prerequisites:**
- MCP connection to Rumi (configured in environment)
- Understand Rumi schema: users, sessions, features, retention, engagement

**Instructions:**
1. Connect to Rumi database via MCP
2. Query for recent wins:
   - New features shipped (last 7 days)
   - User growth metrics (week-over-week)
   - Engagement spikes or retention improvements
3. Extract numbers that tell a story (not raw data dumps)
4. Identify patterns (which features drive engagement?)
5. Return summary with: metric, value, date, significance

**Example:**
- Input: "What should we post about this week?"
- Output: "3 findings: (1) DAU up 18% this week; (2) Lesson Plans feature has 45% adoption; (3) New coach integration launched yesterday"

---

### 7.2 skills/post-generation.md
**Purpose:** Generate authentic, data-backed LinkedIn posts

**Prerequisites:**
- Understand team member's voice and expertise
- Data from Rumi analysis
- Awareness of current trends in growth/SaaS

**Instructions:**
1. Identify team member and their expertise
2. Gather data points (from rumi-analysis.md results)
3. Research: What's trending this week in growth/SaaS? (Check industry blogs, LinkedIn trends)
4. Draft post:
   - Hook: Start with insight or question
   - Data: Lead with numbers
   - Context: Why does this matter?
   - Call-to-action: Question or invitation to discuss
5. Tone: Authentic (sounds like the team member, not corporate AI)
6. Length: LinkedIn-native (100-300 words typically)
7. Format: Breaks for readability, emojis sparingly, 1-2 hashtags max

**Template (Product-Focused):**
```
[Hook about user engagement or feature adoption]

Here's what we shipped: [feature], and here's what happened:
📈 [Metric 1]: [Number]%
📈 [Metric 2]: [Number] users
📈 [Metric 3]: [Insight]

[Why this matters for growth/education/SaaS]

What are you seeing in your space? [Question for engagement]

#Growth #[Topic]
```

---

### 7.3 skills/slack-integration.md
**Purpose:** Send draft posts to Slack and manage approval workflow

**Prerequisites:**
- Slack workspace access (via MCP or webhook)
- Know Slack channel (e.g., #growth)
- Know team member Slack IDs

**Instructions:**
1. Format draft post for Slack (code block or formatted text)
2. Compose message:
   - "Draft post for [Team Member Name] — please review & tweak"
   - Tag @Mahnoor (owner) and @[Team Member] (author)
   - Include context: "Based on [X metric] from Rumi data"
3. Send to #growth (or designated channel)
4. Wait for approval in thread:
   - ✅ "Looks good, posting!" → Go ahead
   - 💬 "Let me tweak..." → Wait for revised version
   - ❌ "Not quite, try..." → Regenerate based on feedback

**Notes:**
- Keep approval workflow in a Slack thread (keeps main channel clean)
- If team member makes edits, document in memory.md for future reference
- Agent does NOT post to LinkedIn (team member handles this)

---

### 7.4 skills/performance-tracking.md
**Purpose:** Track post performance and identify patterns

**Prerequisites:**
- Record of posts sent (titles, dates, authors, topics)
- LinkedIn engagement data (collected manually or via LinkedIn API if available later)

**Instructions:**
1. Log post metadata:
   - Date posted
   - Team member author
   - Topic/theme
   - Key data points used
   - Expertise area (product/partnership/marketing)
2. After 3-7 days, collect engagement:
   - Likes, comments, shares (manually from LinkedIn or via API)
   - Reach (if available)
3. Analyze patterns:
   - Which expertise area gets most engagement?
   - Which data types (growth metrics vs. feature launches)?
   - Optimal post length/format?
4. Update memory.md with learnings

**Example:**
```markdown
## Post #42 (2026-06-15)
- Author: Growth Product Manager 1
- Topic: Feature adoption (Lesson Plans)
- Data: 45% adoption, 3-day TTU
- Engagement: 24 likes, 6 comments, 3 shares
- Performance: Above average for product posts
```

---

## 8. External Integrations

### 8.1 Rumi Database (MVP)
- **Connection:** MCP server
- **What's accessible:** Product metrics, user data, feature adoption, engagement
- **Query frequency:** Daily for automated posts, on-demand for manual requests
- **Schema:** Will be documented in docs/rumi-schema.md after first connection

### 8.2 Slack (MVP)
- **Connection:** MCP server (or Slack webhook if webhook preferred)
- **What's used:** Sending draft messages, tagging users, receiving approval feedback
- **Channels:** #growth (or designated channel for this workflow)
- **Team Members:** Mahnoor + growth team (2 product managers, 1 partnership manager, 1 marketing manager)

### 8.3 External Dashboards (Future)
- **Status:** Not included in MVP
- **Plan:** Once dashboards are identified, create MCP connection and skill to query
- **Metrics:** Usage, engagement, conversion rates, etc.
- **Timeline:** After MVP launch

---

## 9. Implementation Phases

### Phase 1: MVP (Today)
- [x] Design approved
- [ ] Set up project structure and CLAUDE.md
- [ ] Connect Rumi database via MCP
- [ ] Write rumi-analysis.md skill
- [ ] Write post-generation.md skill
- [ ] Write slack-integration.md skill
- [ ] Write performance-tracking.md skill
- [ ] Create team-roster.md and initial memory.md
- [ ] Test: Generate one post, send to Slack, get approval
- [ ] Document lessons in memory.md

### Phase 2: Automation (Day 2+)
- Schedule daily post generation at set time
- Rotate through team member roster
- Test full workflow (data → generate → Slack → approval)

### Phase 3: Analytics (Week 2)
- Collect engagement data for posted content
- Analyze patterns in memory.md
- Refine templates based on what's working

### Phase 4: Scale (Later)
- Add external dashboards
- Add trend detection
- Expand team member roster if needed
- Consider auto-posting (if team agrees)

---

## 10. Error Handling & Safety

### Error Cases & Mitigation

| Error | Mitigation |
|---|---|
| Rumi database unavailable | Fallback: Use cached data from last successful query; alert Mahnoor |
| Can't tag team member in Slack | Log error, send to #general or DM Mahnoor |
| Post generation is low quality | Regenerate with refined prompt; manual review before sending |
| Team member doesn't respond to approval | Slack reminder after 4 hours; escalate to Mahnoor after 24 hours |
| LinkedIn engagement data can't be fetched | Manual entry; note in memory for future API setup |

### Guardrails
- **Agent never posts to LinkedIn** — Team members post manually
- **Mahnoor always tagged** — Maintains oversight
- **Data is always referenced** — No posts without Rumi data backing
- **Authentication:** Rumi MCP uses read-only credentials (no write access)

---

## 11. Testing Strategy

### MVP Testing Checklist
- [ ] Rumi query returns data successfully
- [ ] Post generation produces authentic-sounding content
- [ ] Slack message formats correctly and tags are correct
- [ ] Team member receives notification and can respond
- [ ] On-demand post generation works
- [ ] Performance tracking records posts correctly
- [ ] Memory files update after each cycle

### Success Test
- Generate 3 posts in the next 3 days
- Team members approve and post on LinkedIn
- Collect engagement data after 3-7 days
- Analyze in memory.md

---

## 12. Post-MVP Roadmap

### Week 1 After MVP
- [ ] Identify external dashboards, document in docs/
- [ ] Create MCP connection for dashboards
- [ ] Add dashboard-query skill

### Week 2+
- [ ] Set up LinkedIn trend monitoring skill
- [ ] Refine templates based on engagement data
- [ ] Expand post types (case studies, team spotlights, data deep-dives)
- [ ] Consider: Auto-scheduling (agent picks best time to notify team)

### Future Considerations
- LinkedIn API integration for real-time engagement tracking
- Trend detection: automated monitoring of SaaS/growth topics
- A/B testing: generate 2 variants of a post, measure which performs better
- Team member feedback loop: store feedback in memory, improve over time

---

## 13. Success Metrics (Tracked in memory.md)

- **Consistency:** 1 post generated and approved per day
- **Quality:** Posts sound authentic, team feedback is positive
- **Engagement:** Average likes/comments/shares per post (baseline after 2 weeks)
- **Data Usage:** Every post references 2-3 data points from Rumi
- **Team Satisfaction:** Team members find posts valuable and reusable
- **Time Savings:** Estimated hours saved by team per month

---

## Approval

- [x] Design reviewed and approved by Mahnoor Tanweer
- [ ] Spec review passed
- [ ] Ready for implementation planning

---

**Next Step:** Invoke writing-plans to create detailed implementation plan.
