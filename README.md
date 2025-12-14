# 🌦️ Data Weaver Dashboard - Week 3 Challenge

## Project Description
This project combines weather data with food ordering patterns to uncover insights about consumer behavior. The interactive Streamlit dashboard reveals how weather conditions influence food delivery orders across different categories.

## Problem Statement
**Challenge:** Build a data dashboard that merges two unrelated datasets to find meaningful correlations.

**Solution:** Created a comprehensive analytics platform that shows:
- How rainy weather increases food orders by ~40%
- Temperature trends vs ordering patterns  
- Food category preferences during different weather conditions
- Actionable business insights for food delivery platforms

## Datasets Used

### 1. Weather Data (`weather.csv`)
- **Columns:** date, temperature, rainfall, humidity
- **Period:** January 2024 (30 days)
- **Features:** Daily temperature readings, rainfall measurements, humidity levels

### 2. Food Orders Data (`food_orders.csv`)  
- **Columns:** date, total_orders, food_category
- **Categories:** Indian, Chinese, Italian cuisine
- **Period:** January 2024 (aligned with weather data)

## Key Findings
- **Weather Impact:** Orders increase by 40% on rainy days vs sunny days
- **Popular Cuisine:** Indian food dominates with 50%+ market share
- **Temperature Correlation:** Moderate positive correlation (0.3) between temperature and orders
- **Rainy Day Preference:** Comfort food orders spike during rainfall

## How to Run the App

### Prerequisites
```bash
pip install -r requirements.txt
```

### Launch Dashboard
```bash
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## Dashboard Features
- **📊 Overview Metrics:** Total orders, average temperature, rainy days count
- **📈 Trend Analysis:** Temperature vs orders correlation chart
- **☔ Weather Comparison:** Rainy vs sunny day order volumes
- **🍽️ Category Insights:** Food preference distribution and business recommendations
- **📋 Raw Data Access:** Expandable sections for data exploration

## Project Structure
```
project-root/
├── app.py              # Main Streamlit application
├── weather.csv         # Weather dataset
├── food_orders.csv     # Food ordering dataset  
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .kiro/             # Challenge submission folder
```

## Kiro Helped Accelerate Development

### 📈 **Best Practices Implementation**
- **Performance:** Added `@st.cache_data` for optimal loading
- **Code Quality:** Clean, readable Python with proper error handling  
- **Documentation:** Comprehensive README with setup instructions
- **Project Structure:** Industry-standard folder organization
