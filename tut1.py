import pygame as game 
import colours as c
game.init()
# for creating a window
gamewindow=game.display.set_mode((400,550)) #this is to display the actual/to create a gamming console
gamecaption=game.display.set_caption('first python programme'.upper())
# where 1000 is the width and 500 is the height
# setting a variable for the game
exit_game=False
quit_game=False

# creating an gamming loop for holding the Windows
while not exit_game:
    for event in game.event.get():
        if(event.type==game.QUIT):     #this is  to activate the quite button of the game/window
            exit_game=True
        if(event.type==game.KEYDOWN):
            if(event.type==game.K_RIGHT):
                print('hello')
game.quit()
quit