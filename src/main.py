import pygame
import pygame_menu
from constants.constants import * 
from scenes.gameScreen import * 
from scenes.settings import *

def play(): 
    pygame_menu.events.EXIT
    startGame()

def settings():
    pygame_menu.events.EXIT
    openSettings()

def mainScreen():
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('BitClicker')
    menu = pygame_menu.Menu('Welcome', 420, 420, theme= pygame_menu.themes.THEME_DARK)
    menu.add.button('Play', play)
    menu.add.button('Settings', settings)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

if __name__ == "__main__":
    pygame.init()
    mainScreen()