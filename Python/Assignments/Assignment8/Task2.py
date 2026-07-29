import streamlit as st
Product_price = st.number_input("Product Price: ")
discount = st.slider("Discount Percentage: ",0,50)
if st.button("Click here to calculate discounted price: "):
    discount_price = Product_price - (Product_price * discount / 100)
st.success(f"The discounted price is: ₹{discount_price:.2f}")