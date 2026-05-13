import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# Company config
COMPANY = "TechFlow SaaS Inc."
START_DATE = datetime(2022, 1, 1)
MONTHS = 24

# Products
plans = {
    'Starter':  {'price': 49,  'churn_rate': 0.08},
    'Pro':      {'price': 149, 'churn_rate': 0.05},
    'Business': {'price': 499, 'churn_rate': 0.03},
    'Enterprise':{'price': 1299,'churn_rate': 0.01},
}

# Budget targets per month
budget_targets = {
    'Starter':   {'new_customers': 80,  'revenue_target': 4000},
    'Pro':       {'new_customers': 40,  'revenue_target': 6000},
    'Business':  {'new_customers': 15,  'revenue_target': 7500},
    'Enterprise':{'new_customers': 5,   'revenue_target': 6500},
}

records = []
customers = {plan: 0 for plan in plans}

for month_idx in range(MONTHS):
    current_date = START_DATE + timedelta(days=30 * month_idx)
    month_name = current_date.strftime('%B')
    year = current_date.year
    quarter = f"Q{(current_date.month - 1) // 3 + 1}"

    for plan, config in plans.items():
        # New customers with growth trend
        growth = 1 + (month_idx * 0.02)
        new_customers = int(random.gauss(
            budget_targets[plan]['new_customers'] * growth, 5))
        new_customers = max(0, new_customers)

        # Churned customers
        churned = int(customers[plan] * config['churn_rate']
                      * random.uniform(0.8, 1.2))
        churned = min(churned, customers[plan])

        # Update customer count
        customers[plan] = customers[plan] + new_customers - churned

        # Revenue
        actual_revenue = customers[plan] * config['price']
        budget_revenue = budget_targets[plan]['revenue_target'] * (
            1 + month_idx * 0.015)
        variance = actual_revenue - budget_revenue
        variance_pct = round((variance / budget_revenue) * 100, 1)

        # CAC and LTV
        marketing_spend = random.uniform(1500, 4000)
        cac = round(marketing_spend / max(new_customers, 1), 2)
        ltv = round((config['price'] / config['churn_rate']), 2)
        ltv_cac_ratio = round(ltv / max(cac, 1), 2)

        records.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'month': month_name,
            'month_num': current_date.month,
            'year': year,
            'quarter': quarter,
            'plan': plan,
            'price_per_user': config['price'],
            'new_customers': new_customers,
            'churned_customers': churned,
            'total_customers': customers[plan],
            'churn_rate_pct': round(config['churn_rate'] * 100, 1),
            'actual_revenue': actual_revenue,
            'budget_revenue': round(budget_revenue, 2),
            'variance': round(variance, 2),
            'variance_pct': variance_pct,
            'marketing_spend': round(marketing_spend, 2),
            'cac': cac,
            'ltv': ltv,
            'ltv_cac_ratio': ltv_cac_ratio,
            'mrr': actual_revenue,
            'arr': actual_revenue * 12,
        })

df = pd.DataFrame(records)
df.to_csv('data/saas_financial_data.csv', index=False)
print(f"Done! {len(df)} rows saved to data/saas_financial_data.csv")
print(f"\nPreview:")
print(df[['date','plan','total_customers','actual_revenue',
          'budget_revenue','variance_pct']].head(8).to_string(index=False))