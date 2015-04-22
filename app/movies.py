import media

class Movie(media.Media):
  def __init__(self,title,storyline,image_url,imdb_id):
    media.Media.__init__(self,title,storyline,image_url)
    self.imdb_id = imdb_id

