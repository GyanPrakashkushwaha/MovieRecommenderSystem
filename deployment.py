import streamlit as st
import pickle
import requests
from recommender.designs.remove_ import remove



st.set_page_config(page_title="Movie Recommender System", page_icon=":🎥:", layout="wide", initial_sidebar_state="expanded")

remove()

df = pickle.load(file=open('model\df.pkl', mode='rb'))
similarity = pickle.load(file=open('model\similarity.pkl', mode='rb'))

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=9a7dfef9409852a3eaf9fd8ce6402a34')
    data = response.json()
    print(data)
    return 'http://image.tmdb.org/t/p/w500' + data['poster_path']

def key(x):
    return x[1]

def recommend(movie):
    recommended_movies_posters = []
    recommended_movies = []

    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    top_10_movies = sorted(list(enumerate(distances)), reverse=True, key=key)[1:11]

    for i in top_10_movies:
        recommended_movies.append(df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(df.iloc[i[0]].id))

    return recommended_movies, recommended_movies_posters

st.title('Movie Recommender System')

movies_title = df['title'].values
selected_movie = st.selectbox(label='Select Movie title', options=movies_title)


if st.button('Recommend'):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text((names[0]))
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])









