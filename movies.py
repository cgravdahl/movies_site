import media

class Movie(media.Media):
  def __init__(self,media_id,title,storyline,image_url,trailer_youtube):
    media.Media.__init__(self,media_id,title,storyline,image_url)
    self.trailer_youtube_url = trailer_youtube
