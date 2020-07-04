import flask
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
import pandas as pd
import random

api_key = 'e5e135ca8f4f2ecfe0a67c9998a5441a'

app = flask.Flask(__name__, template_folder='templates')

df = pd.read_csv('./data/tmdb.csv')
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
df = df.reset_index()
indices = pd.Series(df.index, index=df['title'])
all_titles = [df['title'][i] for i in range(len(df['title']))]


def get_recommendations(title):
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    tit = df['title'].iloc[movie_indices]
    dat = df['release_date'].iloc[movie_indices]
    return_df = pd.DataFrame(columns=['Title', 'Year'])
    return_df['Title'] = tit
    return_df['Year'] = dat
    return return_df

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('index.html'))

    if flask.request.method == 'POST':
        yr = flask.request.form['year']
        rate = flask.request.form['rating']
        gen_l = []
        for e in flask.request.form:
            if e[0:2] == "g_":
                gen_l.append(flask.request.form[e])
        gen = ','.join(map(str,gen_l))
        if yr=="Should not be older than":
            yr = '1960'
        if not rate:
            rate = '3'
        if not gen:
            gen = '28,12,16'
        response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + api_key
                                + '&language=en-US&sort_by=popularity.desc&include_adult=true&include_video=false&page=1'
                                  '&primary_release_date.gte=' + yr
                                + '&vote_average.gte=' + rate
                                + '&with_genres=' + gen)
        result = response.json()
        movies = result['results']
        rand_movie = random.choice(movies)
        names = rand_movie['title']
        poster = rand_movie['poster_path']
        if names in all_titles:
            result_final = get_recommendations(names)
            m_names = []
            m_dates = []
            for i in range(len(result_final)):
                m_names.append(result_final.iloc[i][0])
                m_dates.append(result_final.iloc[i][1])
        print(m_names)
        print(m_dates)
        return flask.render_template('index2.html', movie_name=names, poster_path=poster, reco_movie=m_names, reco_date=m_dates)

if __name__ == '__main__':
    app.run()