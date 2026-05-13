import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

df = pd.read_csv('data/saas_financial_data.csv')

monthly = df.groupby(['date', 'month', 'year', 'quarter']).agg(
    total_mrr=('mrr', 'sum'),
    total_arr=('arr', 'sum'),
    total_customers=('total_customers', 'sum'),
    total_new=('new_customers', 'sum'),
    total_churned=('churned_customers', 'sum'),
    total_actual=('actual_revenue', 'sum'),
    total_budget=('budget_revenue', 'sum'),
    total_variance=('variance', 'sum'),
    avg_cac=('cac', 'mean'),
    avg_ltv=('ltv', 'mean'),
    avg_ltv_cac=('ltv_cac_ratio', 'mean'),
    marketing_spend=('marketing_spend', 'sum'),
).reset_index().sort_values('date')

monthly['variance_pct'] = (
    (monthly['total_actual'] - monthly['total_budget']) /
    monthly['total_budget'] * 100).round(1)
monthly['churn_rate'] = (
    monthly['total_churned'] /
    monthly['total_customers'] * 100).round(2)

colors = {
    'Starter': '#4fc3f7',
    'Pro': '#29b6f6',
    'Business': '#0288d1',
    'Enterprise': '#01579b'
}

# --- Chart 1: MRR Growth ---
fig1 = go.Figure()
for plan in df['plan'].unique():
    plan_df = df[df['plan'] == plan].sort_values('date')
    fig1.add_trace(go.Scatter(
        x=plan_df['date'], y=plan_df['mrr'],
        name=plan, mode='lines+markers',
        line=dict(width=2),
        marker=dict(size=5)
    ))
fig1.update_layout(
    title='Monthly Recurring Revenue (MRR) by Plan',
    xaxis_title='Month', yaxis_title='MRR ($)',
    template='plotly_white', height=400,
    legend=dict(orientation='h', y=-0.2)
)
fig1.write_html('data/chart_mrr.html')
print("Chart 1 done - MRR Growth")

# --- Chart 2: Budget vs Actual ---
fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=monthly['date'], y=monthly['total_actual'],
    name='Actual Revenue', marker_color='#0288d1'
))
fig2.add_trace(go.Bar(
    x=monthly['date'], y=monthly['total_budget'],
    name='Budget Revenue', marker_color='#b0bec5'
))
fig2.update_layout(
    title='Budget vs Actual Revenue',
    xaxis_title='Month', yaxis_title='Revenue ($)',
    barmode='group', template='plotly_white', height=400,
    legend=dict(orientation='h', y=-0.2)
)
fig2.write_html('data/chart_budget_vs_actual.html')
print("Chart 2 done - Budget vs Actual")

# --- Chart 3: Variance % ---
fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=monthly['date'],
    y=monthly['variance_pct'],
    marker_color=['#ef5350' if v < 0 else '#26a69a'
                  for v in monthly['variance_pct']],
    name='Variance %'
))
fig3.add_hline(y=0, line_dash='dash', line_color='gray')
fig3.update_layout(
    title='Revenue Variance % (Actual vs Budget)',
    xaxis_title='Month', yaxis_title='Variance %',
    template='plotly_white', height=400
)
fig3.write_html('data/chart_variance.html')
print("Chart 3 done - Variance")

# --- Chart 4: Customer Growth ---
fig4 = go.Figure()
for plan in df['plan'].unique():
    plan_df = df[df['plan'] == plan].sort_values('date')
    fig4.add_trace(go.Scatter(
        x=plan_df['date'], y=plan_df['total_customers'],
        name=plan, mode='lines+markers',
        stackgroup='one'
    ))
fig4.update_layout(
    title='Total Customer Growth by Plan',
    xaxis_title='Month', yaxis_title='Total Customers',
    template='plotly_white', height=400,
    legend=dict(orientation='h', y=-0.2)
)
fig4.write_html('data/chart_customers.html')
print("Chart 4 done - Customer Growth")

# --- Chart 5: CAC vs LTV ---
fig5 = go.Figure()
fig5.add_trace(go.Scatter(
    x=monthly['date'], y=monthly['avg_ltv'],
    name='Avg LTV', mode='lines+markers',
    line=dict(color='#26a69a', width=2)
))
fig5.add_trace(go.Scatter(
    x=monthly['date'], y=monthly['avg_cac'],
    name='Avg CAC', mode='lines+markers',
    line=dict(color='#ef5350', width=2)
))
fig5.update_layout(
    title='Customer Lifetime Value (LTV) vs Acquisition Cost (CAC)',
    xaxis_title='Month', yaxis_title='Amount ($)',
    template='plotly_white', height=400,
    legend=dict(orientation='h', y=-0.2)
)
fig5.write_html('data/chart_ltv_cac.html')
print("Chart 5 done - LTV vs CAC")

# --- Chart 6: Churn Rate ---
fig6 = go.Figure()
fig6.add_trace(go.Scatter(
    x=monthly['date'], y=monthly['churn_rate'],
    mode='lines+markers',
    line=dict(color='#ef5350', width=2),
    fill='tozeroy', fillcolor='rgba(239,83,80,0.1)'
))
fig6.update_layout(
    title='Monthly Churn Rate %',
    xaxis_title='Month', yaxis_title='Churn Rate %',
    template='plotly_white', height=400
)
fig6.write_html('data/chart_churn.html')
print("Chart 6 done - Churn Rate")

print("\nAll charts saved to data/ folder!")
print("Open any .html file in your browser to view the charts.")