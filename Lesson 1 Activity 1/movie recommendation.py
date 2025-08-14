import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

# Initialize colorama
init(autoreset=True)

# Function to load and preprocess dataset
def load_data(file_path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        # Combine Genre and Overview into one feature
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        sys.exit()

# Function to get user's mood
def get_user_mood():
    mood = input(Fore.GREEN + "How are you feeling today? ")
    sentiment = TextBlob(mood).sentiment.polarity
    if sentiment > 0:
        print(Fore.CYAN + "You seem to be in a positive mood! Let's find uplifting movies.")
    elif sentiment < 0:
        print(Fore.CYAN + "You seem to be in a thoughtful mood. Let's find something inspiring.")
    else:
        print(Fore.CYAN + "Neutral mood detected. Let's explore a mix of genres.")
    return sentiment

# Function to recommend movies
def recommend_movies(df, movie_title):
    if movie_title not in df['Series_Title'].values:
        print(Fore.RED + "Sorry, that movie is not in our database.")
        return

    # Vectorize the combined features
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix)

    # Find the movie index
    movie_index = df[df['Series_Title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity[movie_index]))

    # Sort by similarity
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print(Fore.YELLOW + "\nTop 5 recommended movies for you:")
    for i, score in sorted_scores[1:6]:
        print(f"{df.iloc[i]['Series_Title']} ({df.iloc[i]['Released_Year']}) - Genre: {df.iloc[i]['Genre']}")

# Main program
def main():
    df = load_data()

    print(Fore.MAGENTA + "🎬 Welcome to the AI Movie Recommendation System 🎬")
    time.sleep(1)

    sentiment = get_user_mood()
    time.sleep(1)

    movie_title = input(Fore.GREEN + "\nEnter a movie you like: ")
    recommend_movies(df, movie_title)

if __name__ == "__main__":
    main()
