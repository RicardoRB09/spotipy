from spotipy.track import Track
from spotipy.data import tracks_samples
from spotipy.utils import menu_actions
import random

pop = tracks_samples.pop_tracks
salsa = tracks_samples.salsa_tracks
mix = tracks_samples.mix

playlists = []

class Playlist(Track):
   
    def __init__(self, name='My Playlist', likes=0, tracksQty = 0, tracks = [], **kwargs):
        super().__init__(*kwargs)
        self.name = name
        self._likes = likes
        self.tracksQty = tracksQty
        self.tracks = tracks
     
    

    def show_default_playlist(self):
        menu_actions.clear_terminal()
        
        print('✅ Playlists made for you ✅\n')
        
        while True:
            opt = input("""Select your favorite:
                        
[1] 🎧 Pop & Work
[2] 🎺 Salsa Lovers 

[0] 👈 Go back

Insert an option >_ """)
                
            if (opt == '1'):
                menu_actions.clear_terminal()
                
                print('🎧 Pop & Work 🎧\n')
                
                self.show_tracks_samples('pop')
                    
                track_index = int(input('\nSelect a track >_ '))

                is_listening = True
                while is_listening:
                    pop_opt = input(f"""\n🔉🔉Listening {pop[track_index-1]["artist"]} - {pop[track_index-1]["title"]} 🔉🔉

[1] ⏩ Next track
[2] ⏪ Previous track
[3] Add to a Playlist

[0] 👈 Pause & Go back                      
                                    
Insert an option >_ """)
                    if(pop_opt == '1'):
                        track_index +=1
                        
                    elif(pop_opt == '2'):
                        track_index -=1
                        
                    elif(pop_opt == '3'):
                        if(len(playlists) == 0):
                            print()
                            menu_actions.no_playlist_message()
                        else: 
                            print('\n📚 Your Library 📚\n')
                            self.show_playlist_list()
                            opt = input('\nSelect the playlist >_ ')
                            playlists[int(opt)-1].add_track(pop[track_index-1])
                            print(f'\n 📣 {pop[track_index-1]['title']} was added successfully! 📣')
                           
                    elif(pop_opt == '0'):
                        menu_actions.clear_terminal()
                        is_listening = False
                        
                    else:
                        print('🚧 Incorrect input! Try it again! 🚧\n')
                        
            elif (opt == '2'):
                menu_actions.clear_terminal()
                
                print('🎺 Salsa Lovers 🎺\n')
                
                self.show_tracks_samples('salsa')
                    
                track_index = int(input('\nSelect a track >_ '))

                is_listening = True
                while is_listening:
                    pop_opt = input(f"""\n🔉🔉Listening {salsa[track_index-1]["artist"]} - {salsa[track_index-1]["title"]} 🔉🔉

[1] ⏩ Next track
[2] ⏪ Previous track
[3] Add to a Playlist

[0] 👈 Pause & Go back                      
                                    
Insert an option >_ """)
                    if(pop_opt == '1'):
                        track_index +=1
                        
                    elif(pop_opt == '2'):
                        track_index -=1
                        
                    elif(pop_opt == '3'):
                        if(len(playlists) == 0):
                            print()
                            menu_actions.no_playlist_message()
                        else: 
                            print('\n📚 Your Library 📚\n')
                            self.show_playlist_list()
                            opt = input('\nSelect the playlist >_ ')
                            playlists[int(opt)-1].add_track(salsa[track_index-1])
                            print(f'\n📣 {salsa[track_index-1]['title']} was added successfully! 📣')
                           
                    elif(pop_opt == '0'):
                        menu_actions.clear_terminal()
                        is_listening = False
                        
                    else:
                        print('🚧 Incorrect input! Try it again! 🚧\n')
                
            elif (opt == '0'):
                menu_actions.clear_terminal()
                break
            
            else:
                menu_actions.clear_terminal()
                print('🚧 Incorrect input! Try it again! 🚧\n')
                    
        
    def create_playlist(self):
        menu_actions.clear_terminal()
        
        name = input(f"""What will you name it?

[0] 👈 Go back                      
                                    
Insert an option >_ """)
        
        if(name == '0' or ''):
            menu_actions.clear_terminal()
        else:
            new_playlist = Playlist(name=name, tracks=[])
            
            print(f'\n📣 {name} was created successfully! Add tracks to it and ENJOY! 📣')
            
            playlists.append(new_playlist)
            

    def show_playlist(self):
        menu_actions.clear_terminal()
        
        if(len(playlists) == 0):
               menu_actions.no_playlist_message()
        else:
            print('📚 Your Library 📚\n\nSelect one:\n')
            
            self.show_playlist_list()
            
            select_playlist = True
            while select_playlist:
                opt = input("""
[0] 👈 Go back

Insert an option >_ """)
                
                if opt.isnumeric():
                    if (opt == '0'):
                        menu_actions.clear_terminal()
                        select_playlist = False
                    else:
                        if(int(opt) > 0 and int(opt) <= len(playlists)):
                            self.show_selected_playlist(int(opt) - 1)
                            select_playlist = False
                        else:
                            menu_actions.invalid_item_message()
                            self.show_playlist_list()
                               
                else:
                    menu_actions.clear_terminal()
                    menu_actions.incorrect_input_message()
                    select_playlist = False
            
                
    def show_selected_playlist(self, index):
        menu_actions.clear_terminal()
        self.load_random_likes(playlists[index])
        print(f'🎧🎧🎧🎧 {playlists[index].name} 🎧🎧🎧🎧\n')
        print(f'📀 Likes:    {playlists[index].get_likes()}')
        print(f'📀 # Tracks: {len(playlists[index].tracks)}')
        print(f'📀 Tracks:')
        if(len(playlists[index].tracks) == 0):
            print(f'          Add some tracks! Its Free!... yet!')  
        else:
            self.show_tracks_samples(opt='custom',playlist=playlists[index].tracks)
    
        while True:
                opt = input("""
[1] Add a track
[2] Remove a track                          
                            
[0] 👈 Go back

Insert an option >_ """)
                
                if (opt == '0'):
                    menu_actions.clear_terminal()
                    break
                elif (opt == '1'):
                    self.show_add_tracks_menu(index)
                elif (opt == '2'):
                    self.show_remove_tracks_menu(index)
                else:
                    pass    
    
    
    def show_playlist_list(self):
        for index, playlist in enumerate(playlists, start=1):
            print(f'[{index}] {playlist.name}')  
        
    
    def show_tracks_samples(self, opt, playlist=None):
        if opt == 'salsa':
            for index, track in enumerate(salsa, start=1) :
                print(f'[{index}] {track["artist"]} - {track["title"]}')
        elif opt == 'pop':
            for index, track in enumerate(pop, start=1) :
                print(f'[{index}] {track["artist"]} - {track["title"]}')
        elif opt == 'mix':
            for index, track in enumerate(mix, start=1) :
                print(f'[{index}] {track["artist"]} - {track["title"]}')
        elif opt == 'custom':
            print('')
            for index, track in enumerate(playlist, start=1) :
                print(f'   [{index}] {track["artist"]} - {track["title"]}')
        elif opt == 'custom_index':
            print('')
            for index, track in enumerate(playlist, start=1) :
                print(f'   {index}. {track["artist"]} - {track["title"]}')
        else:
            raise Exception(f'Sorry, there is not such {opt} option')
        
        
    def show_add_tracks_menu(self, index):
        menu_actions.clear_terminal()
        print(f'💿 Available Tracks 💿\n')
        self.show_tracks_samples('mix')
        track_index = int(input('\nSelect the track to add >_ '))
        playlists[index].add_track(mix[track_index-1])
        print(f'\n📣 {mix[track_index-1]['title']} was added successfully! 📣\n')
        print(f"📀 {playlists[index].name}'s tracks:")
        self.show_tracks_samples(opt='custom_index',playlist=playlists[index].tracks)    
    
    
    def show_remove_tracks_menu(self, index):
        self.show_tracks_samples(opt='custom_index', playlist=playlists[index].tracks)
        track_index = int(input('\nSelect the track to remove >_ '))
        playlists[index].remove_track(track_index-1)
        print(f'\n🔄 {mix[track_index-1]['title']} was removed successfully! 🔄\n')
        print(f"📀 {playlists[index].name}'s tracks:")
        self.show_tracks_samples(opt='custom_index',playlist=playlists[index].tracks)
            
            
    def load_random_likes(self, playlist):
        playlist._likes = random.randint(1, 1000)
        
    
    def add_track(self, track):
        self.tracks.append(track)
        self.tracksQty += 1
        
        
    def remove_track(self, track):
        self.tracks.pop(track)
        self.tracksQty -= 1
        
        
    def set_like(self):
        self._likes += 1
        
        
    def get_likes(self):
        return self._likes
    
    
    

        
    