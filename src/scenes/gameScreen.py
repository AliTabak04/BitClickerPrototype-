import pygame_menu
import pygame 
from constants.constants import *  
pygame.init()
screensize = pygame.display.list_modes()
def startGame(): 
    main_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #figured out how to do it however, this time we lost exit button due to making game screen full size. 
    menu = pygame_menu.Menu('BitClicker', main_screen.get_width(), main_screen.get_height(), theme= pygame_menu.themes.THEME_DARK)
    menu.mainloop(main_screen)



