import json, re

from spotipy.utils.menu_actions import clear_terminal

json_file_path = 'spotipy/data/artists.json'


data = json.load(open(json_file_path))
data = json.dumps(data)


class Song():
    def __init__(self, duration = 0, artistName = '-', songName = 'Undefined', genre = 'undefined', album  = 'undefined', **kwargs):
        super().__init__(**kwargs)
        self.duration = duration
        self.artisName = artistName
        self.songName = songName
        self.genre = genre
        self.album = album
        
        
    def search_song():
        clear_terminal()
        
        print("""\🔍 Search a song 🔍

[0] ⏪ Go back
              """)
        
        user_input = input('\nWhat do you want to hear? >_ ').lower()
     
        matches =  re.findall(r'\"title\": "(.+user_input.+)",\n\s+"duration"', data)
        
        print(matches)
           
        
        

