# 🎬 Movie Recommendation System
A content-based movie recommender built with Python, scikit-learn, and Streamlit. It uses TF-IDF vectorization and cosine similarity to recommend movies based on their overview, genres, keywords, cast, and director.

<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit">

# 📂 Project Structure

- MR_EDA.ipynb
- README.md
- app.py
- movies.pkl
- requirements.txt
- tfidf_vectorizer.pkl
- tmdb_5000_credits.csv
- tmdb_5000_movies.csv  


# ⚙️ Installation

Clone the repository:```git clone https://github.com/Chazgrey/Syntecxhub_Movie_Recommender.git
cd Syntecxhub_Movie_Recommender```

Install dependencies:``` bash pip install -r requirements.txt```

# ▶️ Running the App
Run the Streamlit app locally: streamlit run app.py

Open the local URL in your browser.

# 🎛️ Features

Content-based filtering using TF-IDF + Cosine Similarity.

Dropdown search with autocomplete for movie titles.

Adjustable slider for number of recommendations.

Displays similarity score, rating, and popularity.


# 📦 Requirements
streamlit pandas scikit-learn joblib requests

# 🚀 Deployment 
You can deploy this app easily on:

[Streamlit Cloud](https://streamlit.io/cloud)

# 🎯 Demo

Try the live app here:  
→ **[Movie Recommendation System](https://syntecxappmovierecommender-iqqm6dnfhw9hakmh7chprg.streamlit.app/)**

# 🛠️ Tech Stack

- **Python** 3.12+
- **scikit-learn** — model training & pipeline
- **joblib** — model serialization
- **Streamlit** — interactive web app
- **pandas** / **numpy**
