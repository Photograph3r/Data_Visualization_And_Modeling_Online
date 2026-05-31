# 💼 Job Market & Salary Trends Dataset (2024–2026)

**Author:** Hamna Munir  
**Version:** 1.0.0  
**Last Updated:** April 2026  
**License:** CC0: Public Domain  
**Dataset Type:** Synthetic / Simulated  

---

## 📌 Overview

This dataset provides a comprehensive, synthetic snapshot of the **global job market and salary trends** across 2024, 2025, and 2026. It covers 10,000 job records spanning 30 job titles across 15 industries and 15 countries, with detailed information on compensation, work models, skills demand, AI tool adoption, automation risk, employee satisfaction, and hiring patterns.

The data is **fully synthetic**, generated using statistically realistic distributions calibrated against publicly available labor market research. It is safe for research, academic, and machine learning use.

---

## 🎯 Use Cases

- **Salary prediction** using regression models (Linear, XGBoost, Random Forest)
- **Job market trend analysis** across years 2024–2026
- **Remote work vs on-site** compensation comparison
- **Gender pay gap** analysis across industries and roles
- **AI adoption impact** on job roles and automation risk
- **Clustering** of job profiles by skills, salary, and satisfaction
- **Hiring time prediction** based on role and company characteristics
- **Industry-wise salary benchmarking** across countries

---

## 📁 Files

| File | Description |
|------|-------------|
| `job_market_salary_trends.csv` | Main dataset — 10,000 rows × 32 columns |
| `dataset-metadata.json` | Kaggle metadata with column descriptors |
| `README.md` | Full documentation (this file) |

---

## 📊 Dataset Schema

### 🔑 Identifier & Time

| Column | Type | Description |
|--------|------|-------------|
| `job_id` | string | Unique job record identifier (JOB000001–JOB010000) |
| `year` | int | Year of job posting: 2024, 2025, or 2026 |
| `quarter` | string | Quarter of job posting: Q1, Q2, Q3, Q4 |

---

### 💼 Job & Role Details

| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `job_title` | string | Specific job title | Software Engineer, Data Scientist, Product Manager... |
| `job_category` | string | Broad category of the role | Tech & Engineering, Data & AI, Finance & Legal... |
| `industry` | string | Industry sector | Technology, Finance & Banking, Healthcare... |
| `employment_type` | string | Nature of employment | Full-time, Part-time, Contract, Freelance, Remote Full-time |
| `work_model` | string | Work arrangement | On-site, Remote, Hybrid |
| `company_size` | string | Size of the hiring company | Startup (1–50) to Enterprise (5000+) |
| `job_posting_platform` | string | Where the job was posted | LinkedIn, Indeed, Glassdoor, Referral... |
| `hiring_time_days` | int | Days taken to fill the position | 3–180 |
| `visa_sponsorship_available` | string | Whether visa sponsorship is offered | Yes, No |

---

### 🌍 Location

| Column | Type | Description |
|--------|------|-------------|
| `country` | string | Country of the job location (15 countries) |

---

### 👤 Candidate Profile

| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `experience_level` | string | Seniority level | Entry Level, Junior, Mid-level, Senior, Lead/Principal |
| `years_of_experience` | int | Total years of professional experience | 0–25 |
| `education_level` | string | Highest education qualification | High School to PhD |
| `gender` | string | Gender of the job holder | Male, Female, Non-binary |
| `age_group` | string | Age bracket | 18-24, 25-34, 35-44, 45-54, 55+ |
| `certifications_count` | int | Number of professional certifications held | 0–10 |
| `primary_skills` | string | Main technical skill set | Python/SQL, React/JS, AWS/Docker... |
| `required_skills_count` | int | Number of skills required for the role | 2–8 |

---

### 💰 Compensation

| Column | Type | Description |
|--------|------|-------------|
| `salary_usd_annual` | int | Annual base salary in USD |
| `salary_local_currency` | int | Annual salary in the local currency |
| `currency` | string | ISO currency code (USD, GBP, EUR, INR, PKR, AED...) |
| `benefits_score` | int | Employer benefits quality score (1=Poor, 10=Excellent) |

---

### 😊 Satisfaction & Well-being

| Column | Type | Description | Scale |
|--------|------|-------------|-------|
| `job_satisfaction` | string | Overall job satisfaction | Very Dissatisfied → Very Satisfied |
| `salary_satisfaction` | string | Satisfaction with pay | Very Dissatisfied → Very Satisfied |
| `work_life_balance_score` | int | Work-life balance rating | 1 (Very Poor) – 10 (Excellent) |
| `career_growth_score` | int | Career advancement opportunities rating | 1 (Very Poor) – 10 (Excellent) |
| `remote_work_preference` | string | Preference for remote work | Strongly Prefer Remote → Strongly Prefer On-site |

---

### 🤖 AI & Automation

| Column | Type | Description | Sample Values |
|--------|------|-------------|---------------|
| `ai_tools_usage` | string | Frequency of AI tool usage at work | Never, Rarely, Sometimes, Often, Daily |
| `automation_risk_level` | string | Risk level of role being automated | Very Low → Very High |

---

## 📈 Key Statistics

| Metric | Value |
|--------|-------|
| Total Records | 10,000 |
| Total Features | 32 |
| Years Covered | 2024, 2025, 2026 |
| Countries | 15 |
| Job Titles | 30 |
| Industries | 15 |
| Avg Salary (USD) | ~$95,000 |
| Salary Range | ~$35,000 – ~$260,000 |
| Remote Workers | ~35% |

---

## 🔬 Suggested Research Questions

1. How have salaries changed from 2024 to 2026 across different industries?
2. Is there a significant gender pay gap in Tech vs Finance roles?
3. Do remote workers earn more than on-site workers for the same role?
4. Which job titles face the highest automation risk?
5. How does company size affect salary, benefits, and satisfaction?
6. Can we accurately predict salary using ML based on role, country, and experience?
7. What is the relationship between AI tool usage and career growth score?
8. Which countries offer the best compensation when adjusted for cost of living?
9. How does education level impact salary across different industries?
10. What factors most influence hiring time?

---

## 🧮 Salary Generation Methodology

Salaries were generated using the following logic:
- **Base range** set by experience level (Entry: $35K–$60K → Lead: $145K–$250K)
- **Industry multipliers** applied (Tech: 1.25x, Education: 0.85x, etc.)
- **Remote premium**: +5% for remote roles
- **Year-over-year growth**: +4% per year (2024 → 2025 → 2026)
- **Local currency** converted using approximate 2025 exchange rates

---

## ⚠️ Disclaimer

This dataset is **entirely synthetic**. All records were generated programmatically. No real employee, company, or salary data was used. Any resemblance to real individuals or organizations is coincidental. Do not use for real hiring, compensation, or policy decisions.

---

## 📜 Citation

```
Munir, H. (2026). Job Market & Salary Trends Dataset 2024–2026 (Synthetic) [Data set]. Kaggle.
https://www.kaggle.com/datasets/hamnamunir/job-market-salary-trends
```

---

## 🤝 Author

**Hamna Munir**  
Data Scientist & Researcher  
🌐 Kaggle: [kaggle.com/hamnamunir](https://www.kaggle.com/hamnamunir)

---

*Synthetic dataset for educational and research purposes. CC0 Public Domain License.*
