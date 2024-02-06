from spotipy.track import Track
from spotipy.playlist import Playlist
from spotipy.utils import menu_actions as actions
from spotipy.user import User


#TODO: 
# Heredar excepciones
# hacer uso del name = main
# hacer uso del str
# Implementar Try Exceptions and raisens

if __name__ == '__main__':
    actions.clear_terminal()
    
    
exe = True

actions.get_username()

while exe:
        option = input (f"""Good {actions.get_greeting_time()}
                        
📢📢 Welcome to Spotipy {User.username} 📢📢
          
[1] ✅ Playlists made for you
[2] 📚 Your library
[3] 📚 Create a Playlist
[4] 🔍 Search a song

[0] ⏪ Quit 

Insert an option >_ """)
    
        if option == '1':
            Playlist.show_default_playlist()
        elif option == '2':
            Playlist.show_playlist()
        elif option == '3':
            Playlist.create_playlist()
        elif option == '4':
            Track.search_track()
        elif option == '0':
            exe = False
            actions.clear_terminal()
            print(' Come back SOONg!💫\n')
        else:
            print('\n🚧 Incorrect input! Try it again! 🚧\n')
                
        actions.press_enter()    
        actions.clear_terminal()        
        
