import movies
import fresh_tomatoes
import tmdbsimple as tmdb
import rtsimple as rt

rt.API_KEY = "6ku8rtp252mu6r84yke6xrfa"
tmdb.API_KEY = "27591dafb389ecb4d7c7bb206fbfe833"
movie_list = []
top_6 = tmdb.Discover()
response = top_6.movie(page = 1, sort_by = "popularity.desc", year = 2015)



#Loop through results from The Movie Database site and set info to the movie object
i = 0
while i < 6:
  movie = movies.Movie(top_6.results[i]["id"],top_6.results[i]["title"],"A story of a boy and his toys","https://image.tmdb.org/t/p/w500/"+top_6.results[i]["poster_path"],"https://www.youtube.com/watch?v=vwyZH85NQC4")
  movie_list.append(movie)
  i = i +1

print(top_6.results)

#fresh_tomatoes.open_movies_page(movie_list)
