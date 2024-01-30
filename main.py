from spotipy.song import Song
from spotipy.utils import menu_actions as actions



#TODO: 
# Heredar excepciones
# hacer uso del name = main
# hacer uso del str
# Implementar Try Exceptions and raisens

if __name__ == '__main__':
    actions.clear_terminal()
    
    
exe = True

while exe:
        option = input ("""📢📢 Welcome to Spotipy 📢📢
          
[1] 🔍 Search a song
[2] 📚 Your library

[0] ⏪ Quit 

Insert an option >_ """)
    
        if option == '1':
            Song.search_song()
        elif option == '2':
            print()
        elif option == '0':
            exe = False
            print('\n💫 Come back SOONg!💫\n')
        else:
            print('\n🚧 Incorrect input! Try it again! 🚧\n')
                
        actions.press_enter()    
        actions.clear_terminal()

