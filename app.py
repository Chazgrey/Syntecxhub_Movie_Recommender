import streamlit as st
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# Load saved models
tfidf = joblib.load('tfidf_vectorizer.pkl')
movies = pd.read_pickle('movies.pkl')

# Recompute cosine similarity at startup
tfidf_matrix = tfidf.transform(movies['tags'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Create indices mapping
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim, top_n=10):
    if title not in indices:
        return pd.DataFrame({'Error': [f"Movie '{title}' not found in dataset."]})
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    movie_indices = [i[0] for i in sim_scores]
    
    result = movies[['title', 'vote_average', 'popularity']].iloc[movie_indices].copy()
    result['similarity'] = [round(s[1], 4) for s in sim_scores]
    return result.sort_values('similarity', ascending=False)

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Content-based filtering using TF-IDF + Cosine Similarity")

movie_name = st.selectbox("Choose a movie:", options=sorted(movies['title'].unique()))
top_n = st.slider("Number of recommendations:", 5, 20, 10)

if movie_name:
    recommendations = get_recommendations(movie_name, top_n=top_n)
    st.write(f"### Recommended Movies similar to **{movie_name}**:")
    st.dataframe(recommendations)