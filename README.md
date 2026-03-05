🎬 Movie Recommendation SystemA content-based movie recommender built with Python, scikit-learn, and Streamlit. It uses TF-IDF vectorization and cosine similarity to recommend movies based on their overview, genres, keywords, cast, and director.

📂 Project Structuremovie-recommender/ │ ├── app.py                  # Streamlit webapp ├── movies.pkl              # Saved dataframe with metadata ├── tfidf_vectorizer.pkl    # Saved TF-IDF model ├── cosine_similarity.pkl   # Saved similarity matrix ├── requirements.txt        # Dependencies └── README.md               # Project documentation

⚙️ Installation

Clone the repository:git clone https://github.com/YourUsername/movie-recommender.git cd movie-recommender

Install dependencies:pip install -r requirements.txt

▶️ Running the AppRun the Streamlit app locally:streamlit run app.pyOpen the local URL (usually http://localhost:8501) in your browser.

🎛️ Features

Content-based filtering using TF-IDF + Cosine Similarity.

Dropdown search with autocomplete for movie titles.

Adjustable slider for number of recommendations.

Displays similarity score, rating, and popularity.

Fetches movie posters dynamically using the TMDB API.

🖼️ Movie PostersThis app integrates with the TMDB API to fetch movie posters.

Get your API key from TMDB.

Add it to app.py:API_KEY = "YOUR_TMDB_API_KEY"

📦 Requirementsstreamlit pandas scikit-learn joblib requests

🚀 DeploymentYou can deploy this app easily on:

Streamlit Cloud → streamlit.io/cloud

Hugging Face Spaces → huggingface.co/spaces

📸 Screenshots(Add screenshots of your app running locally with recommendations and posters)