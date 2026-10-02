import streamlit as st
import nltk
import sklearn
import pandas as pd
import pickle
import joblib
## title
st.title("Movie Recommendation System")

with open('movies.pickle','rb') as m:
    movies = pickle.load(m)

similarity = joblib.load("similarity.joblib")

movie_names = movies['title'].values

## function output 5 recommended movies
def recommend(name_movie):

    movie_index = movies[movies['title'] == name_movie].index[0]

    recommendations = similarity[movie_index]

    movie_list = sorted(enumerate(recommendations),reverse=True,key = lambda x:x[1])[1:6]
    ## these are the index of the 5 recommended movies

    recommendation_movie_List = []
    for i in movie_list:
        recommendation_movie_List.append(movies.iloc[i[0]].title)
        # print(movies.iloc[i[0]].title) ## it will print the index location of the recommended movies
    return recommendation_movie_List

name_movie = st.selectbox("Enter the Movie Name",movie_names)

if st.button("Recommend"):
    r = recommend(name_movie)
    st.write("Recommended Movies are:")

    for i in r:
        st.write(i)