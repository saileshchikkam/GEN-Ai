import pandas as pd
import streamlit as st

st.write("Hello World")

st.title("Hello StreamLit ")

st.write("This is my first streamlit app")

st.header("Welcome to Streamlit")

st.text("This is plain text")

st.subheader("This is a Subheader")

## Buttons, Checkboxes and Sliders

if st.button("Click me !"):
    st.write("Button Click! ")

agree = st.checkbox("I agree")
if agree:
    st.write("You agrees, tq for approval")

level = st.slider("Select a Level : ",1,10,5)
st.write(f"Selected level is {level}")

# uploading file
uploadedfile = st.file_uploader("Upload a File",type=["csv","txt"])

if uploadedfile is not None:
    df = pd.read_csv()
    st.write(df.head())