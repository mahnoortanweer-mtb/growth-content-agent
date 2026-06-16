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
- **Escalation:** If 24 hours pass with no response, escalate to Mahnoor via DM.
