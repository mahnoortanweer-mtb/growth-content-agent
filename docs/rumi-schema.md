# Rumi Database Schema

**Status:** TO BE FILLED AFTER MCP CONNECTION

This document outlines the Rumi database structure and which tables are relevant for post generation.

## Connection Details
- **Database Type:** [PostgreSQL / MySQL — confirm after connection]
- **Host:** [Connected via MCP]
- **Connection Status:** [Pending — ask agent to confirm "Can you list the tables in Rumi?"]

## Core Tables (Post-Relevant)

### users
- Stores teacher and admin user data
- **Key columns:** user_id, name, email, school_id, created_at, last_login
- **Used for posts:** User growth metrics, new user onboarding

### sessions
- Stores user session data (logins, app usage, engagement)
- **Key columns:** session_id, user_id, created_at, duration_minutes, features_used
- **Used for posts:** Daily active users (DAU), engagement spikes, session trends

### features
- Stores information about Rumi features (Lesson Plans, Coaching, etc.)
- **Key columns:** feature_id, feature_name, launch_date, description
- **Used for posts:** Feature announcement data, context on feature launches

### feature_adoption
- Tracks which users have adopted which features
- **Key columns:** user_id, feature_id, first_used_date, usage_count, last_used_date
- **Used for posts:** Feature adoption rates, adoption velocity, time-to-first-use

### engagement_metrics
- Daily engagement data per school/user
- **Key columns:** date, school_id, active_users, sessions, avg_session_duration
- **Used for posts:** Weekly/monthly engagement trends, week-over-week growth

### retention
- Cohort retention curves (what % of users from each cohort return)
- **Key columns:** cohort_date, days_since_join, retention_rate, user_count
- **Used for posts:** Retention curves, cohort analysis, stickiness metrics

### partnerships
- Partnership and integration data
- **Key columns:** partnership_id, partner_name, integration_type, launch_date, active_schools
- **Used for posts:** Partnership announcements, ecosystem wins

## Supporting Tables

### schools
- School/organization data
- **Key columns:** school_id, school_name, region, student_count, teacher_count

### events
- Detailed event logs (feature usage, errors, etc.)
- **Key columns:** event_id, event_type, user_id, timestamp, event_data

## Data Freshness Notes

**Update frequency (to confirm after connection):**
- sessions: Real-time or hourly
- users: Real-time
- feature_adoption: Daily
- engagement_metrics: Daily (usually updated overnight)
- retention: Daily (updated end-of-day)
- partnerships: On-demand (updated when new partnership launches)

## Query Patterns for Post Generation

### Daily Active Users
```sql
SELECT COUNT(DISTINCT user_id) as dau FROM sessions WHERE created_at >= NOW() - INTERVAL '1 day'
```

### Feature Adoption
```sql
SELECT feature_name, COUNT(DISTINCT user_id) as users, 
  COUNT(DISTINCT user_id) * 100.0 / (SELECT COUNT(DISTINCT user_id) FROM users) as adoption_rate
FROM feature_adoption f JOIN features ft ON f.feature_id = ft.feature_id
GROUP BY feature_name
```

### Weekly Retention
```sql
SELECT cohort_date, days_since_join, retention_rate FROM retention
WHERE cohort_date >= NOW() - INTERVAL '30 days'
```

---

**Next step:** After MCP is connected, fill in the actual table structures, columns, and data freshness notes.
