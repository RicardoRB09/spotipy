from spotipy.track import Track
from spotipy.data import tracks_samples
from spotipy.utils import menu_actions

pop = tracks_samples.pop_tracks
salsa = tracks_samples.salsa_tracks

class Playlist(Track):
    #TODO: create variable to storage playlists
    playlists = []

    def __init__(self, name='My Playlist', likes=0, songsQty = 0, songs = [],**kwargs):
        super().__init__(*kwargs)
        self.name = name
        self._likes = likes
        self.songsQty = songsQty
        self.songs = songs
    
    
    @staticmethod
    def show_default_playlist():
        menu_actions.clear_terminal()
        
        print('✅ Playlists made for you ✅\n')
        
        while True:
            opt = input("""Select your favorite:
                        
[1] 🎧 Pop & Work
[2] 🎺 Salsa Lovers 

[0] ⏪ Go back

Insert an option >_""")
                
            if (opt == '1'):
                menu_actions.clear_terminal()
                
                print('🎧 Pop & Work 🎧\n')
                
                for index, track in enumerate(pop, start=1) :
                    print(f'[{index}] {track["artist"]} - {track["title"]}')
                    
                track_index = int(input('\nSelect a track >_ '))
            
                is_listening = True
                
                while is_listening:
                    pop_opt = input(f"""\n🔉🔉Listening {pop[track_index-1]["artist"]} - {pop[track_index-1]["title"]} 🔉🔉

[1] ⏩ Next track
[2] ⏪ Previous track
[3] Add to a Playlist

[0] ⏪ Go back                      
                                    
Insert an option >_ """)
                    if(pop_opt == '1'):
                        track_index +=1
                    elif(pop_opt == '2'):
                        track_index -=1
                    elif(pop_opt == '0'):
                        menu_actions.clear_terminal()
                        is_listening = False
                    else:
                        print('🚧 Incorrect input! Try it again! 🚧\n')
                    
            elif (opt == '2'):
                for index, track in enumerate(tracks_samples.salsa_tracks, start=1) :
                    print(f'[{index}] {track["artist"]} - {track["title"]}')
                    
            elif (opt == '0'):
                break
                       
            else:
                menu_actions.clear_terminal()
                print('🚧 Incorrect input! Try it again! 🚧\n')
                    
        
    
    
   
    def create_playlist(self):
        self.name = input('What will you name it ? >_')
            

    def show_playlist(self, menu_opt):
        menu_actions.clear_terminal()
        
        if menu_opt == 1:
            pass
        
    def add_song(self, song):
        self.songs.append(song)
        self.songsQty += 1
        
    def remove_song(self, song):
        self.songs.remove(song)
        self.songsQty -= 1
        
    def set_like(self):
        self._likes += 1
        
    def get_likes(self):
        return self._likes
    
    
    

        
    