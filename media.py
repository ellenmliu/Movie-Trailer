import webbrowser

class Movie():
    """This class provides a way to store movies related information"""

    # Creating the init function of Movie
    def __init__(self, m_title, poster_image, trailer_url):
        self.title = m_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    # Opens the Youtube trailer link
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

