#Importing necessary libraries with files 
import pygame.display
import pygame_menu
from constants.constants import * 
from scenes.gameScreen import * 
from scenes.settings import *


#function to start game and dive into main game screen(where main game logic is and played)
def play(): 
    pygame_menu.events.EXIT
    startGame()

#function to leave starter menu and visit settings
def settings():
    pygame_menu.events.EXIT
    openSettings()

#Main Starter Menu built using pygame-menu library
def mainScreen():
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('BitClicker')
    menu = pygame_menu.Menu('Welcome', 420, 420, theme=theme_dark)
    menu.add.button('Play', play)
    menu.add.button('Settings', settings)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

#Calling mainScreen to start game (starts main starter screen)
if __name__ == "__main__":
    pygame.init()
    mainScreen()