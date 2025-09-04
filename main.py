import pygame


pygame.init()
screen = pygame.display.set_mode((480, 360))
clock = pygame.time.Clock()
running = True
dt = 0
velocity_y = 0
gravity = -0.5
player_y = 180
player_x = 240

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill("blue")

    player = pygame.draw.rect(screen, "red", (player_x,player_y,50,50))
    floor = pygame.draw.rect(screen, "purple", (0,300,480,60))
    if player.colliderect(floor):
        pass
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    velocity_y -= gravity
 
    pygame.display.flip()
    player_y += velocity_y

 
    dt = clock.tick(60) / 1000
    

pygame.quit()