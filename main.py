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
def fix_overlap():
    global velocity_y,player_y,fall_tick
    if velocity_y > 0:
        player_y += 0 - velocity_y
        velocity_y = -0.5
        fall_tick = 0
    else:
        player_y += velocity_y
        velocity_y = 0
def move(x):
    global velocity_x,player_x
    player_x += x
    
    # Check for screen boundary collisions
    if player_x < 0:  # Left wall
        player_x = 0
        velocity_x = 0
    elif player_x > 430:  # Right wall (480 - 50 pixel player width)
        player_x = 430
        velocity_x = 0
    
    # Check for floor and block collisions
    if player.colliderect(floor) or player.colliderect(block_1):
        if velocity_x > 1:
            player_x -= x
            velocity_x = 0
        if velocity_x < -1:
            player_x += x
            velocity_x = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill("blue")

    velocity_x *= 0.6
    player = pygame.draw.rect(screen, "red", (player_x,player_y,50,50))
    floor = pygame.draw.rect(screen, "purple", (0,300,480,60))
    block_1 = pygame.draw.rect(screen, "purple", (360,240,120,60))
    if player.colliderect(floor) or player.colliderect(block_1):
        fix_overlap()
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and fall_tick == 0:
        velocity_y = -10
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        velocity_x -= move_speed
    if keys[pygame.K_RIGHT]:
        velocity_x += move_speed
    velocity_y -= gravity

 
    pygame.display.flip()
    player_y += velocity_y
    fall_tick += 1
    move(velocity_x)

 
    dt = clock.tick(60) / 1000
    

pygame.quit()