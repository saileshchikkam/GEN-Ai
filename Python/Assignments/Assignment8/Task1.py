# Task 1
import streamlit as st
st.title("Welcome to Streamlit")
name = st.text_input("Enter your name: ")
if st.button("Greet Me..."):
    st.write("Hello !"+name)

