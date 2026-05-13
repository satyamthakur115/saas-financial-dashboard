import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('data/saas_financial_data.csv')

monthly = df.groupby(['date', 'month', 'year', 'quarter']).agg(
    total_mrr=('mrr', 'sum'),
    total_customers=('total_customers', 'sum'),
    total_new=('new_customers', 'sum'),
    total_churned=('churned_customers', 'sum'),
    total_actual=('actual_revenue', 'sum'),
    total_budget=('budget_revenue', 'sum'),
    total_variance=('variance', 'sum'),
    avg_cac=('cac', 'mean'),
    avg_ltv=('ltv', 'mean'),
    marketing_spend=('marketing_spend', 'sum'),
).reset_index().sort_values('date')

monthly['variance_pct'] = (
    (monthly['total_actual'] - monthly['total_budget']) /
    monthly['total_budget'] * 100).round(1)
monthly['churn_rate'] = (
    monthly['total_churned'] /
    monthly['total_customers'] * 100).round(2)

fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        'Monthly Recurring Revenue (MRR) by Plan',
        'Budget vs Actual Revenue',
        'Revenue Variance % (Actual vs Budget)',
        'Total Customer Growth by Plan',
        'LTV vs CAC',
        'Monthly Churn Rate %'
    ),
    vertical_spacing=0.12,
    horizontal_spacing=0.08
)

# Chart 1 - MRR
for plan in df['plan'].unique():
    plan_df = df[df['plan'] == plan].sort_values('date')
    fig.add_trace(go.Scatter(
        x=plan_df['date'], y=plan_df['mrr'],
        name=plan, mode='lines+markers',
        marker=dict(size=4),
        legendgroup=plan
    ), row=1, col=1)

# Chart 2 - Budget vs Actual
fig.add_trace(go.Bar(
    x=monthly['date'], y=monthly['total_actual'],
    name='Actual', marker_color='#0288d1',
    showlegend=False
), row=1, col=2)
fig.add_trace(go.Bar(
    x=monthly['date'], y=monthly['total_budget'],
    name='Budget', marker_color='#b0bec5',
    showlegend=False
), row=1, col=2)

# Chart 3 - Variance %
fig.add_trace(go.Bar(
    x=monthly['date'],
    y=monthly['variance_pct'],
    marker_color=['#ef5350' if v < 0 else '#26a69a'
                  for v in monthly['variance_pct']],
    name='Variance %', showlegend=False
), row=2, col=1)

# Chart 4 - Customer Growth
for plan in df['plan'].unique():
    plan_df = df[df['plan'] == plan].sort_values('date')
    fig.add_trace(go.Scatter(
        x=plan_df['date'], y=plan_df['total_customers'],
        name=plan, mode='lines+markers',
        stackgroup='one',
        legendgroup=plan, showlegend=False
    ), row=2, col=2)

# Chart 5 - LTV vs CAC
fig.add_trace(go.Scatter(
    x=monthly['date'], y=monthly['avg_ltv'],
    name='LTV', mode='lines+markers',
    line=dict(color='#26a69a', width=2),
    showlegend=False
), row=3, col=1)
fig.add_trace(go.Scatter(
    x=monthly['date'], y=monthly['avg_cac'],
    name='CAC', mode='lines+markers',
    line=dict(color='#ef5350', width=2),
    showlegend=False
), row=3, col=1)

# Chart 6 - Churn Rate
fig.add_trace(go.Scatter(
    x=monthly['date'], y=monthly['churn_rate'],
    mode='lines+markers',
    line=dict(color='#ef5350', width=2),
    fill='tozeroy', fillcolor='rgba(239,83,80,0.1)',
    name='Churn %', showlegend=False
), row=3, col=2)

fig.update_layout(
    title=dict(
        text='TechFlow SaaS Inc. — Financial Performance Dashboard',
        font=dict(size=22),
        x=0.5
    ),
    height=1100,
    template='plotly_white',
    barmode='group',
    legend=dict(
        orientation='h',
        y=-0.05,
        x=0.5,
        xanchor='center'
    )
)

fig.write_html('data/saas_dashboard.html')
print("Combined dashboard saved to data/saas_dashboard.html")
print("Open it in your browser to view!")