import pygame
import math
import random

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))
# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyimg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(30, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(30)

# bullet
# ready- you can't see the bullet
# fire- the bullet is currently moving
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))


# collision detection
def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


#score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

#game over
over_font=pygame.font.Font("freesansbold.ttf",64)
def game_over_text(x,y):
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(x,y))

def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def player(x, y):
    screen.blit(playerimg, (x, y))


# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(no_of_enemies):
        #game over
        if enemyY[i]>=220:
            for j in range(no_of_enemies):
                enemyY[j]=1000
            game_over_text(200,250)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.7
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.7
            enemyY[i] += enemyY_change[i]

        # collision
        collision1 = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision1:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(30, 150)
        enemy(enemyX[i], enemyY[i],i)

    # bullet movement
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480

    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
