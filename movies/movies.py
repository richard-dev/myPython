import webbrowser

class Movie():
    """ This class provides a way to store movie related infromation"""
    VALIDRATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, posterImage, trailerYouTube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYouTube

    def show_trailer(self):
        """ Launch youtube with url """
        webbrowser.open(self.trailer_youtube_url)
