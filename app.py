import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Same Dataset as above
data = {
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'title': ['The Dark Knight', 'Avengers: Endgame', 'Inception', 'Toy Story', 'Finding Nemo', 'The Lion King', 'Interstellar', 'The Prestige', 'The Martian', 'Coco', 'Up', 'Monsters Inc', 'The Godfather', 'Pulp Fiction', 'Goodfellas'],
    'genres': ['Action Crime Drama', 'Action Adventure Sci-Fi', 'Action Adventure Sci-Fi', 'Animation Adventure Comedy', 'Animation Adventure Comedy', 'Animation Adventure Drama', 'Adventure Drama Sci-Fi', 'Drama Mystery Sci-Fi', 'Sci-Fi Adventure Drama', 'Animation Comedy Family', 'Animation Adventure Comedy', 'Animation Comedy Family', 'Crime Drama', 'Crime Drama', 'Crime Drama']
}
df = pd.DataFrame(data)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genres'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(movie_title):
    try:
        idx = df[df['title'] == movie_title].index[0]
        sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)
        movie_indices = [i[0] for i in sim_scores[1:4]]
        return df['title'].iloc[movie_indices].tolist()
    except:
        return ["Movie not found!"]

st.title("🎬 Movie Recommendation System")
st.write("This system suggests movies based on their genres.")

selected_movie = st.selectbox("Select a movie you like:", df['title'].values)

if st.button("Recommend"):
    recommendations = get_recommendations(selected_movie)
    st.subheader("Recommended for you:")
    for movie in recommendations:
        st.write(f"✅ {movie}")
