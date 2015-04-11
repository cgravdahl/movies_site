import media

class TvShow(media.Media):
  def __init__(self,title,storyline,image_url):
    media.Media.__init__(self,title,storyline,image_url)
