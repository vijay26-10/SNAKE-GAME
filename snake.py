import pygame
import random
import os
pygame.init()

# colors
red = (255, 0, 0)
black = (0, 0, 0)
blue = (135, 206, 235)
# screen size
screen_width = 500
sceen_height = 500
# to create a window
gameWindow = pygame.display.set_mode((screen_width, sceen_height))
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()

# background image
bgimg = pygame.image.load("snake.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, sceen_height)).convert_alpha()
bgimg1 = pygame.image.load("GAMEOVER.png")
bgimg1 = pygame.transform.scale(bgimg1, (screen_width, sceen_height)).convert_alpha()
gamewindow = pygame.image.load("main.png")
gamewindow = pygame.transform.scale(gamewindow, (screen_width, sceen_height)).convert_alpha()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

#  to display highscore
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

#  to plot snake
def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.circle(gameWindow, red, [x, y], snake_size, snake_size)


snk_list = []
snk_length = 1

# first screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(bgimg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)


# game loop
def gameloop():
    # game  variables
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    # check if highscore file exist,
    if (not os.path.exists("highscore.txt")):
        # to create a file to store highscore
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    # to plot food
    food_x = random.randint(10, 300)
    food_y = random.randint(10, 450)
    # to plot bonus food
    food_x1 = random.randint(0, 400)
    food_y1 = random.randint(0, 300)
    # initial score
    score = 0
    # bonus score
    bonusscore = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000)

    init_velocity = 5
    snake_size = 15
    food_size = 15
    food_size1 = 25
    fps = 30

    while not exit_game:
        # to save the highscore in a file
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.blit(bgimg1, (0, 0))
            # to display highscore at the end of the game
            text_screen("SCORE: " + str(score) + " HIGHSCORE: " + str(highscore), red, 100, 10)
            # for handling keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                    elif event.key == pygame.K_q:
                        exit()
        else:
            # keyboard events to move snake
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            # to plot food at random x,y position and to eat  it
            if abs(snake_x - food_x) < 17 and abs(snake_y - food_y) < 20:
                score += 10
                food_x = random.randint(0, screen_width / 2)
                food_y = random.randint(0, sceen_height / 2)
                snk_length += 5
                # to display highscore
                if score > int(highscore):
                    highscore = score

            # gameWindow.fill(white)
            gameWindow.blit(gamewindow, (0, 0))
            # to draw food
            pygame.draw.rect(gameWindow, blue, [food_x, food_y, food_size, food_size])
            # to create bonus
            for i in bonusscore:
                if score == i:
                    pygame.draw.rect(gameWindow, blue, [food_x1, food_y1, food_size1, food_size1])
                    if abs(snake_x - food_x1) < 17 and abs(snake_y - food_y1) < 20:
                        score += 20
                        food_x1 = random.randint(0, screen_width / 2)
                        food_y1 = random.randint(0, sceen_height / 2)
                        snk_length += 10

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
            # game over
            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > sceen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
        #     to update changes
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()




