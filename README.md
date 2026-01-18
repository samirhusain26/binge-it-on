# Binge-It-On

Binge-It-On is a web application designed to help you decide what movie to watch next. It combines live data from the [The Movie Database (TMDB)](https://www.themoviedb.org/) API with a content-based recommendation engine powered by machine learning to suggest movies tailored to your preferences.

## Features

*   **Movie Generator**: Filter movies by minimum release year, minimum rating, and genre.
*   **Smart Recommendations**: If the generated movie is in our local dataset, the app uses **Cosine Similarity** and **CountVectorizer** (NLP) to recommend finding 10 other movies with similar plots, genres, and features.
*   **Fallback Recommendations**: If the movie is new or not in the local dataset, it provides top-rated related movies from TMDB.
*   **Rich Media**: Displays movie posters, overviews, and YouTube trailers for both the main pick and recommendations.

## Tech Stack

*   **Backend**: Python, Flask
*   **Data Processing**: Pandas, NumPy
*   **Machine Learning**: Scikit-Learn (Cosine Similarity, CountVectorizer)
*   **API**: TMDB API key
*   **Deployment**: Gunicorn (ready for Heroku/Cloud)

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd binge-it-on
    ```

2.  **Install dependencies**:
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Data Setup**:
    Ensure you have the `tmdb.csv` dataset in the `./data/` directory.

## Usage

1.  **Run the application**:
    ```bash
    python app.py
    ```

2.  **Access the App**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

3.  **Get Recommendations**:
    - Select a minimum year (e.g., "Should not be older than 2012").
    - Select a minimum rating (e.g., "7").
    - Choose your preferred genres.
    - Click the submit button to get your movie suggestion and recommendations!

## Project Structure

*   `app.py`: Main Flask application containing routes and logic for fetching data and calculating similarity.
*   `data/`: Contains the `tmdb.csv` dataset used for the recommendation engine.
*   `templates/`: HTML templates for the web interface (`index.html`, `index_reco.html`, etc.).
*   `requirements.txt`: List of Python dependencies.

## Acknowledgments

*   Movie data provided by [The Movie Database (TMDB)](https://www.themoviedb.org/).
