from spotipy.track import Track
from spotipy.data import tracks_samples
from spotipy.utils import menu_actions

pop = tracks_samples.pop_tracks
salsa = tracks_samples.salsa_tracks

playlists = []

class Playlist(Track):
   
    

    def __init__(self, name='My Playlist', likes=0, songsQty = 0, songs = [], **kwargs):
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
                
                Playlist.show_tracks_samples('pop')
                    
                track_index = int(input('\nSelect a track >_ '))

                is_listening = True
                while is_listening:
                    pop_opt = input(f"""\n🔉🔉Listening {pop[track_index-1]["artist"]} - {pop[track_index-1]["title"]} 🔉🔉

[1] ⏩ Next track
[2] ⏪ Previous track
[3] Add to a Playlist

[0] ⏪ Pause & Go back                      
                                    
Insert an option >_ """)
                    if(pop_opt == '1'):
                        track_index +=1
                    elif(pop_opt == '2'):
                        track_index -=1
                    elif(pop_opt == '3'):
                    
                        if(len(playlists) == 0):
                            print('\n🚫 You dont have any playlist yet. Create one. 🚫\n')
                        else: 
                            print('Your Playlists:')
                            for playlist in playlists:
                                print(playlist)
                    elif(pop_opt == '0'):
                        menu_actions.clear_terminal()
                        is_listening = False
                    else:
                        print('🚧 Incorrect input! Try it again! 🚧\n')
            elif (opt == '2'):
                Playlist.show_tracks_samples('salsa')
            elif (opt == '0'):
                break
            else:
                menu_actions.clear_terminal()
                print('🚧 Incorrect input! Try it again! 🚧\n')
                    
        
    def create_playlist():
        menu_actions.clear_terminal()
        
        name = input(f"""What will you name it?

[0] ⏪ Go back                      
                                    
Insert an option >_ """)
        
        if(name == '0' or ''):
            pass
        else:
            new_playlist = Playlist(name=name)
            
            print(f'\n📣 {name} was created successfully! Add songs to it and ENJOY! 📣\n')
            
            playlists.append(new_playlist)
            

    def show_playlist():
        menu_actions.clear_terminal()
        
        if(len(playlists) == 0):
                print('\n🚫 You dont have any playlist yet. Create one. 🚫\n')
        else:
            print('📚 Your Library 📚\n\nSelect one:\n')
            
            for index, playlist in enumerate(playlists, start=1):
                print(f'[{index}] {playlist.name}')  
            
            selecting = True
            while selecting:
                opt = input("""
[0] ⏪ Go back

Insert an option >_""")
                
                if (opt == '0'):
                    selecting = False
                else:
                    Playlist.show_selected_playlist(int(opt) - 1)
            
                
    @staticmethod
    def show_selected_playlist(index):
        menu_actions.clear_terminal()
        
        print(f'🎧 {playlists[index].name} 🎧\n')
        
        selecting = True
        
        
        while selecting:
                opt = input("""
[1] Add a song
[2] Remove a song                          
                            
[0] ⏪ Go back

Insert an option >_""")
                
                if (opt == '0'):
                    selecting = False
                elif (opt == '1'):
                    selecting = False
                elif (opt == '2'):
                    selecting = False
                else:
                    pass    
    
    
    def show_tracks_samples(opt):
        if opt == 'salsa':
            for index, track in enumerate(tracks_samples.salsa_tracks, start=1) :
                print(f'[{index}] {track["artist"]} - {track["title"]}')
        elif opt == 'pop':
            for index, track in enumerate(pop, start=1) :
                print(f'[{index}] {track["artist"]} - {track["title"]}')
        else:
            raise Exception(f'Sorry, there is not such {opt} option')
            
        
    
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
    
    
    

        
    