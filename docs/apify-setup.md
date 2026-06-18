# Apify Setup: LinkedIn Profile & Engagement Scraping

**Purpose:** Allow the agent to automatically read team members' LinkedIn posts (for voice profiling) and track post engagement metrics (likes, comments, shares).
**Cost:** Free tier — $5/month credit, we use ~$0.50/month.
**Time to set up:** ~15 minutes

---

## Part 1: Create Apify Account

1. Go to **apify.com** and sign up (free, no credit card required)
2. Verify your email
3. You'll land on the Apify Console dashboard

---

## Part 2: Get Your API Key

1. In Apify Console → click your profile (top right) → **Settings**
2. Go to **Integrations** tab
3. Under **Personal API tokens** → copy your token (looks like `apify_api_xxxxxxxxxxxx`)
4. Keep this — you'll need it in Part 4

---

## Part 3: Find the Right Scrapers

You'll use two Apify "Actors" (their term for scrapers):

### Actor 1: LinkedIn Profile Scraper
- Search "LinkedIn Profile Scraper" in the Apify Store
- Actor by: **apify** (official) or **bebity** (recommended — more reliable for posts)
- Used for: pulling a person's recent posts + bio

### Actor 2: LinkedIn Post Scraper (for engagement)
- Search "LinkedIn Post Scraper" in the Apify Store
- Actor by: **bebity** or **curious_coder**
- Used for: getting likes, comments, shares on specific posts

You don't need to configure anything yet — just note the Actor names/IDs.

---

## Part 4: Add Apify MCP to Claude Code

Open Claude Code and run:

```
/mcp add
```

Select **Apify** from the list (or manually add it):

**MCP name:** `apify`
**Configuration:**
```json
{
  "APIFY_TOKEN": "your_api_token_here"
}
```

Replace `your_api_token_here` with the token from Part 2.

Alternatively, add it directly to your Claude Code MCP config:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

---

## Part 5: Test the Connection

In a new Claude Code session, say:

```
Use the Apify MCP to run the LinkedIn Profile Scraper for 
https://www.linkedin.com/in/waqastanveer/ and return his last 5 posts.
```

If it works, you'll see Waqas's posts returned as structured data.

---

## Part 6: Tell Me It's Connected

Once you've done Parts 1–5, come back and say **"Apify connected"** and I will:

1. Build the **voice profiling skill** — runs once per team member, analyzes their post style, saves a persona profile for each person to `docs/voice-profiles/`
2. Build the **engagement tracking automation** — runs weekly, pulls likes/comments/shares for all posts from the past week, logs to `memory.md`
3. Update `CLAUDE.md` to reference both new skills
4. Wire it into the post generation flow so every post is written in that person's real voice

---

## LinkedIn Profile URLs (collected so far)

| Person | LinkedIn URL |
|--------|-------------|
| Waqas Tanveer | https://www.linkedin.com/in/waqastanveer/ |
| Junaid Ali | https://www.linkedin.com/in/junaid-ali786/ |
| Gul Perwasha | https://www.linkedin.com/in/gul-perwasha-938336147/ |
| Zeest Qureshi | Not yet shared |
| Amina Tayyub | Not yet shared |
| Mahnoor Tanweer Butt | Not yet shared |

**Add the missing 3 URLs once you have them — needed before voice profiling can run.**

---

## What the Agent Will Do Once Set Up

### Weekly automation (every Monday):
1. Pull each team member's posts from the past week
2. Check engagement on posts the agent generated (likes, comments, shares, reposts)
3. Log to `memory.md` → feeds into next week's post generation
4. Flag high-performing posts → agent learns what resonates

### One-time voice profiling (runs once per person):
1. Pull last 20–30 posts per person
2. Analyze: sentence length, vocabulary, hooks they use, data vs storytelling, hashtags, post length, recurring themes
3. Save to `docs/voice-profiles/[name].md`
4. Agent reads this file every time it writes a post for that person

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| MCP not showing in Claude Code | Restart Claude Code after adding the MCP config |
| Actor fails with auth error | Check your API token is correct in the MCP config |
| LinkedIn returns empty results | LinkedIn occasionally blocks — retry after 30 min |
| Actor costs more than expected | Switch to a cheaper Actor in the Apify Store |
