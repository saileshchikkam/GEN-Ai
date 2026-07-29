import streamlit as st
name = st.sidebar.text_input("Product name: ")
category = st.sidebar.selectbox(
    "Select Product Category",
    ["Mobile", "Clothes", "Sports", "Groceries", "Chairs"]
)
price = st.sidebar.number_input("Enter the price of the product: ")
if st.button("Submit"):
    st.write("Successfully your Products added")
    st.write(f"Product name: {name} \n Product Category: {category} \n Price : {price}" )