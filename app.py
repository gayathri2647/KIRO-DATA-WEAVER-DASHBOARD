import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(page_title="Data Weaver Dashboard", page_icon="🌦️", layout="wide")

# Load and process data
@st.cache_data
def load_data():
    weather = pd.read_csv('weather.csv')
    food_orders = pd.read_csv('food_orders.csv')
    
    # Convert dates
    weather['date'] = pd.to_datetime(weather['date'])
    food_orders['date'] = pd.to_datetime(food_orders['date'])
    
    # Aggregate food orders by date
    daily_orders = food_orders.groupby('date')['total_orders'].sum().reset_index()
    
    # Merge datasets
    merged_data = pd.merge(weather, daily_orders, on='date')
    
    # Create rain categories
    merged_data['rain_category'] = merged_data['rainfall'].apply(
        lambda x: 'Rainy' if x > 5 else 'Sunny'
    )
    
    return weather, food_orders, merged_data

weather_df, food_orders_df, merged_df = load_data()

# Dashboard header
st.title("🌦️ Data Weaver Dashboard")
st.markdown("**Analyzing the relationship between Weather and Food Orders**")

# Overview metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Orders", f"{merged_df['total_orders'].sum():,}")

with col2:
    st.metric("Avg Temperature", f"{merged_df['temperature'].mean():.1f}°C")

with col3:
    rainy_days = len(merged_df[merged_df['rain_category'] == 'Rainy'])
    st.metric("Rainy Days", rainy_days)

with col4:
    avg_orders_rain = merged_df[merged_df['rain_category'] == 'Rainy']['total_orders'].mean()
    avg_orders_sunny = merged_df[merged_df['rain_category'] == 'Sunny']['total_orders'].mean()
    st.metric("Rain vs Sunny Orders", f"+{((avg_orders_rain/avg_orders_sunny-1)*100):.0f}%")

st.divider()

# Charts section
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Temperature vs Orders Trend")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=merged_df['date'], y=merged_df['temperature'], 
                             name='Temperature (°C)', line=dict(color='red')))
    fig1.add_trace(go.Scatter(x=merged_df['date'], y=merged_df['total_orders']/10, 
                             name='Orders (÷10)', line=dict(color='blue')))
    fig1.update_layout(height=400, showlegend=True)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("☔ Rainy vs Sunny Day Orders")
    rain_orders = merged_df.groupby('rain_category')['total_orders'].sum()
    fig2 = px.bar(x=rain_orders.index, y=rain_orders.values, 
                  color=rain_orders.index, color_discrete_map={'Rainy': '#1f77b4', 'Sunny': '#ff7f0e'})
    fig2.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)

# Food category analysis
st.subheader("🍽️ Food Category Distribution")
col1, col2 = st.columns(2)

with col1:
    category_totals = food_orders_df.groupby('food_category')['total_orders'].sum()
    fig3 = px.pie(values=category_totals.values, names=category_totals.index, 
                  color_discrete_sequence=['#ff9999', '#66b3ff', '#99ff99'])
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("Key Insights")
    
    # Calculate correlations and insights
    temp_corr = merged_df['temperature'].corr(merged_df['total_orders'])
    
    st.write("**Weather Impact on Orders:**")
    st.write(f"• Orders increase by {((avg_orders_rain/avg_orders_sunny-1)*100):.0f}% on rainy days")
    st.write(f"• Temperature correlation: {temp_corr:.2f}")
    
    st.write("**Popular Categories:**")
    for category, total in category_totals.items():
        percentage = (total / category_totals.sum()) * 100
        st.write(f"• {category}: {percentage:.1f}% of orders")
    
    st.write("**Business Recommendations:**")
    st.write("• Stock more comfort food during rainy weather")
    st.write("• Indian cuisine dominates - expand variety")
    st.write("• Weather-based promotional campaigns")

# Raw data section
with st.expander("View Raw Data"):
    tab1, tab2, tab3 = st.tabs(["Weather Data", "Food Orders", "Merged Data"])
    
    with tab1:
        st.dataframe(weather_df)
    
    with tab2:
        st.dataframe(food_orders_df)
    
    with tab3:
        st.dataframe(merged_df)