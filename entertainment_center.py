import movies
import fresh_tomatoes
import tmdbsimple as tmdb
import omdb
import re


tmdb.API_KEY = "27591dafb389ecb4d7c7bb206fbfe833"
movie_list = []
movie_info = []
title_list = []
plot_list = []
poster_list = []
imdb_id_list = []
movie_6 = []
top_6 = tmdb.Discover()
response = top_6.movie(page = 1, sort_by = "popularity.desc", year = 2015)



#Loop through results from The Movie Database site and set titles into an array for a future call
i = 0
while i < 6:
  #movie = movies.Movie(top_6.results[i]["id"],top_6.results[i]["title"],"A story of a boy and his toys","https://image.tmdb.org/t/p/w500/"+top_6.results[i]["poster_path"],"https://www.youtube.com/watch?v=vwyZH85NQC4")
  movie_list.append(top_6.results[i]['title'])
  i = i +1

for m in movie_list:
  movie_info = omdb.get(title=m, fullplot=True, tomatoes=True)
  url_clean = movie_info["poster"]
  poster_image_url = re.sub(r'(^\[)\w|(\])+g',"",url_clean)
  movie_6.append(movies.Movie(m,[movie_info["plot"]],poster_image_url,[movie_info["imdb_id"]]))
  # title_list.append([m])
  # plot_list.append([movie_info["plot"]])
  # poster_list.append([movie_info["poster"]])
  # imdb_id_list.append([movie_info["imdb_id"]])
# movie_z = zip(title_list,plot_list,poster_list,imdb_id_list)
# for movie in movie_z:
#   movie = movies.Movie(movie[0],movie[1],movie[2],movie[3])
#   movie_6.append(movie)

print(movie_6[1].image_url)
fresh_tomatoes.open_movies_page(movie_6)
