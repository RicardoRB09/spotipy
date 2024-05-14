from playlist import Playlist
from track import Track
from user import User
from utils import menu_actions as actions


if __name__ == '__main__':
    actions.clear_terminal()
    
    
exe = True

actions.get_username()

playlist = Playlist()

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
            playlist.show_default_playlist()
        elif option == '2':
            playlist.show_playlist()
        elif option == '3':
            playlist.create_playlist()
        elif option == '4':
            Track.search_track()
        elif option == '0':
            exe = False
            actions.clear_terminal()
            print('✌ ✌ ✌  Come back soon  ✌ ✌ ✌')
        else:
            actions.incorrect_input_message()
                
        actions.press_enter()    
        actions.clear_terminal()        
        
