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
