import pygame
from GameScene import GameScene
from MenuScene import MenuScene
from Player import Player 

pygame.init()
screen = pygame.display.set_mode((480, 360))
clock = pygame.time.Clock()
running = True
dt = 0
gravity = -0.5
move_speed = 1.5
red = (255,0,0)
black = (0,0,0)
font = pygame.font.Font('freesansbold.ttf', 30)
score = 0
lives = 3
green_change = 0

blocks = [
   
]
selected_spikes = []
scenes = {1:[
             pygame.Rect(0, 300, 480, 60),
             pygame.Rect(360, 240, 120, 60),
             pygame.Rect(150, 130, 120, 30),
             pygame.Rect(0, 240, 170, 60),
             pygame.Rect(0, 190, 80, 100),
             pygame.Rect(300, 80, 120, 30)
         ],
         2:[pygame.Rect(0, 300, 480, 60),
            pygame.Rect(0, 240, 190, 60),
            pygame.Rect(260,170,70,150),
            pygame.Rect(260,240,140,100)],
         3:[pygame.Rect(0, 300, 480, 60),
           pygame.Rect(340,240,140,60)]}

spikes = {1:[],2:[[(190,300),(225,260),(260,300)]],3:[[(150,300),(170,270),(190,300)],[(300,300),(320,270),(340,300)]]}

coins = {
    1:[(180,60,40,50)],
    2:[],
    3:[(230,210,40,50)]
}

menu = MenuScene()
menu.Render(screen)
showMenu = True
while showMenu:
    for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
             if event.button == 1:
                 if menu.get_play_button().collidepoint(event.pos):
                    showMenu = False
    

actualPlayer = Player(screen)
actualScene = GameScene()
actualScene.set_up(240,180,scenes,coins,blocks,selected_spikes,actualPlayer)

originalPlayer = Player(screen)
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("blue")
    text = font.render(f"score: {score}", True, red,black)
    text2 = font.render(f"lives: {lives}",True,red,black)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect.center = (60 + len(str(score)) * 8,30)
    textRect2.center = (410 - len(str(score)) * 8,30)
    screen.blit(text,textRect)
    screen.blit(text2,textRect2)
    actualPlayer.update_vx_vy(actualPlayer.get_vel_x() * 0.6,actualPlayer.get_vel_y())
   
    actualPlayer.set_up_sprite()
    actualPlayer.create_eyes(actualPlayer.get_x() + actualPlayer.get_vel_x(), actualPlayer.get_y() + actualPlayer.get_vel_y(), screen)
    actualPlayer.set_green(actualPlayer.get_green() - green_change)
    if actualPlayer.get_green() < 150 and not green_change == 0:
        green_change -= 0.75
        print(green_change)
    else:
        actualPlayer.set_green(150)
        green_change = 0
    
    for block in blocks:
        pygame.draw.rect(screen, "purple", block)
        if actualPlayer.collide(block):
            actualPlayer.fix_overlap()
    for selected_spike in selected_spikes:
        spike = pygame.draw.polygon(screen, "red",selected_spike)
        
        if actualPlayer.collide(spike):
            
            if lives > 1:
                lives -= 1
                actualPlayer.update_vx_vy(actualPlayer.get_vel_x(),-10)
                green_change = 12
                print(green_change)
            else:
                lives = 3
                actualScene.set_scene_row(1)
                actualScene.set_up(240,180,scenes,coins,blocks,selected_spikes,actualPlayer)
                score = 0
    for selected_coin in actualScene.get_selected_coins():
        c = pygame.draw.ellipse(screen,(255,164,0),(selected_coin))
        pygame.draw.ellipse(screen,(255,212,0),(selected_coin),5)
        pygame.draw.rect(screen,(255,212,0),(selected_coin[0]+ 18.5,selected_coin[1] + 10,5,30))
        if actualPlayer.collide(c):
            actualScene.remove_coin(selected_coin)
            score += 1
        
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and actualPlayer.get_fall_tick() == 0:
        actualPlayer.update_vx_vy(actualPlayer.get_vel_x(),-10)
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_LEFT]:
        actualPlayer.update_vx_vy(actualPlayer.get_vel_x() - move_speed,actualPlayer.get_vel_y())
    if keys[pygame.K_RIGHT]:
        actualPlayer.update_vx_vy(actualPlayer.get_vel_x() + move_speed,actualPlayer.get_vel_y())
    actualPlayer.update_vx_vy(actualPlayer.get_vel_x(),actualPlayer.get_vel_y() - gravity)

    pygame.display.flip()
    actualPlayer.update_xy(actualPlayer.get_x(),actualPlayer.get_y() + actualPlayer.get_vel_y())
    actualPlayer.move(actualPlayer.get_vel_x(),blocks,scenes,coins,selected_spikes,actualScene,screen)
    actualPlayer.set_fall_tick(actualPlayer.get_fall_tick() + 1)

    dt = clock.tick(60) / 1000

pygame.quit()

# #pretend game.py is real
# # import Game
# # if __name__ == "__main__":
# #     game = Game()
# #     game.runGame()

# import pygame
# from MenuScene import MenuScene
# def run_game(width, height, fps, starting_scene):
#     pygame.init()
#     screen = pygame.display.set_mode((width, height))
#     clock = pygame.time.Clock()

#     current_scene = starting_scene

#     while current_scene != None:
#         pressed_keys = pygame.key.get_pressed() 
#         filtered_events = []
#         for event in pygame.event.get():
#             quit_attempt = False
#             if event.type == pygame.QUIT:
#                 quit_attempt = True
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     quit_attempt = True
#             if quit_attempt:
#                 current_scene.Terminate()
#             else:
#                 filtered_events.append(event)
#         current_scene.ProcessInput(filtered_events, pressed_keys)
#         current_scene.Update()
#         current_scene.Render(screen)
#         pygame.display.flip()
#         clock.tick(fps)
# run_game(480, 360,60, GameScene())