import webbrowser

class Movie():
    def __init__(self, title, storyline, posterImage, trailerYouTube):
        self.title = title
        self.storyline = storyline
        self.posterImageUrl = posterImage
        self.trailerYouTubeUrl = trailerYouTube

    def showTrailer(self):
        webbrowser.open(self.trailerYouTubeUrl)
        