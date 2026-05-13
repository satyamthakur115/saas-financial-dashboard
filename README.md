# 📊 SaaS Financial Performance & Forecasting Dashboard

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=mysql&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat)

> End-to-end SaaS financial analytics system tracking MRR, ARR, Budget vs Actual variance, Customer Churn, CAC and LTV across 24 months using Python and Plotly.

---

## 📊 Dashboard Preview

![SaaS Dashboard](data/saas_dashboard.png)

---

## 📌 Project Overview

This project models a real SaaS company financial analytics workflow — the kind of analysis done daily by Financial Analysts and BI Analysts at tech companies.

**Raw data → Python ETL → Financial KPIs → Variance Analysis → Interactive Plotly Dashboard**

### Business questions answered:
- How is Monthly Recurring Revenue (MRR) growing across plans?
- Where is actual revenue exceeding or missing budget targets?
- Which customer plans have the highest churn risk?
- Is our Customer Lifetime Value (LTV) healthy compared to Acquisition Cost (CAC)?
- How are total customers growing month over month?

---

## 💡 Key Insights

| Metric | Finding |
|--------|---------|
| MRR Growth | Enterprise plan grew from **$3,897 → $190K+** over 24 months |
| Budget vs Actual | Company consistently **exceeded budget** from Q2 2022 onwards |
| Best LTV/CAC Ratio | Enterprise plan at **LTV $129,900 vs CAC ~$200** |
| Churn Rate | Stabilized between **4–6%** monthly after initial ramp |
| Customer Growth | Total customers grew from **137 → 2,300+** over 2 years |

---

## 🗂️ Project Structure

```
saas-financial-dashboard/
│
├── python/
│   ├── generate_data.py         # Generates 24 months of SaaS financial data
│   ├── dashboard.py             # Creates individual chart HTML files
│   └── combined_dashboard.py   # Creates single combined dashboard HTML
│
├── data/
│   ├── saas_financial_data.csv  # Generated dataset (96 rows)
│   ├── saas_dashboard.png       # Dashboard screenshot
│   └── saas_dashboard.html      # Interactive Plotly dashboard
│
└── README.md
```

---

## 📈 Metrics Tracked

| Metric | Description |
|--------|-------------|
| MRR | Monthly Recurring Revenue per plan |
| ARR | Annual Recurring Revenue (MRR × 12) |
| Budget vs Actual | Monthly revenue vs target with variance % |
| Churn Rate | % of customers lost each month |
| CAC | Customer Acquisition Cost (marketing spend / new customers) |
| LTV | Customer Lifetime Value (price / churn rate) |
| LTV/CAC Ratio | Health indicator — ratio above 3x is considered strong |
| New vs Churned | Monthly customer flow per plan |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Data Generation | Python 3.10+, Pandas, NumPy |
| Financial Modeling | Python (variance, churn, LTV/CAC calculations) |
| Visualization | Plotly (interactive HTML charts) |
| Version Control | Git / GitHub |

---

## ⚡ Quick Start

```bash
git clone https://github.com/satyamthakur115/saas-financial-dashboard.git
cd saas-financial-dashboard
pip install pandas plotly numpy
python python/generate_data.py
python python/combined_dashboard.py
```

Then open `data/saas_dashboard.html` in your browser.

---

## 🔍 Key Financial Concepts Used

- **MRR/ARR** — standard SaaS revenue metrics used by every tech company
- **Budget variance analysis** — actual vs target with % deviation
- **Churn rate modeling** — plan-specific churn with realistic randomization
- **LTV/CAC ratio** — gold standard SaaS health metric (healthy = 3x+)
- **Rolling customer cohorts** — tracking new, churned and total customers per plan
- **Waterfall revenue flow** — showing where revenue was gained or lost

---

## 📬 Connect

**Satyam Thakur** — Data Analyst

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/YOUR-LINKEDIN-URL)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/satyamthakur115)
