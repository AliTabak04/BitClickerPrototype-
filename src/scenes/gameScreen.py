#Importing necessary libraries with files 
import pygame_menu
import pygame.display
from constants.constants import *  
pygame.init()
screensize = pygame.display.list_modes()

#function starts game and opens full main game screen(responsive for the device)
def startGame(): 
    main_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    menu = pygame_menu.Menu('BitClicker', main_screen.get_width(), main_screen.get_height(), theme= pygame_menu.themes.THEME_DARK)
    menu.mainloop(main_screen)



