class Song():
    def __init__(self, duration = 0, artistName = '-', songName = 'Undefined', genre = 'undefined', album  = 'undefined', **kwargs):
        super().__init__(**kwargs)
        self.duration = duration
        self.artisName = artistName
        self.songName = songName
        self.genre = genre
        self.album = album
        

