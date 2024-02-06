import os
from datetime import datetime, time
from spotipy.user import User


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def press_enter():
    input('\nPress ENTER to continue >_ ')
    

def get_username():
    clear_terminal()
    User.username = input('Whats your name? >_ ')
    clear_terminal()
    
    
def get_greeting_time():
    now = datetime.now().time()
    
    if (now >= time(5,00)) and (now <= time(11,59)):
        return 'Morning!!! 🌞'
    
    if (now >= time(12,00)) and (now <= time(16,59)):
        return 'Afternoon!!! 🌗'
    
    if ((now >= time(17,00)) or (now <= time(4,59))):
        return 'Evening!!! 🌙'

