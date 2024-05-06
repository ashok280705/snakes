# this is the play button code
import pygame as game
import colours as c  
import random as r
game.init()
def update():
    game.display.update()
game.display.set_caption("SNAKE")
game.mixer.init
game.mixer.music.load('back.mp3')
game.mixer.music.play()
gamewindow=game.display.set_mode((800,750))
quit_game=False
clock=game.time.Clock()
play_image=game.image.load('snakeback.png')
play_image=game.transform.scale(play_image,(800,750)).convert_alpha()
def playgame():
    exit_game=False
    while not exit_game:
        mx,my=game.mouse.get_pos()
        gamewindow.fill(c.white)
        gamewindow.blit(play_image,(0,0))
        for event in game.event.get():
            if (event.type==game.QUIT):
                exit_game=True
            if ((mx,my)>=(300,284)and (mx,my)<(540,284)):
                if(event.type==game.MOUSEBUTTONDOWN):
                    if (game.mouse.get_pressed()[0]):
                        import snakegame
            update()
            clock.tick(60)
playgame()