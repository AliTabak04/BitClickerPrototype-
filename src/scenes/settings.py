#Importing necessary libraries with files 
import pygame
import pygame_menu
from constants.constants import * 

pygame.init()


#function to open settings and made necessary customisations to this menu
def openSettings():
    settings_screen = pygame.display.set_mode(window_size)
    settings_menu = pygame_menu.Menu('Settings', settings_screen.get_width(), settings_screen.get_height(), theme = pygame_menu.themes.THEME_DARK)
    settings_menu.add.selector('Currency Mode: ',[('Bits',1), ('Bytes',2)])
    settings_menu.add.selector('Select Theme: ',[('Dark',1), ('Light',2),('Solar',3), ('Blue',4)])
    settings_menu.add.button('Back')
    settings_menu.mainloop(settings_screen)



