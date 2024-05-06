import pygame as game
import random as r
import os as o
import colours as c

game.mixer.init()

game.init()


# Creating window
screenwidth = 800
screenheight = 750
gameWindow = game.display.set_mode((screenwidth, screenheight))

#Background Image
bgimg = game.image.load("snakelawn.png")
bgimg = game.transform.scale(bgimg, (screenwidth, screenheight)).convert_alpha()

endimg=game.image.load('endpg.png')
endimg=game.transform.scale(endimg,(screenwidth,screenheight)).convert_alpha()
# Game Title
game.display.set_caption("SnakesWithHarry")
game.display.update()
clock = game.time.Clock()
font = game.font.SysFont(None, 80)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for i, (x, y) in enumerate(snk_list):
            if i == len(snk_list) - 1:
             # Draw head of the snake in black
                game.draw.rect(gameWindow, c.black, [x, y, snake_size, snake_size])
            else:
                game.draw.rect(gameWindow, color, [x, y, snake_size,snake_size])
def plot_head(gameWindow,color,head,snake_size):
    for x in range(0,2):
        game.draw.rect(gameWindow,color,[head[x],head[1],snake_size,snake_size])


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 200
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore file exists
    if(not o.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        highscore = f.read()
    food_x=r.randint(150,750)
    food_y=r.randint(150,700)
    score = 0
    init_velocity = 5
    size = 20
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(c.white)
            gameWindow.blit(endimg,(0,0))

            for event in game.event.get():
                if event.type == game.QUIT:
                    exit_game = True

                if event.type == game.KEYDOWN:
                    if event.key == game.K_RETURN:
                        gameloop()
                        
                if event.type == game.KEYDOWN:
                    if event.key == game.K_SPACE:
                        gameloop()
        else:

            for event in game.event.get():
                if event.type == game.QUIT:
                    exit_game = True

                if event.type == game.KEYDOWN:
                    if event.key == game.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == game.K_d:
                        velocity_x = init_velocity
                        velocity_y = 0
                    
                    if event.key == game.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                        
                    if event.key==game.K_a:
                        velocity_x= - init_velocity
                        velocity_y=0

                    if event.key == game.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                        
                    if event.key == game.K_w:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == game.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        
                    if event.key == game.K_s:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<12 and abs(snake_y - food_y)<12:
                game.mixer.music.load('beep.mp3')
                game.mixer.music.play( )
                score +=10
                food_x=r.randint(150,750)
                food_y=r.randint(150,700)
                snk_length +=5
                if score>int(highscore):
                    highscore = score
            
            gameWindow.fill(c.pink)
            gameWindow.blit(bgimg,(0,0))
            text_screen(str(score),c.white,250,30)
            text_screen(str(highscore),c.white,367,98)
            game.draw.rect(gameWindow,c.blue,[food_x,food_y,size,size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if head==snk_list:
                plot_snake(gameWindow,c.black,snk_list,size)
                
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                game.mixer.music.load('explosion.mp3')
                game.mixer.music.play()

            if snake_x<0 or snake_x>screenwidth or snake_y<0 or snake_y>screenheight or snake_y<140:
                game_over = True
                game.mixer.music.load('explosion.mp3')
                game.mixer.music.play()
            
            plot_snake(gameWindow, c.red, snk_list,size)
        game.display.update()
        clock.tick(fps)

    game.quit()
    quit()
gameloop()
