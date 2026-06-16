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
