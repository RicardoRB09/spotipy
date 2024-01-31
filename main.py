from spotipy.song import Song
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
          
[1] 🔍 Playlists made for you
[2] 📚 Your library
[3] 🔍 Search a song

[0] ⏪ Quit 

Insert an option >_ """)
    
        if option == '1':
            print()
        elif option == '2':
            print()
        elif option == '3':
            Song.search_song()
        elif option == '0':
            exe = False
            actions.clear_terminal()
            print(' Come back SOONg!💫\n')
        else:
            print('\n🚧 Incorrect input! Try it again! 🚧\n')
                
        actions.press_enter()    
        actions.clear_terminal()

