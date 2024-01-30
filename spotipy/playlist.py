from  spotipy.song import Song

class Playlist(Song):
    #TODO: create variable to storage playlists
    playlists = []
    
    def __init__(self, name='MyPlaylist', likes=0, songsQty = 0, songs = [],**kwargs):
        super().__init__(*kwargs)
        self.name = name
        self._likes = likes
        self.songsQty = songsQty
        self.songs = songs
        
    def create_playlist(self):
        self.name = input('What will you name it ?')
        
        
    def show_playlist(self):
        pass
        
    def add_song(self, song):
        self.songs.append(song)
        self.songsQty += 1
        
    def rem_song(self, song):
        self.songs.remove(song)
        self.songsQty -= 1
        
    def set_like(self):
        self._likes += 1
        
    def get_likes(self):
        return self._likes
        
    