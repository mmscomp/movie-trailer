import webbrowser


class Movie():
    def __init__(self, title, storyline, poster, trailer): #  constructor 
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self): #  A method to play the trailer of the movie
        webbrowser.open(self.trailer_youtube_url)
