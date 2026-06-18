# Rumi Database Schema

**Status:** ✅ CONNECTED via MCP (rumi-db)
**Connected:** 2026-06-17
**Database:** PostgreSQL via Supabase
**Host:** aws-1-ap-southeast-1.pooler.supabase.com:6543
**Total Tables:** 82 (37 relevant for post generation)

---

## Post-Relevant Tables (37 Total)

### User & Profile
| Table | Purpose | Post Angle |
|-------|---------|------------|
| `users` | All user accounts (teachers, admins) | User growth, onboarding trends |
| `students` | Student data | Student engagement, outcomes |
| `student_lists` | Teacher's student rosters | Class size, teacher reach |
| `teacher_progress` | Teacher skill/usage progress | Teacher adoption, improvement |
| `teacher_facts` | Teacher profile data | Educator demographics, context |

### Lessons
| Table | Purpose | Post Angle |
|-------|---------|------------|
| `lesson_plans` | Teacher-created lesson plans | Lesson Plans adoption, usage |
| `lesson_plan_requests` | Requests for AI lesson plans | AI usage demand, feature popularity |
| `homework_chapters` | Homework content | Student engagement with homework |
| `pic_lp_sessions` | Picture-based lesson sessions | Visual learning engagement |

### Assessments
| Table | Purpose | Post Angle |
|-------|---------|------------|
| `quizzes` | Quiz content library | Assessment content growth |
| `quiz_sessions` | Student quiz attempts | Assessment engagement, completion |
| `quiz_answers` | Individual quiz answers | Learning outcomes, accuracy |
| `reading_assessments` | Reading skill evaluations | Literacy improvement tracking |
| `exam_templates` | Exam formats | Assessment variety |
| `exam_submissions` | Student exam results | Student performance outcomes |

### Videos
| Table | Purpose | Post Angle |
|-------|---------|------------|
| `videos` | Video content library | Content library growth |
| `video_requests` | Teacher video requests | Feature demand signals |
| `student_video_feedback` | Student ratings on videos | Content quality feedback |
| `audio_sessions` | Audio learning sessions | Audio engagement metrics |

### Interactive / Sessions
| Table | Purpose | Post Angle |
|-------|---------|------------|
| `chat_sessions` | AI chat interactions | AI feature adoption |
| `coaching_sessions` | Teacher coaching sessions | Coaching feature engagement |
| `byof_sessions` | Bring-your-own-format sessions | Custom content usage |
| `attendance_sessions` | Attendance tracking sessions | Regular usage/stickiness |

### Features
| Table | Purpose | Post Angle |
|-------|---------|------------|
| `feature_permissions` | Feature access control | Feature rollout tracking |
| `feature_suggestions` | User-submitted feature ideas | Community voice, product direction |
| `user_feature_first_use` | First time a user used a feature | Adoption velocity, time-to-first-use |

### Analytics
| Table | Purpose | Post Angle |
|-------|---------|------------|
| `api_usage_log` | API call tracking | Usage volume, system health |

---

## Key Query Patterns for Post Generation

### 1. User Growth (Week-over-Week)
```sql
SELECT 
  DATE_TRUNC('week', created_at) as week,
  COUNT(DISTINCT id) as new_users
FROM users
WHERE created_at >= NOW() - INTERVAL '14 days'
GROUP BY DATE_TRUNC('week', created_at)
ORDER BY week DESC;
```

### 2. Lesson Plans Adoption
```sql
SELECT 
  COUNT(DISTINCT user_id) as teachers_using,
  COUNT(*) as total_plans_created,
  AVG(EXTRACT(EPOCH FROM (created_at - u.created_at))/86400) as avg_days_to_first_plan
FROM lesson_plans lp
JOIN users u ON lp.user_id = u.id
WHERE lp.created_at >= NOW() - INTERVAL '30 days';
```

### 3. Feature First Use (Adoption Velocity)
```sql
SELECT 
  feature_name,
  COUNT(DISTINCT user_id) as users_adopted,
  MIN(first_used_at) as first_adoption,
  AVG(EXTRACT(EPOCH FROM (first_used_at - u.created_at))/86400) as avg_days_to_adopt
FROM user_feature_first_use uff
JOIN users u ON uff.user_id = u.id
GROUP BY feature_name
ORDER BY users_adopted DESC;
```

### 4. Coaching Session Engagement
```sql
SELECT 
  DATE_TRUNC('week', created_at) as week,
  COUNT(*) as sessions,
  COUNT(DISTINCT user_id) as unique_teachers
FROM coaching_sessions
WHERE created_at >= NOW() - INTERVAL '30 days'
GROUP BY DATE_TRUNC('week', created_at)
ORDER BY week DESC;
```

### 5. Quiz Completion Rates
```sql
SELECT 
  COUNT(*) as total_attempts,
  AVG(score) as avg_score,
  COUNT(DISTINCT student_id) as unique_students
FROM quiz_sessions
WHERE created_at >= NOW() - INTERVAL '7 days';
```

### 6. Reading Assessment Improvement
```sql
SELECT 
  DATE_TRUNC('month', assessment_date) as month,
  AVG(score) as avg_reading_score,
  COUNT(DISTINCT student_id) as students_assessed
FROM reading_assessments
WHERE assessment_date >= NOW() - INTERVAL '90 days'
GROUP BY DATE_TRUNC('month', assessment_date)
ORDER BY month DESC;
```

### 7. Video Engagement
```sql
SELECT 
  COUNT(*) as total_sessions,
  AVG(rating) as avg_rating,
  COUNT(DISTINCT student_id) as unique_students
FROM student_video_feedback
WHERE created_at >= NOW() - INTERVAL '7 days';
```

### 8. Feature Suggestions (Community Voice)
```sql
SELECT 
  suggestion_text,
  COUNT(*) as votes,
  COUNT(DISTINCT user_id) as unique_requesters
FROM feature_suggestions
GROUP BY suggestion_text
ORDER BY votes DESC
LIMIT 10;
```

---

## Data Freshness Notes
- **users, students:** Real-time (immediate)
- **lesson_plans, quiz_sessions, coaching_sessions:** Real-time
- **reading_assessments, exam_submissions:** On completion
- **user_feature_first_use:** Triggered on first use
- **api_usage_log:** Real-time
- **teacher_progress:** Updated on activity

---

## Post Generation Priority Tables

**For Growth Product Managers (metrics & features):**
- `user_feature_first_use` — adoption velocity
- `lesson_plans` + `lesson_plan_requests` — Lesson Plans engagement
- `quiz_sessions` + `quiz_answers` — Assessment outcomes
- `coaching_sessions` — Coaching feature engagement

**For Partnership Manager:**
- `feature_permissions` — rollout by partner/school
- `feature_suggestions` — community requests (partnership angle)
- `users` + `students` — reach metrics

**For Marketing Manager:**
- `reading_assessments` — learning outcome stories
- `student_video_feedback` — content quality signals
- `teacher_progress` — teacher journey narratives
- `attendance_sessions` — stickiness / daily active usage
