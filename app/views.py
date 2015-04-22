from flask import render_template
from app import app
import movies
import tmdbsimple as tmdb
import omdb
import re
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
  current_date = str(datetime.now())
  tmdb.API_KEY = "27591dafb389ecb4d7c7bb206fbfe833"
  movie_6 = {}
  top_6 = tmdb.Discover()
  movie_list = []
  response = top_6.movie(page = 1, sort_by = "popularity.desc", year=2015)



  #Loop through results from The Movie Database site and set titles into an array for a future call
  i = 0
  while i < 6:
    movie_list.append(top_6.results[i]['title'])
    i = i +1

  #Takes titles from The Movie Database and uses the Open Movie database to get further info

  for m in movie_list:
    movie_info = omdb.get(title=m, fullplot=True, tomatoes=True)
    url_clean = movie_info["poster"]
    imdb_clean = movie_info["imdb_id"]
    imdb_id = re.sub(r'tt',"",imdb_clean)
    # trailers = requests.get('http://api.traileraddict.com/?imdb='+imdb_id+'&count=1&width=680')
    poster_image_url = re.sub(r'(^\[)\w|(\])+g',"",url_clean)
    movie_6.update({m:movies.Movie(m,[movie_info["plot"]],poster_image_url,imdb_id)})
  return render_template('index.html',
                         movie_tiles = movie_6)
