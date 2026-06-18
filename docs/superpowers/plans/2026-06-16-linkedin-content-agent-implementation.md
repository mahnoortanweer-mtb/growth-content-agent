# LinkedIn Content Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a functioning LinkedIn content agent that generates daily posts tailored to team member expertise, coordinates via Slack, and tracks performance — MVP complete by end of day.

**Architecture:** Single agent with modular skills. Agent reads from Rumi database, generates posts via templates, notifies via Slack, tracks performance in memory files. Skills are standalone markdown files that define how to perform specific tasks. CLAUDE.md routes to skills and defines team structure.

**Tech Stack:** Claude Code (agent framework), MCP (Rumi database connection), Slack API/MCP (notifications), Markdown (skills and memory), Python (if needed for complex queries).

---

## File Structure

```
d:\MTB'S AGENT\
├── CLAUDE.md                              # Agent entry point (routing, team roster, rules)
├── memory.md                              # Learnings, post history, performance (grows over time)
├── docs/
│   ├── superpowers/
│   │   ├── specs/
│   │   │   └── 2026-06-16-linkedin-content-agent-design.md  (already created)
│   │   └── plans/
│   │       └── 2026-06-16-linkedin-content-agent-implementation.md  (this file)
│   ├── team-roster.md                    # Team members, expertise areas, Slack IDs
│   ├── trending-topics.md                # Current growth/SaaS trends (manually updated)
│   ├── post-templates.md                 # Example posts for each expertise area
│   └── rumi-schema.md                    # Rumi database structure (auto-generated on first run)
├── skills/
│   ├── rumi-analysis.md                  # Skill: Query Rumi for post-worthy data
│   ├── post-generation.md                # Skill: Generate authentic LinkedIn posts
│   ├── slack-integration.md              # Skill: Send to Slack, manage approval workflow
│   └── performance-tracking.md           # Skill: Track post performance metrics
└── output/
    └── posts/                            # Generated post drafts (dated files)
```

---

## Implementation Tasks

### Task 1: Create Project Structure and CLAUDE.md

**Files:**
- Create: `d:\MTB'S AGENT\CLAUDE.md`
- Create: `d:\MTB'S AGENT\memory.md`
- Create: `d:\MTB'S AGENT\docs\` (directory)
- Create: `d:\MTB'S AGENT\skills\` (directory)
- Create: `d:\MTB'S AGENT\output\posts\` (directory)

**Context:** CLAUDE.md is the agent's entry point. It should be under 100 lines and route to other files. This is what the agent reads first every session.

- [ ] **Step 1: Create CLAUDE.md**

File: `d:\MTB'S AGENT\CLAUDE.md`

```markdown
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
- Status: [TO BE FILLED AFTER MCP SETUP]
- Access: Read-only
- Key metrics: User growth, engagement, retention, feature adoption

## Quick Reference
- Rumi analysis: see skills/rumi-analysis.md
- Post generation: see skills/post-generation.md
- Slack workflow: see skills/slack-integration.md
- Performance tracking: see skills/performance-tracking.md
- Team info: see docs/team-roster.md
- Trending topics: see docs/trending-topics.md
- Post examples: see docs/post-templates.md

## Preferences
- Post length: 100-300 words (LinkedIn native)
- Tone: Professional but conversational, authentic to team member voice
- Data format: Lead with numbers, then narrative
- Visuals: Mention data points clearly, format for readability
```

- [ ] **Step 2: Create memory.md**

File: `d:\MTB'S AGENT\memory.md`

```markdown
# Memory: LinkedIn Content Agent

## Post History
(This file grows as posts are generated. Track date, author, topic, data used, performance)

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
```

- [ ] **Step 3: Create directories**

Run these commands:
```powershell
New-Item -ItemType Directory -Path "d:\MTB'S AGENT\docs" -Force
New-Item -ItemType Directory -Path "d:\MTB'S AGENT\skills" -Force
New-Item -ItemType Directory -Path "d:\MTB'S AGENT\output\posts" -Force
```

Expected: Directories created without error.

- [ ] **Step 4: Commit**

```bash
git init "d:\MTB'S AGENT"
git config user.email "mahnoor.tanweer@niete.edu.pk"
git config user.name "Mahnoor Tanweer"
cd "d:\MTB'S AGENT"
git add CLAUDE.md memory.md
git commit -m "chore: initialize project structure and CLAUDE.md

- Agent entry point with team roster and key rules
- Empty memory.md for tracking posts and learnings
- Directories for skills, docs, and output"
```

Expected: Commit succeeds.

---

### Task 2: Create Team Roster and Supporting Documentation

**Files:**
- Create: `d:\MTB'S AGENT\docs\team-roster.md`
- Create: `d:\MTB'S AGENT\docs\trending-topics.md`
- Create: `d:\MTB'S AGENT\docs\post-templates.md`

- [ ] **Step 1: Create team-roster.md**

File: `d:\MTB'S AGENT\docs\team-roster.md`

```markdown
# Growth Team Roster

## Team Members

### Mahnoor Tanweer
- **Role:** Growth Lead / Owner
- **Responsibility:** Reviews and approves all posts
- **Slack ID:** @mahnoor.tanweer (or @mahnoor — confirm in Slack)
- **Focus:** Strategic direction

### Growth Product Manager 1
- **Name:** [TO BE FILLED]
- **Slack ID:** [TO BE FILLED]
- **Expertise:** Product adoption, feature launches, user onboarding
- **Post Focus:** New features, adoption rates, user journey improvements
- **Assigned Days:** Day 1, 5, 9, ... (every 4 days)

### Growth Product Manager 2
- **Name:** [TO BE FILLED]
- **Slack ID:** [TO BE FILLED]
- **Expertise:** Product metrics, engagement, retention analysis
- **Post Focus:** Growth metrics, engagement trends, retention insights
- **Assigned Days:** Day 2, 6, 10, ... (every 4 days)

### Growth Partnership Manager
- **Name:** [TO BE FILLED]
- **Slack ID:** [TO BE FILLED]
- **Expertise:** Integrations, partnerships, ecosystem growth
- **Post Focus:** Partnership announcements, integration wins, ecosystem updates
- **Assigned Days:** Day 3, 7, 11, ... (every 4 days)

### Growth Marketing Manager
- **Name:** [TO BE FILLED]
- **Slack ID:** [TO BE FILLED]
- **Expertise:** Campaigns, brand, audience growth, messaging
- **Post Focus:** Campaign results, audience insights, brand announcements
- **Assigned Days:** Day 4, 8, 12, ... (every 4 days)

## Assignment Logic
- Posts rotate through team members in order
- Each team member is assigned one day every 4 days
- Posts are tailored to their expertise
- Mahnoor always tagged for review

## Slack Configuration
- **Primary channel:** #growth (or TBD)
- **Approval workflow:** Post draft sent as thread reply, reactions used for approval
  - ✅ = Approved, go ahead and post
  - 💬 = Want to tweak, will edit in thread
  - ❌ = Needs rework, feedback in thread
```

- [ ] **Step 2: Create trending-topics.md**

File: `d:\MTB'S AGENT\docs\trending-topics.md`

```markdown
# Trending Topics & Themes (Updated: 2026-06-16)

This file is updated weekly to track what's trending in growth, SaaS, and education tech.
Use these to inform post topics and find angles on your wins.

## Current Trends (Week of June 16-22, 2026)

### AI in Education
- AI-powered personalized learning gaining traction
- Teacher sentiment: cautious but curious
- Opportunity: Position Rumi as tool that supports, not replaces, teachers

### EdTech M&A
- Consolidation continues in India's edtech space
- Focus: Unit economics and sustainable growth
- Angle: Sustainable growth through retention (vs. CAC-heavy approaches)

### Product-Led Growth
- Moving away from pure CAC/LTV metrics
- Emphasis on: feature adoption, time-to-value, user engagement
- Angle: Rumi's adoption metrics, engagement spikes

### Teacher Retention & Burnout
- Teacher burnout at all-time high globally
- EdTech positioning: reduce administrative burden, improve outcomes
- Angle: How Rumi reduces teacher workload

### Growth Metrics Conversations
- Shift from vanity metrics (users) to meaningful metrics (engagement, retention)
- Teams talking openly about: churn analysis, cohort retention, feature impact
- Angle: Your retention data, feature adoption insights

## Topic Ideas for Posts
- **Feature focus:** Lesson Plans adoption spike, Coach feedback integration launch
- **Data-driven:** Weekly retention curves, feature adoption by segment
- **Team wins:** Team growing, features shipping, partnerships landing
- **BTS:** How you approach a problem, decision-making, failures + learnings
- **Industry commentary:** Commentary on edtech trends, responding to industry news

## Hashtags to Use
- #EdTech, #Growth, #Product, #SaaS, #TeacherTech, #India, #Learning
- (Keep to 1-2 per post)

## Seasonal Themes
- June-July: Mid-year reviews, H2 planning
- Aug-Sept: Back-to-school, teacher hiring
- Oct-Nov: Holiday campaigns, year-end pushes
- Dec-Jan: New Year, resolutions, data retrospectives
```

- [ ] **Step 3: Create post-templates.md**

File: `d:\MTB'S AGENT\docs\post-templates.md`

```markdown
# LinkedIn Post Templates

Use these as starting points. Customize for each team member and topic.

## Template 1: Feature Launch / Product Win

```
[Hook: Start with impact or insight]

We just shipped [Feature Name], and early numbers are telling:
📈 [Metric 1]: [Number]% improvement
📈 [Metric 2]: [Number] users impacted
📈 [Metric 3]: [Insight or surprise]

[2-3 sentences on why this matters for your audience]

What's one feature you'd love to see shipped next?

#EdTech #Growth #Product
```

**Example:**
```
Teachers asked for it. We listened.

Lesson Plans is now live in Rumi, and adoption is already outpacing our projections:
📈 45% of active users exploring the feature in first week
📈 3-day time-to-first-plan (vs. 10-day average for other features)
📈 Teachers spending 2x more time in Rumi on planning days

Why it matters: Lesson planning is where teachers spend the most time. Now they can draft, iterate, and share plans directly in Rumi. Fewer tab switches, less friction.

What's the feature your teachers have been asking for?

#EdTech #Growth #Teachers
```

## Template 2: Data Insight / Retention Analysis

```
We looked at [X time period] of data across [Y users/schools].

What we found surprised us:

[Insight 1]: [Data]
[Insight 2]: [Data]
[Insight 3]: [Data or pattern]

[2-3 sentences on what this means for teachers, schools, or growth]

[Question or invitation to discuss]

#Growth #Data #EdTech
```

**Example:**
```
We analyzed 4 weeks of Rumi engagement data across 50 schools.

What we found shifted how we think about retention:

Teachers who use Coaching feedback show 3x higher retention through week 4 — even with lower initial adoption.

Schools with +10% week-over-week session growth showed 60% churn reduction (no other changes in their setup).

The common thread? Time-to-value. Features that show impact in the first 2 weeks drive long-term stickiness.

What's surprising you in your data this month?

#Growth #EdTech #DataDriven
```

## Template 3: Partnership / Ecosystem Win

```
Excited to announce: we're now integrated with [Partner Name].

What this means for our teachers:
• [Benefit 1]
• [Benefit 2]
• [Benefit 3]

[2-3 sentences on ecosystem value and what comes next]

[Call to action or question]

#EdTech #Growth #Partnerships
```

**Example:**
```
Excited to announce: Rumi now integrates with Google Classroom.

No more context switching. Teachers can:
• Assign Rumi lessons directly from Google Classroom
• Auto-sync attendance and grades back to Classroom
• See student progress in both platforms without logging out

We built this because teachers live in Classroom. Why build them another place to go? This is the first of many ecosystem integrations we're shipping.

Who else should we integrate with? Drop a comment.

#EdTech #Growth #Teachers
```

## Template 4: Team Milestone / Behind-the-Scenes

```
[Team milestone/win announcement]

[2-3 sentences on what it took, the journey, key learnings]

[Personal or team insight]

[Question or invitation to discuss your own journey]

#Growth #Startups #EdTech
```

**Example:**
```
We just shipped 3 major features in 8 weeks.

Sounds fast (and it was), but it required ruthless prioritization. We said no to 15 ideas to say yes to 3. We spent 60% of time on research and design, 40% on coding. We shipped, measured, then doubled down on what worked.

Biggest learning: shipping something that people use is 10x harder than shipping something that works.

What's your biggest bottleneck when shipping fast?

#Growth #Product #Startups
```

## Template 5: Commentary / Industry Insight

```
[Hot take or observation on industry trend]

[Data or evidence to back it up]

[Why it matters for your audience]

[Question or invitation to debate]

#EdTech #Growth #[Topic]
```

**Example:**
```
India's edtech companies have stopped talking about CAC.

Not because it doesn't matter — it does. They're talking about it privately and obsessing over retention instead.

Why the shift? Unit economics changed. It's no longer about who can acquire the most users. It's about who can engage them and keep them coming back.

At Rumi, 60% of our growth this quarter came from retention and expansion in existing schools — not new user acquisition. That's a different playbook entirely.

What metric matters most to your business right now?

#EdTech #Growth #UnitEconomics
```

---

## Writing Tips
1. **Lead with data:** Numbers first, narrative second
2. **Be specific:** Avoid vague claims; back everything up
3. **Show, don't tell:** Use examples and stories
4. **Be authentic:** Write like the team member (not corporate AI)
5. **Invite engagement:** End with a question or invitation to discuss
6. **Keep it short:** LinkedIn thrives on scannable content (100-300 words)
7. **Use line breaks:** White space matters; break up text blocks

---
```

- [ ] **Step 4: Commit**

```bash
cd "d:\MTB'S AGENT"
git add docs/team-roster.md docs/trending-topics.md docs/post-templates.md
git commit -m "docs: add team roster, trending topics, and post templates

- Team member roster with expertise areas and Slack IDs (to be filled)
- Trending topics for growth/SaaS/EdTech (updated weekly)
- Post templates for common content types (feature, data, partnership, team, commentary)"
```

Expected: Commit succeeds.

---

### Task 3: Connect to Rumi Database via MCP

**Files:**
- Modify: `d:\MTB'S AGENT\CLAUDE.md` (update Rumi connection status)
- Create: `d:\MTB'S AGENT\docs\rumi-schema.md` (auto-generated after connection test)

**Context:** This task requires you to set up an MCP connection to the Rumi database. The agent will use this to query product metrics, feature adoption, retention data, etc.

- [ ] **Step 1: Prepare Rumi credentials**

You'll need:
- Database host
- Database port
- Database name
- Username (read-only)
- Password

Get these from a secure location (Notion, password manager, etc.). Do NOT commit credentials to git.

- [ ] **Step 2: Ask the agent to set up MCP**

In Claude Code, type this prompt:

```
"Can you please set up an MCP for me? We need to connect to the Rumi database for data analysis on our product. Please read documentation online on how to set up an MCP connection to a database and let me know when you're ready. I'll provide credentials when you ask."
```

Expected: Agent asks for credentials and database details.

- [ ] **Step 3: Provide credentials to agent**

When the agent asks, provide:
- Host: [your Rumi host]
- Port: [your Rumi port]
- Database name: [your Rumi database name]
- Username: [read-only user]
- Password: [password]

Expected: Agent configures MCP and creates configuration file.

- [ ] **Step 4: Test the connection**

Ask the agent:

```
"Can you list the tables in the Rumi database? I want to confirm the connection is working."
```

Expected: Agent returns list of tables (e.g., users, sessions, features, events, etc.).

- [ ] **Step 5: Ask agent to document schema**

Ask:

```
"Please document the Rumi database schema in docs/rumi-schema.md. Include:
- All table names
- Key columns in each table
- Relationships between tables
- Which tables have data we'll use for posts (e.g., user engagement, feature adoption, retention)
- Any notes on data freshness or update frequency"
```

Expected: Agent creates `docs/rumi-schema.md` with complete schema documentation.

- [ ] **Step 6: Update CLAUDE.md with connection status**

Modify: `d:\MTB'S AGENT\CLAUDE.md`

Find this line:
```
- Status: [TO BE FILLED AFTER MCP SETUP]
```

Replace with:
```
- Status: ✅ Connected via MCP
- Database: Rumi (read-only)
- Last verified: [today's date]
```

- [ ] **Step 7: Commit**

```bash
cd "d:\MTB'S AGENT"
git add CLAUDE.md docs/rumi-schema.md
git commit -m "feat: connect to Rumi database via MCP

- MCP configured for read-only access to Rumi database
- Schema documented in docs/rumi-schema.md
- Connection tested and verified"
```

Expected: Commit succeeds.

---

### Task 4: Create rumi-analysis.md Skill

**Files:**
- Create: `d:\MTB'S AGENT\skills\rumi-analysis.md`

**Context:** This skill teaches the agent how to query Rumi and extract post-worthy data: product metrics, recent wins, feature adoption, engagement spikes, etc.

- [ ] **Step 1: Write rumi-analysis.md**

File: `d:\MTB'S AGENT\skills\rumi-analysis.md`

```markdown
# Skill: Rumi Data Analysis

## Purpose
Extract post-worthy insights from Rumi database: product metrics, feature adoption, engagement spikes, and wins that tell a compelling story.

## Prerequisites
- MCP connection to Rumi database (configured and tested)
- Rumi schema understood (see docs/rumi-schema.md)
- Database is read-only (no write access)

## Instructions

### Step 1: Connect to Rumi
Use the MCP connection that's already configured. This gives you access to all Rumi tables.

### Step 2: Query for Recent Wins (Last 7 Days)
Look for:
- New features shipped (check feature_releases or similar table)
- User growth metrics (week-over-week comparison)
- Engagement spikes (feature usage, session counts)
- Retention improvements (cohort retention curves)

**Query template:**
```sql
-- Example: Get user growth this week vs. last week
SELECT 
  DATE_TRUNC('week', created_at) as week,
  COUNT(DISTINCT user_id) as new_users
FROM users
WHERE created_at >= NOW() - INTERVAL '14 days'
GROUP BY DATE_TRUNC('week', created_at)
ORDER BY week DESC;
```

### Step 3: Extract Meaningful Numbers
Don't return raw data. Extract insights:
- Not: "DAU = 1,234"
- Yes: "DAU is up 18% week-over-week, driven by Lesson Plans feature"

### Step 4: Identify the Story
For each metric, ask: **Why does this matter?**
- For engagement metrics: Which feature drives it? Is adoption growing?
- For user growth: Is it organic or from a specific school/cohort?
- For retention: Which cohort performs best? Why?

### Step 5: Return Summary
Format your findings as:

```
## This Week's Post Candidates

### Finding 1: [Headline]
- Metric: [X metric] = [Number]
- Context: [Why it matters]
- Data confidence: High/Medium
- Best presenter: [Which team member's expertise matches this?]

### Finding 2: [Headline]
- Metric: [X metric] = [Number]
- Context: [Why it matters]
- Data confidence: High/Medium
- Best presenter: [Which team member's expertise matches this?]

### Finding 3: [Headline]
- Metric: [X metric] = [Number]
- Context: [Why it matters]
- Data confidence: High/Medium
- Best presenter: [Which team member's expertise matches this?]
```

## Example Run

**Input:** "What should we post about this week?"

**Output:**
```
## This Week's Post Candidates

### Finding 1: Lesson Plans Feature Adoption Spike
- Metric: 45% of active users exploring Lesson Plans within first week
- Context: Highest adoption velocity for any feature launched. Teachers are already building on the feature.
- Data confidence: High
- Best presenter: Growth Product Manager 1 (feature launches)

### Finding 2: Week-over-Week Session Growth
- Metric: +22% session count vs. last week (15,000 → 18,300 sessions/day)
- Context: Sustained growth for 2+ weeks. Driven by retention improvements, not just new signups.
- Data confidence: High
- Best presenter: Growth Product Manager 2 (metrics & engagement)

### Finding 3: Partnership Integration Live
- Metric: Google Classroom integration now live; 5 schools have activated
- Context: First partnership integration shipped. Schools requesting more integrations.
- Data confidence: High
- Best presenter: Growth Partnership Manager (partnerships)
```

## Common Mistakes & How to Avoid

| Mistake | Avoidance |
|---------|-----------|
| Returning raw data (20 rows of numbers) | **Extract insights, not data.** Summarize to 2-3 key findings. |
| Missing context ("DAU up 15%") | **Always answer: Why did it change? What drove it?** |
| Hallucinating data | **Always check: Can I source this from a query? If not, don't claim it.** |
| Skipping recent wins | **Always look at: features shipped, partnerships announced, milestones hit** in last 7 days. |
| Low confidence claims | **Tag your confidence (High/Medium/Low).** Mahnoor will spot unsupported claims. |

## Notes
- **Data freshness:** Most metrics update daily. Some (cohort retention) lag by 1-2 days.
- **Always verify:** If a finding seems surprising, run the query twice to confirm.
- **Ask questions:** If a metric seems off, ask before including it in findings.
- **Update memory:** After each run, note which queries worked and which were slow (for future optimization).
```

- [ ] **Step 2: Commit**

```bash
cd "d:\MTB'S AGENT"
git add skills/rumi-analysis.md
git commit -m "skill: add rumi-analysis for extracting post-worthy insights

- Query for recent wins, feature launches, engagement spikes
- Extract meaningful numbers with context
- Map findings to team member expertise areas
- Includes query templates and example runs"
```

Expected: Commit succeeds.

---

### Task 5: Create post-generation.md Skill

**Files:**
- Create: `d:\MTB'S AGENT\skills\post-generation.md`

**Context:** This skill teaches the agent how to turn Rumi insights into authentic LinkedIn posts tailored to each team member's voice and expertise.

- [ ] **Step 1: Write post-generation.md**

File: `d:\MTB'S AGENT\skills\post-generation.md`

```markdown
# Skill: LinkedIn Post Generation

## Purpose
Transform Rumi insights into authentic LinkedIn posts that sound like they're written by the assigned team member, backed by data, and optimized for engagement.

## Prerequisites
- Rumi data insights (from rumi-analysis.md skill)
- Team member expertise and voice (from docs/team-roster.md)
- Trending topics context (from docs/trending-topics.md)
- Post templates as reference (from docs/post-templates.md)

## Instructions

### Step 1: Identify the Team Member & Their Voice
Who is this post for?
- **Growth Product Manager (adoption focus):** Excited about features, metrics-driven, user-centric
- **Growth Product Manager (metrics focus):** Data storyteller, retention obsessed, pragmatic
- **Growth Partnership Manager:** Ecosystem thinker, integration announcements, partnership wins
- **Growth Marketing Manager:** Audience insights, campaign results, brand voice

### Step 2: Understand the Data Story
Take the Rumi finding and ask:
- **What's surprising?** The finding should have a "so what?" answer.
- **Who cares?** Teachers? School admins? Other growth teams?
- **What's the insight?** Not just "user growth is up" but "user growth is up because Lesson Plans drove first-time adoption"

### Step 3: Outline the Post
Before writing, outline in 3-4 bullets:
1. Hook: What's the surprising or interesting angle?
2. Data: What numbers back this up?
3. Context: Why does this matter?
4. Engagement: What question or call-to-action closes this?

### Step 4: Write the Draft
Use these guidelines:
- **Tone:** Professional but conversational. Authentic to the team member. Not corporate.
- **Structure:** 
  - Hook (1-2 sentences that grab attention)
  - Data (2-3 key numbers, clearly formatted)
  - Context (2-3 sentences on why it matters)
  - CTA (question or invitation to engage)
- **Length:** 100-300 words (LinkedIn native)
- **Formatting:** Use line breaks, bullet points, emojis sparingly (max 2-3)
- **Hashtags:** 1-2 relevant hashtags max

### Step 5: Data Authenticity Check
Before finalizing:
- [ ] Every number is from the Rumi query (not hallucinated)
- [ ] Numbers are recent (last 7-30 days)
- [ ] Context explains the "why" behind the metric
- [ ] Post answers "why should someone care about this?"

### Step 6: Voice Check
Read the post as if you're the team member. Does it sound like them?
- For Product Managers: Is it technical enough? Focused on impact?
- For Partnership Manager: Does it celebrate the partnership value?
- For Marketing Manager: Does it speak to audience growth and reach?

### Example Run

**Input:** 
```
Data finding: Lesson Plans feature has 45% adoption rate in first week 
Team member: Growth Product Manager 1 (feature launches expertise)
Trending context: Teachers are burnt out on admin tasks
```

**Outline:**
1. Hook: Teachers asked, we shipped, they're using it
2. Data: 45% adoption, 3-day TTU, 2x more time in app
3. Context: Lesson planning is the most time-consuming teacher task
4. CTA: What feature would you ship next?

**Draft:**
```
Teachers asked for it. We listened.

Lesson Plans is now live in Rumi, and adoption is already outpacing our projections:
📈 45% of active users exploring the feature in first week
📈 3-day time-to-first-plan (vs. 10-day average for other features)
📈 Teachers spending 2x more time in Rumi on planning days

Why it matters: Lesson planning is where teachers spend the most time. Now they can draft, iterate, and share plans directly in Rumi. Fewer tab switches, less friction.

What feature would you want us to ship next?

#EdTech #Growth #Teachers
```

## Common Mistakes & How to Avoid

| Mistake | Avoidance |
|---------|-----------|
| Generic AI tone ("Exciting news!") | **Use specific language. Lead with data. Authentic beats polished.** |
| Numbers without context ("DAU +18%") | **Always explain the why. What drove the growth? Why does it matter?** |
| Too long (500+ words) | **Edit ruthlessly. LinkedIn rewards scanning. Keep it under 300 words.** |
| Missing the team member's voice | **Read the post as them. Does it sound like something they'd say?** |
| Hashtags everywhere | **1-2 max. More is spam. Less is better.** |
| No engagement hook | **Every post needs a question or invitation to comment. No monologues.** |

## Iterating on Drafts
After Mahnoor + team member review in Slack, expect feedback:
- "Can you add more context on why adoption is high?"
- "Let's lead with the partnership value, not feature count"
- "This feels too corporate, make it more conversational"

Use this feedback to improve future posts. Document what works in memory.md.

## Notes
- **Data freshness:** Don't use data older than 7 days (exceptions: retention curves which are 14-30 day views)
- **Trending angle:** Check docs/trending-topics.md to see if you can connect this finding to a current trend
- **Team member voice:** If unsure, ask: "Does this sound like [Person]?"
- **Update memory:** After each post is published, track engagement and document what worked
```

- [ ] **Step 2: Commit**

```bash
cd "d:\MTB'S AGENT"
git add skills/post-generation.md
git commit -m "skill: add post-generation for creating authentic LinkedIn posts

- Outline-first approach: hook → data → context → CTA
- Voice matching: generate posts that sound like the team member
- Data authenticity checks
- Includes example runs and common mistakes
- Templates reference for structure"
```

Expected: Commit succeeds.

---

### Task 6: Create slack-integration.md Skill

**Files:**
- Create: `d:\MTB'S AGENT\skills\slack-integration.md`

**Context:** This skill teaches the agent how to send draft posts to Slack, tag the right people (Mahnoor + team member), and manage the approval workflow.

- [ ] **Step 1: Write slack-integration.md**

File: `d:\MTB'S AGENT\skills\slack-integration.md`

```markdown
# Skill: Slack Integration & Approval Workflow

## Purpose
Send draft LinkedIn posts to Slack, tag Mahnoor + assigned team member, and manage the approval workflow (review, revise, approve).

## Prerequisites
- MCP connection to Slack (configured in environment)
- Team member Slack IDs (from docs/team-roster.md)
- Mahnoor's Slack ID
- Draft post is ready (from post-generation.md skill)
- Slack channel for posts (#growth or designated channel)

## Instructions

### Step 1: Prepare the Message
Before sending, have ready:
- Draft post text (from post-generation.md)
- Team member being tagged
- Data sources used (e.g., "Based on user adoption metrics from Rumi")
- Today's date

### Step 2: Format for Slack
Format the draft so it's readable in Slack:

```
🔗 **LinkedIn Post Draft**
Assigned to: [Team Member Name]
Date: [Today]
Based on: [Data source, e.g., "User adoption metrics from Rumi"]

---

[Full post text here]

---

👀 **Mahnoor:** Please review and comment
📝 **[Team Member]:** Please review, tweak if needed, and approve with ✅

Reactions:
✅ = Approved, I'll post this
💬 = Let me tweak it [then edit in thread]
❌ = Needs rework [provide feedback in thread]
```

### Step 3: Send to Slack
Send this message to #growth (or your designated channel):

Command:
```
@Mahnoor @[Team Member Name]

[Paste formatted message above]
```

Expected: Message appears in Slack with mentions notifying both Mahnoor and team member.

### Step 4: Wait for Approval
Monitor the Slack thread for reactions:

| Reaction | Action | Next Step |
|----------|--------|-----------|
| ✅ | Post approved | Confirm: "Looks good! Going live — please post on your LinkedIn." |
| 💬 | Team member will tweak | Wait for edited version in thread, review again |
| ❌ | Needs rework | Read feedback in thread, regenerate post, send new draft |

### Step 5: Confirm and Hand Off
Once approved (✅ reaction):
- Reply in thread: "Approved! Please post this on your LinkedIn and reply here once you do."
- Team member posts on their LinkedIn
- They reply in thread with the LinkedIn post URL

### Step 6: Log in Memory
Once posted, update memory.md with:
```markdown
## Post #[Number] ([Date])
- Author: [Team Member]
- Topic: [Topic]
- Data used: [What metrics/findings]
- Posted URL: [LinkedIn URL from team member]
- Date posted: [Today]
- Status: Awaiting engagement data (check in 3-7 days)
```

## Example Conversation Flow

**Agent sends to Slack:**
```
🔗 **LinkedIn Post Draft**
Assigned to: Growth Product Manager 1
Date: 2026-06-16
Based on: Feature adoption metrics from Rumi

---

Teachers asked for it. We listened.

Lesson Plans is now live in Rumi, and adoption is already outpacing our projections:
📈 45% of active users exploring the feature in first week
📈 3-day time-to-first-plan (vs. 10-day average for other features)
📈 Teachers spending 2x more time in Rumi on planning days

Why it matters: Lesson planning is where teachers spend the most time. Now they can draft, iterate, and share plans directly in Rumi. Fewer tab switches, less friction.

What feature would you want us to ship next?

#EdTech #Growth #Teachers

---

👀 **Mahnoor:** Please review and comment
📝 **[PM 1]:** Please review, tweak if needed, and approve with ✅
```

**Mahnoor reacts:** ✅  
**PM 1 reacts:** 💬 and replies: "Let me tweak the last paragraph. I'll edit in this thread."  
**PM 1 replies in thread:** "Here's the revised version: [edited text]"  
**Agent reviews and asks:** "Does this updated version look good?"  
**PM 1 reacts:** ✅  
**Agent replies:** "Approved! Please post this on your LinkedIn and reply here with the URL."  
**PM 1 posts on LinkedIn and replies:** "Live! https://www.linkedin.com/posts/..."  
**Agent logs in memory.md:** "[Post metadata with engagement tracking date]"

## Common Mistakes & How to Avoid

| Mistake | Avoidance |
|---------|-----------|
| Tagging wrong person | **Always verify: Check docs/team-roster.md for correct Slack IDs.** |
| Forgetting to tag Mahnoor | **Mahnoor always tagged.** Rule: Every post gets Mahnoor's review. |
| Post is too long for Slack | **Format with line breaks and dashes (---) for readability.** |
| No clear data source | **Always include: "Based on [X metric] from Rumi"** |
| Disappearing approval (no follow-up) | **Set reminder: If no reaction in 4 hours, ping in thread.** |
| Multiple tweaks, no clear final version | **After each revision, ask: "Does this version look good?" Lock the version.** |

## Notes
- **Slack channel:** Confirm your channel is #growth. If different, update this skill.
- **Time zone:** Sends happen at [TBD — set time when automating]. Ensure team is online.
- **Threading:** Always keep approval in a thread (not main channel clutter).
- **Emoji reactions:** Using simple emoji reactions (✅💬❌) is faster than typing.
- **escalation:** If 24 hours pass with no response, escalate to Mahnoor via DM.
```

- [ ] **Step 2: Commit**

```bash
cd "d:\MTB'S AGENT"
git add skills/slack-integration.md
git commit -m "skill: add slack-integration for post approval workflow

- Format and send draft posts to Slack
- Tag Mahnoor (owner) and assigned team member
- Handle approval workflow (✅ approve, 💬 tweak, ❌ rework)
- Log approved posts to memory.md
- Includes example conversation flow and common mistakes"
```

Expected: Commit succeeds.

---

### Task 7: Create performance-tracking.md Skill

**Files:**
- Create: `d:\MTB'S AGENT\skills\performance-tracking.md`

**Context:** This skill teaches the agent how to track post performance (likes, comments, shares) and analyze patterns to improve future posts.

- [ ] **Step 1: Write performance-tracking.md**

File: `d:\MTB'S AGENT\skills\performance-tracking.md`

```markdown
# Skill: Performance Tracking & Analytics

## Purpose
Track LinkedIn post engagement metrics and identify patterns to optimize future posts. Used to update memory.md with learnings.

## Prerequisites
- Posted LinkedIn URLs (from Slack approval workflow)
- LinkedIn access to view post engagement
- memory.md file for logging (from main agent setup)

## Instructions

### Step 1: Collect Post Metadata
For each post published, record:
- Post date
- Author (team member)
- Topic/theme
- Key data points used
- URL on LinkedIn

Example:
```markdown
## Post #1 (2026-06-16)
- Author: Growth Product Manager 1
- Topic: Feature launch (Lesson Plans)
- Data: 45% adoption, 3-day TTU, 2x session time
- URL: https://www.linkedin.com/posts/...
- Posted date: 2026-06-16
- Engagement tracked: 2026-06-23 (7 days post)
```

### Step 2: Check Engagement After 3-7 Days
Visit each LinkedIn post and record:
- Likes: [Count]
- Comments: [Count]
- Shares: [Count]
- Reach: [If available, approximate from profile views]
- Top comments: [1-2 key observations from comments]

Example:
```markdown
## Post #1 — Engagement Data (Checked 2026-06-23)
- Likes: 42
- Comments: 8
- Shares: 3
- Reach: ~150 people (estimated from profile)
- Top comment: "@pm1 When will this be available to all teachers?"
- Performance level: Above average for product posts
```

### Step 3: Identify Patterns
After 3-5 posts, look for patterns:
- Which types of posts get most engagement? (Feature launches vs. data insights vs. partnerships)
- Which topics resonate? (Product focus vs. retention focus vs. marketing angle)
- Which team members' posts get more comments? (Correlation to engagement style)
- What time of day performs best? (Day of week, time posted)
- Does data-heavy always win? Or do narrative posts perform well?

Example pattern entry:
```markdown
## Pattern: Feature Launch Posts
- Average engagement: 35 likes, 6 comments, 2 shares
- Insight: Product launches are Rumi's strength. We ship with impact.
- Next time: Lead with adoption velocity (the surprise), not just announcement.
```

### Step 4: Update memory.md with Learnings
After analyzing patterns, update memory.md with:
- What's working (post types, topics, data angles)
- What's not working (generic posts, outdated data, weak angles)
- Suggestions for next posts
- Team member feedback

Example:
```markdown
## Performance Patterns (Week 1)
- Product launch posts: 35 avg likes, 6 comments (strong)
- Data insight posts: 18 avg likes, 2 comments (moderate)
- Partnership posts: 12 avg likes, 1 comment (weak - small audience)
- Pattern: Our audience cares most about product and engagement metrics

## Learnings
- Lead with surprising metrics, not just announcements
- Data credibility builds comments (people ask for details)
- Keep data fresh (week-old data gets 40% fewer comments than 1-2 day old)

## Next iteration
- Focus more on feature launch and adoption data posts
- For partnership posts, add customer impact angle ("Teachers can now do X")
```

### Step 5: Refine Post Templates
Use learnings to improve future posts. Example:
- If feature launch posts perform best: spend more time on feature stories
- If data posts underperform: add more context on "why this matters"
- If a team member's posts consistently outperform: document their style for reference

## Data Collection Template

Use this for each post:

```markdown
## Post #[Number] ([Date])
Author: [Team Member]
Topic: [Topic]
Data sources: [What metrics used]
Posted: [Date posted]
LinkedIn URL: [URL]

### Engagement (Checked [Date])
- Likes: [Number]
- Comments: [Number]
- Shares: [Number]
- Reach: [If available]

### Performance Assessment
- Level: [Below average / Average / Above average / Exceptional]
- Why: [Brief reason based on topic/data/team member/timing]

### Learnings
- What worked: [What drove engagement]
- What didn't: [What fell flat]
```

## Common Mistakes & How to Avoid

| Mistake | Avoidance |
|---------|-----------|
| Only tracking likes (vanity metric) | **Track all 3: likes + comments + shares. Comments = engagement quality.** |
| Checking engagement too early (same day) | **Wait 3-7 days.** Posts take time to circulate through LinkedIn algorithm. |
| No pattern analysis | **After 5 posts, analyze. What type of post wins? Document in memory.** |
| Forgetting context | **When logging engagement, log what made this post different (new data? hot topic?).** |
| No feedback loop | **Use learnings to refine next posts. Iteration matters.** |

## Notes
- **LinkedIn reach:** Usually estimated from profile views + network reach. Not always exact.
- **Time lag:** LinkedIn algorithm shows peak engagement 3-7 days post. Checking too early misses the full picture.
- **Seasonal variation:** Some topics perform better at certain times (back-to-school in Aug/Sept, Q4 planning in Nov/Dec).
- **Team member impact:** Same post might get different engagement based on the author's follower count and audience.

---

## Post-Performance Checklist
- [ ] LinkedIn URL recorded
- [ ] Engagement data collected (after 3-7 days)
- [ ] Performance level assigned (below avg / avg / above avg / exceptional)
- [ ] Learnings documented in memory.md
- [ ] Team member feedback noted (if any)
- [ ] Pattern analysis updated (every 5 posts)
```

- [ ] **Step 2: Commit**

```bash
cd "d:\MTB'S AGENT"
git add skills/performance-tracking.md
git commit -m "skill: add performance-tracking for LinkedIn engagement analysis

- Track likes, comments, shares, reach for each post
- Check engagement 3-7 days after posting
- Identify patterns (what post types win, what data resonates)
- Update memory.md with learnings for future optimization
- Includes data collection template and common mistakes"
```

Expected: Commit succeeds.

---

### Task 8: End-to-End MVP Test

**Files:**
- Use: All created files (CLAUDE.md, skills, docs, memory.md)
- Update: memory.md with first post data

**Context:** Now that all skills are in place, run a complete workflow: query Rumi → generate post → send to Slack → get approval → log in memory.

- [ ] **Step 1: Query Rumi for Post Ideas**

In Claude Code, type:

```
"Using the rumi-analysis skill, what are the top 3 post-worthy insights from Rumi this week? 
Please include:
1. The metric/finding
2. Why it matters
3. Which team member's expertise it best fits
"
```

Expected: Agent returns 3 findings with context and recommended team member.

- [ ] **Step 2: Generate a Draft Post**

Ask the agent:

```
"Based on the top finding from Step 1, generate a LinkedIn post for [Team Member Name] 
using the post-generation skill. Make sure it:
- Sounds authentic to their voice
- Leads with the data
- Includes context on why it matters
- Ends with a question or call-to-action
"
```

Expected: Agent returns a draft post (100-300 words).

- [ ] **Step 3: Review the Draft**

Read the post. Does it:
- [ ] Sound authentic (not generic AI)?
- [ ] Reference real Rumi data?
- [ ] Answer "why should someone care"?
- [ ] End with an engagement hook?

If yes, proceed. If no, ask agent to revise.

- [ ] **Step 4: Send to Slack (Simulated)**

Ask the agent:

```
"Format this post for Slack using the slack-integration skill. Include:
- Clear formatting with the draft post
- Tags for @mahnoor.tanweer and the assigned team member
- Context on what data was used
- Instructions for the approval workflow (✅ / 💬 / ❌)
"
```

Expected: Agent returns a formatted Slack message ready to send.

- [ ] **Step 5: Simulate Approval**

Ask the agent:

```
"Assume the post gets a ✅ approval from both Mahnoor and the team member. 
According to the slack-integration skill, what's the next step?"
```

Expected: Agent confirms team member posts on LinkedIn.

- [ ] **Step 6: Log in memory.md**

Ask the agent:

```
"Using the performance-tracking skill, create a memory.md entry for this post. 
Include:
- Post metadata (date, author, topic, data used)
- Placeholder for engagement data (to be filled in 7 days)
- Reminder to check engagement on [date 7 days from today]
"
```

Expected: Agent provides memory.md entry.

- [ ] **Step 7: Update memory.md**

Copy the memory.md entry from Step 6 into your actual `d:\MTB'S AGENT\memory.md` file.

Modify: `d:\MTB'S AGENT\memory.md`

Add this to the "Post History" section:

```markdown
## Post History

### Post #1 (2026-06-16)
- Author: [Team Member Name]
- Topic: [Topic from Step 1]
- Data used: [Metrics from the post]
- Posted: Pending (waiting for team member to post on LinkedIn)
- LinkedIn URL: [TBD]
- Status: In approval workflow

**Engagement tracking date:** 2026-06-23 (check in 7 days)
```

- [ ] **Step 8: Commit**

```bash
cd "d:\MTB'S AGENT"
git add memory.md
git commit -m "feat: log first post in memory for tracking

- Post #1 generated and sent to Slack approval workflow
- Data from Rumi analysis skill, post from post-generation skill
- Awaiting team member approval and LinkedIn posting
- Engagement metrics to be collected in 7 days"
```

Expected: Commit succeeds.

---

### Task 9: Verify Complete Workflow

**Context:** Quick sanity check to make sure all parts work together.

- [ ] **Step 1: Review all files created**

Run:
```powershell
Get-ChildItem -Path "d:\MTB'S AGENT" -Recurse -File | Select-Object FullName | Sort-Object FullName
```

Expected output should show:
```
d:\MTB'S AGENT\CLAUDE.md
d:\MTB'S AGENT\memory.md
d:\MTB'S AGENT\docs\superpowers\specs\2026-06-16-linkedin-content-agent-design.md
d:\MTB'S AGENT\docs\superpowers\plans\2026-06-16-linkedin-content-agent-implementation.md
d:\MTB'S AGENT\docs\team-roster.md
d:\MTB'S AGENT\docs\trending-topics.md
d:\MTB'S AGENT\docs\post-templates.md
d:\MTB'S AGENT\docs\rumi-schema.md
d:\MTB'S AGENT\skills\rumi-analysis.md
d:\MTB'S AGENT\skills\post-generation.md
d:\MTB'S AGENT\skills\slack-integration.md
d:\MTB'S AGENT\skills\performance-tracking.md
```

- [ ] **Step 2: Check CLAUDE.md is readable**

Open `d:\MTB'S AGENT\CLAUDE.md` and verify:
- [ ] Project name is clear
- [ ] Team roster is listed (even if names are TBD)
- [ ] All skill pointers are present
- [ ] Key rules are clear

- [ ] **Step 3: Verify skills are complete**

Check that each skill file has:
- [ ] Purpose statement
- [ ] Prerequisites
- [ ] Step-by-step instructions
- [ ] Example run
- [ ] Common mistakes section
- [ ] Notes section

- [ ] **Step 4: Check git history**

Run:
```bash
cd "d:\MTB'S AGENT"
git log --oneline
```

Expected: 4 commits:
1. "chore: initialize project structure and CLAUDE.md"
2. "docs: add team roster, trending topics, and post templates"
3. "feat: connect to Rumi database via MCP"
4. "skill: add rumi-analysis for extracting post-worthy insights"
5. "skill: add post-generation for creating authentic LinkedIn posts"
6. "skill: add slack-integration for post approval workflow"
7. "skill: add performance-tracking for LinkedIn engagement analysis"
8. "feat: log first post in memory for tracking"

- [ ] **Step 5: Final Verification**

Ask the agent:

```
"Can you verify the LinkedIn Content Agent MVP is complete? Check:
1. Is CLAUDE.md the entry point for the agent?
2. Are all 4 core skills in place (rumi-analysis, post-generation, slack-integration, performance-tracking)?
3. Is the Rumi database connected via MCP?
4. Are all supporting docs present (team-roster, trending-topics, post-templates, rumi-schema)?
5. Is memory.md set up for tracking posts?
6. Can we generate → Slack → approve → track a post end-to-end?

If all 6 are yes, the MVP is ready for daily automation."
```

Expected: Agent confirms MVP is complete.

---

## Summary & Next Steps

**MVP Complete:** The LinkedIn Content Agent is now set up and ready.

**What's working:**
- ✅ CLAUDE.md routes to all skills
- ✅ Rumi database connected (read-only)
- ✅ Can query Rumi for insights
- ✅ Can generate authentic posts
- ✅ Can send to Slack for approval
- ✅ Can track performance
- ✅ Can log learnings in memory.md

**Immediate next steps (after MVP launch):**
1. **Automation:** Set up daily post generation at set time (e.g., 9 AM daily)
2. **Team member assignment:** Fill in names and Slack IDs in docs/team-roster.md
3. **First week:** Generate 5 posts, get team member approval, collect engagement data
4. **Optimization:** Update memory.md with patterns, refine post templates based on what works

**Phase 2 (Week 2+):**
- Connect external dashboards when available
- Add trend detection
- Refine post generation based on engagement patterns
- Consider auto-scheduling (agent picks best time to notify)

---

**Saved to:** `docs/superpowers/plans/2026-06-16-linkedin-content-agent-implementation.md`
