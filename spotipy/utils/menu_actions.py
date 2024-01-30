import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def press_enter():
    input('Press ENTER to continue >_ ')