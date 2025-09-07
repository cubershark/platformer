import pygame


pygame.init()
screen = pygame.display.set_mode((480, 360))
clock = pygame.time.Clock()
running = True
dt = 0
velocity_y = 0
velocity_x = 0
gravity = -0.5
player_y = 180
player_x = 240
move_speed = 1.5
fall_tick = 0
scene_row = 1
scene_height = 1
scene_id = scene_row + scene_height * 100
print(scene_id)
blocks = [pygame.Rect(0,300,480,60),pygame.Rect(360,240,120,60),pygame.Rect(150,130,120,30),pygame.Rect(0,240,170,60),pygame.Rect(0,190,80,100),pygame.Rect(300,80,120,30)]
scene_101 = [pygame.Rect(0,300,480,60),pygame.Rect(360,240,120,60),pygame.Rect(150,130,120,30),pygame.Rect(0,240,170,60),pygame.Rect(0,190,80,100),pygame.Rect(300,80,120,30)]
def set_up(scene):
    pass
def fix_overlap():
    global velocity_y,player_y,fall_tick
    if velocity_y > 0:
        player_y -= velocity_y
        velocity_y = 0
        fall_tick = 0
    elif velocity_y < 0:
        player_y -= velocity_y
        velocity_y = 0
def move(x):
    global velocity_x,player_x,player_y
    player_x += x
    player_y -= 3
    player = pygame.draw.rect(screen, "red", (player_x,player_y,50,50))
    for block in blocks:
        if player.colliderect(block):
            player_x -= x
            player = pygame.draw.rect(screen, "red", (player_x,player_y,50,50))
            velocity_x = 0
    player_y += 3

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill("blue")

    velocity_x *= 0.6
    player = pygame.draw.rect(screen, "red", (player_x,player_y,50,50))
    floor = pygame.draw.rect(screen, "purple", (0,300,480,60))
    for block in blocks:
        pygame.draw.rect(screen, "purple", block)
    for block in blocks:
        if player.colliderect(block):
            fix_overlap()
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and fall_tick == 0:
        velocity_y = -10
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_LEFT]:
        velocity_x -= move_speed
    if keys[pygame.K_RIGHT]:
        velocity_x += move_speed
    velocity_y -= gravity

 
    pygame.display.flip()
    player_y += velocity_y
    move(velocity_x)
    fall_tick += 1

 
    dt = clock.tick(60) / 1000
    

pygame.quit()