import streamlit as st

# Title and Description
st.title("Simple Sales Dashboard")
st.write("Monthly Sales Dashboard")

# Months
months = ["January", "February", "March", "April"]

# Sales Dictionary
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

# Select a month
selected_month = st.selectbox("Select a Month", months)

# Display sales of selected month
st.metric("Sales", sales[selected_month])

# Bar Chart
st.subheader("Monthly Sales Chart")
st.bar_chart(list(sales.values()))