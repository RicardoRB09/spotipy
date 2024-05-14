import json

from utils.menu_actions import clear_terminal

json_file_path = 'data/artists.json'


data = json.load(open(json_file_path))
data = json.dumps(data)


class Track():
    def __init__(self, duration = 0, artistName = '-', trackName = 'Undefined', genre = 'undefined', album  = 'undefined', **kwargs):
        super().__init__(**kwargs)
        self.duration = duration
        self.artisName = artistName
        self.songName = trackName
        self.genre = genre
        self.album = album
        
    def search_track():
        clear_terminal()
        print('💰 Explore Premium 💰. Now 3 months free.')
        
#         print("""\🔍 Search a track 🔍

# [0] ⏪ Go back
#               """)
        
#         user_input = input('\nWhat do you want to listen? >_ ').lower()
     
#         matches =  re.findall(r'\"title\": "(.+user_input.+)",\n\s+"duration"', data)
        
#         print(matches)
           
        
        

