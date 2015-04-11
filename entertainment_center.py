#import movies
#import fresh_tomatoes
import tmdbsimple as tmdb
import omdb

tmdb.API_KEY = "27591dafb389ecb4d7c7bb206fbfe833"
movie_list = []
movie_info = []
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
  print(movie_info)

print(movie_list)

#fresh_tomatoes.open_movies_page(movie_list)
