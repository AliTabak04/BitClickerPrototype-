# Importing necessary libraries with files 
import pygame_menu
import pygame.display
from constants.constants import *
pygame.init()
screensize = pygame.display.list_modes()

generation_speed = 1 
currency = 0
threshold = 100


mother_board = False
cpu = False 
gpu = False
power_supply = False
ram = False
percentage = 0

def displayPercentage():
    global percentage
    items_completed = sum([mother_board, cpu, gpu, power_supply, ram])
    total_items = 5  # Total number of items to be completed
    percentage = (items_completed / total_items) * 100
    percentage_assembled.set_title(f'Percentage of PC Assembled: {percentage}%')

def updateCurrencyLabel():
    global generation_speed
    global currency
    currency += generation_speed
    currency_shower.set_title(f'Bits Generated: {currency}')

def updateBoughtAndPriceLabels():
    global cpu_shop, gpu_shop, power_shop, ram_shop, motherboard_shop
    cpu_shop.set_title(f'Buy Cpu: {threshold} bits, Is It Bought {cpu}')
    gpu_shop.set_title(f'Buy Gpu {threshold} bits, Is It Bought {gpu}')
    power_shop.set_title(f'Buy Power Supply {threshold} bits, Is It Bought {power_supply}')
    ram_shop.set_title(f'Buy Ram {threshold} bits, Is It Bought {ram}')
    motherboard_shop.set_title(f'Buy MotherBoard {threshold} bits, Is It Bought {mother_board}')


def resetLabels():
    global threshold, cpu, gpu, power_supply, ram, mother_board
    cpu = False
    gpu = False
    power_supply = False
    ram = False
    mother_board = False
    threshold *= 2  # Double the threshold
    updateBoughtAndPriceLabels()
    displayPercentage()

def ramBought():
    global ram, currency
    if currency >= threshold:
        currency -= threshold
        ram = True
        displayPercentage()
        updateCurrencyLabel()
        updateBoughtAndPriceLabels()

def cpuBought():
   global cpu, currency
   if currency >= threshold:
        currency -= threshold
        cpu = True
        displayPercentage()
        updateCurrencyLabel()
        updateBoughtAndPriceLabels()

def motherboardBought():
   global currency, mother_board
   if currency >= threshold:
        currency -= threshold
        mother_board = True
        displayPercentage()
        updateCurrencyLabel()
        updateBoughtAndPriceLabels()

def powerBought():
    global power_supply, currency
    if currency >= threshold:
        currency -= threshold
        power_supply = True
        displayPercentage()
        updateCurrencyLabel()
        updateBoughtAndPriceLabels()

def gpuBought():
    global gpu, currency
    if currency >= threshold:
        currency -= threshold
        gpu = True
        displayPercentage()
        updateCurrencyLabel()
        updateBoughtAndPriceLabels()



def increaseBitSpeed():
    global generation_speed
    global percentage
    global cpu
    global gpu 
    global power_supply
    global ram
    global mother_board
    global threshold
    if cpu == True and gpu == True and mother_board == True and power_supply == True and ram == True:
        generation_speed += 1
        resetLabels()
    

def increaseBits():
    global currency
    global generation_speed
    currency +=  generation_speed
    currency_shower.set_title(f'Bits Generated: {currency}')


def backToMenu():
    pygame_menu.events.EXIT
    mainScreen()


#function starts game and opens full main game screen(responsive for the device)
def startGame(): 
    global currency_shower
    global motherboard_shop
    global ram_shop
    global cpu_shop
    global power_shop
    global gpu_shop
    global percentage_assembled
    main_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    menu = pygame_menu.Menu('BitClicker', main_screen.get_width(), main_screen.get_height(), theme= theme)
    generator_button = menu.add.button('Generate Bits',increaseBits)
    currency_shower = menu.add.label(f'Bits Generated {currency}')
    cpu_shop = menu.add.button(f'Buy Cpu: {threshold} bits, Is It Bought {cpu}',cpuBought)
    gpu_shop = menu.add.button(f'Buy Gpu {threshold} bits, Is It Bought {gpu}', gpuBought)
    power_shop = menu.add.button(f'Buy Power Supply {threshold} bits, Is It Bought {power_supply}',powerBought)
    ram_shop = menu.add.button(f'Buy Ram {threshold} bits, Is It Bought {ram}',ramBought)
    motherboard_shop = menu.add.button(f'Buy MotherBoard {threshold} bits, Is It Bought {mother_board}',motherboardBought)
    percentage_assembled = menu.add.label(f'Percentage of PC Assembled: {percentage}%')
    menu.add.button('Assemble The PC', increaseBitSpeed)
    menu.add.button('Back To Main Menu', backToMenu)

    menu.mainloop(main_screen)


def changeToDark():
    global theme 
    theme = theme_dark
    openSettings()
    startGame()
    mainScreen()

def changeToLight():
    global theme 
    theme = theme_light
    openSettings()
    startGame()
    mainScreen()


def changeToSolar():
    global theme
    theme = theme_solar
    openSettings()
    startGame()
    mainScreen()
 
def changeToBlue():
    global theme 
    theme = theme_blue
    openSettings()
    startGame()
    mainScreen()

selected_theme  = None
selected_currency = None

#function to open settings and made necessary customisations to this menu
def openSettings():
    settings_screen = pygame.display.set_mode(window_size)
    settings_menu = pygame_menu.Menu('Settings', settings_screen.get_width(), settings_screen.get_height(), theme = theme)

    #callback function to retireive selected index at theme selector 
    def handleThemeChange(selected_item, selected_index): 
        global selected_theme
        selected_theme = selected_index
    
    #settings apply function to apply settings made
    def apply():
        if selected_theme == 1:
            changeToDark()
        elif selected_theme == 2:
            changeToLight()
        elif selected_theme == 3: 
            changeToSolar()
        else:
            changeToBlue()
    
    #Initial theme indexing
    initial_theme_index = 1  # Default to Dark theme
    if theme == theme_light:
        initial_theme_index = 2
    elif theme == theme_solar:
        initial_theme_index = 3
    elif theme == theme_blue:
        initial_theme_index = 4
    
    theme_selector = settings_menu.add.selector('Select Theme: ',[('Dark',1), ('Light',2),('Solar',3), ('Blue',4)], onchange= handleThemeChange, default=initial_theme_index)
    settings_menu.add.button('Apply Settings', apply)
    settings_menu.add.button('Back', mainScreen)
    settings_menu.mainloop(settings_screen)
  

def settings():
    pygame_menu.events.EXIT
    openSettings() 

#Main Starter Menu built using pygame-menu library
def mainScreen():
    screen = pygame.display.set_mode(window_size)
    global theme 
    theme = theme.copy()
    pygame.display.set_caption('BitClicker')
    menu = pygame_menu.Menu('Welcome', 420, 420, theme= theme)
    menu.add.button('Play', startGame)
    menu.add.button('Settings', settings)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

# Calling mainScreen to start game (starts main starter screen)
if __name__ == "__main__":
    pygame.init()
    mainScreen()
