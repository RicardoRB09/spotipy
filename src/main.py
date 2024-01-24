import os
import song, playlist


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def press_enter():
    input('Press ENTER to continue >_ ')

if __name__ == '__main__':
    clear_terminal()
    
    
exe = True

while exe:
        option = input ("""📢📢 Welcome to Spotipy 📢📢
          
[1] 🔍 Search a song
[2] 📚 Your library

[0] ⏪ Quit 

Insert an option >_ """)
    
        if option == '1':
            print()
        elif option == '2':
            print()
        elif option == '0':
            exe = False
            print('\n💫 Come back SOONg!💫\n')
        else:
            print('\n🚧 Input incorrect! Try it again 🚧\n')
                
        press_enter()    
        clear_terminal()

