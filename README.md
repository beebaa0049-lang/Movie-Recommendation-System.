# 🎬 Movie Recommendation System

## 📌 Project Overview
This project is an intelligent recommendation system developed as part of the EncoderX Remote Internship. The system suggests movies to users based on the genre of a movie they select using a Content-Based Filtering approach.

## 🛠️ Technical Approach
- **Recommendation Logic:** Content-Based Filtering.
- **Vectorization:** I used `TfidfVectorizer` to convert text-based movie genres into numerical vectors.
- **Similarity Measure:** I used `Cosine Similarity` to calculate the mathematical distance between movies. Movies with similar genres have a higher similarity score and are recommended first.
- **Frontend Interface:** The system is wrapped in a user-friendly interface developed using `Streamlit`.

## 📊 Dataset
For this project, a **Custom User Preference Dataset** was used, containing a curated list of movies and their respective genres (e.g., Action, Sci-Fi, Animation, Crime Drama).

## 🚀 How to Run the Project
1. Clone this repository.
2. Install required libraries: 
   `pip install pandas scikit-learn streamlit`
3. Run the application:
   `streamlit run app.py`

## ✅ Evaluation
The system was evaluated by testing various movie inputs. For example, when selecting "The Dark Knight" (Action/Crime), the system correctly recommended other crime-drama movies, proving the effectiveness of the Cosine Similarity logic.

## 🛠️ Tools Used
- **Language:** Python
- **Libraries:** Pandas, Scikit-learn, Streamlit
- **Platform:** Google Colab, GitHub
