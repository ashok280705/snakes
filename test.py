
import pygame as game
import random as r

# Define colors
class Colors:
    white = (255, 255, 255)
    pink = (255, 192, 203)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)

def update():
    game.display.update()

game.init()
game.mixer.init()

screenwidth = 800
screenheight = 750

game.display.set_caption('Snake Game'.upper())
gamewindow = game.display.set_mode((screenwidth, screenheight))

# Load images
bgimg = game.image.load('snakelawn.png')
bgimg = game.transform.scale(bgimg, (screenwidth, screenheight)).convert_alpha()

endimg = game.image.load('endpg.png')
endimg = game.transform.scale(endimg, (screenwidth, screenheight)).convert_alpha()

fps = 30  # Frames per second
font = game.font.SysFont(None, 80)
clock = game.time.Clock()

def text_screen(text, colour, x, y):
    screentext = font.render(text, True, colour)
    gamewindow.blit(screentext, [x, y])

def plot_game(gamewindow, colour, snake_list, size):
    for i, (x, y) in enumerate(snake_list):
        if i == len(snake_list) - 1:
            # Draw head of the snake in black
            game.draw.rect(gamewindow, Colors.black, [x, y, size, size])
        else:
            game.draw.rect(gamewindow, colour, [x, y, size, size])

def gameloop():
    global fps
    food_x = r.randint(150, 750)
    food_y = r.randint(150, 700)
    gamequit = False
    exitgame = False
    snakex = 45
    snakey = 200
    size = 20
    score = 0
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    snake_list = []
    snake_length = 1
    with open('highscore.txt', 'r') as f:
        highscore = f.read()
    while not exitgame:
        if gamequit:
            gamewindow.fill(Colors.white)
            gamewindow.blit(endimg, (0, 0))

            with open('highscore.txt', 'w') as f:
                f.write(str(highscore))

            for event in game.event.get():
                if event.type == game.QUIT:
                    exitgame = True
                if event.type == game.KEYDOWN:
                    if event.key == game.K_RETURN:
                        gameloop()
        else:
            for event in game.event.get():
                if event.type == game.QUIT:
                    exitgame = True
                if event.type == game.KEYDOWN:
                    if event.key == game.K_RIGHT:
                        snakex = snakex + init_velocity
                        velocity_x = 10
                        velocity_y = 0

                    if event.key == game.K_DOWN:
                        snakey = snakey + init_velocity
                        velocity_x = 0
                        velocity_y = 10

                    if event.key == game.K_LEFT:
                        snakex = snakex - init_velocity
                        velocity_x = -10
                        velocity_y = 0

                    if event.key == game.K_UP:
                        snakey = snakey - init_velocity
                        velocity_y = -10
                        velocity_x = 0
            snakex = snakex + velocity_x
            snakey = snakey + velocity_y
            if abs(snakex - food_x) < 12 and abs(snakey - food_y) < 12:
                game.mixer.music.load('beep.mp3')
                game.mixer.music.play()
                score = score + 10
                food_x = r.randint(150, 750)
                food_y = r.randint(150, 700)
                snake_length += 5
                if score > int(highscore):
                    highscore = score

            gamewindow.fill(Colors.pink)
            gamewindow.blit(bgimg, (0, 0))
            text_screen(str(score), Colors.white, 250, 30)
            text_screen(str(highscore), Colors.white, 367, 98)
            game.draw.rect(gamewindow, Colors.blue, [food_x, food_y, size, size])

            head = []
            head.append(snakex)
            head.append(snakey)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:len(snake_list) - 1]:
                game.mixer.music.load('explosion.mp3')
                game.mixer.music.play()
                gamequit = True
                print(gamequit)
            if (snakex < 0 or snakey < 0 or snakex > screenwidth or snakey > screenheight or snakey < 140):
                game.mixer.music.load('explosion.mp3')
                game.mixer.music.play()
                gamequit = True
            plot_game(gamewindow, Colors.red, snake_list, size)
        game.display.update()
        clock.tick(fps)

    game.quit()
    quit()

gameloop()