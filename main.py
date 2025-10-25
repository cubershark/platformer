import pygame
from GameScene import GameScene
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
            pygame.Rect(260,150,70,150),
            pygame.Rect(260,220,140,100)],
         3:[pygame.Rect(0, 300, 480, 60)]}
spikes = {1:[],2:[[(190,300),(225,260),(260,300)]],3:[[(170,300),(190,270),(210,300)]]}


actualPlayer = Player(screen)
actualScene = GameScene()

def set_up(id, x, y):
    list_scenes = []
    list_coins = []
    list_spikes = []
    coins = {
        1:[(180,60,40,50)],
        2:[],
        3:[(210,190,40,50)]
    }
    
    list_scenes = scenes[id]
    list_spikes = spikes[id]
    list_coins = coins[id]
    blocks.clear()
    selected_spikes.clear()
    actualScene.clear_selected_coins()
    for list_scene in list_scenes:
        blocks.append(list_scene)
    for list_spike in list_spikes:
        selected_spikes.append(list_spike)
    for list_coin in list_coins:
        actualScene.append_coins(list_coin)
    actualPlayer.update_xy(x,y)
set_up(actualScene.get_scene_row(),240,180)

def fix_overlap():
    if actualPlayer.get_vel_y() > 0:
        actualPlayer.update_xy(actualPlayer.get_x(),actualPlayer.get_y() - actualPlayer.get_vel_y())
        actualPlayer.update_vx_vy(actualPlayer.get_vel_x(),0)
        actualPlayer.set_fall_tick(0)
    elif actualPlayer.get_vel_y() < 0:
        actualPlayer.update_xy(actualPlayer.get_x(),actualPlayer.get_y() - actualPlayer.get_vel_y())
        actualPlayer.update_vx_vy(actualPlayer.get_vel_x(),0)
        

def move(x):
    actualPlayer.update_xy(actualPlayer.get_x() + x,actualPlayer.get_y() -3)
    player = pygame.draw.rect(screen, "orange", (actualPlayer.get_x(), actualPlayer.get_y(), 50, 50))
    for block in blocks:
        if player.colliderect(block):
            actualPlayer.update_xy(actualPlayer.get_x() - x,actualPlayer.get_y())
            player = pygame.draw.rect(screen, "orange",
                                      (actualPlayer.get_x(), actualPlayer.get_y(), 50, 50))
          
            actualPlayer.update_vx_vy(0,actualPlayer.get_vel_y())
    actualPlayer.update_xy(actualPlayer.get_x(),actualPlayer.get_y() + 3)
    if actualPlayer.get_x() > 480:
        if actualScene.get_scene_row() + 1 in scenes:
            actualScene.change_scene_row(1)
            set_up(actualScene.get_scene_row(),0,actualPlayer.get_y())
        else:
            actualPlayer.update_xy(actualPlayer.get_x() + x,actualPlayer.get_y())
            actualPlayer.update_vx_vy(0,actualPlayer.get_vel_y())
    if actualPlayer.get_x() < 0:
        if actualScene.get_scene_row() - 1 in scenes:
            actualScene.change_scene_row(-1)
            set_up(actualScene.get_scene_row(),480,actualPlayer.get_y())
        else:
            actualPlayer.update_xy(actualPlayer.get_x() - x,actualPlayer.get_y())
            actualPlayer.update_vx_vy(0,actualPlayer.get_vel_y())

originalPlayer = Player(screen)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")
    text = font.render(f"score: {score}", True, red,black)
    textRect = text.get_rect()
    textRect.center = (60 + len(str(score)) * 8,30)
    screen.blit(text,textRect)
    actualPlayer.update_vx_vy(actualPlayer.get_vel_x() * 0.6,actualPlayer.get_vel_y())
    actualPlayer.set_up_sprite()
    actualPlayer.create_eyes(actualPlayer.get_x() + actualPlayer.get_vel_x(), actualPlayer.get_y() + actualPlayer.get_vel_y(), screen)
    for block in blocks:
        pygame.draw.rect(screen, "purple", block)
        if actualPlayer.collide(block):
            fix_overlap()
    for selected_spike in selected_spikes:
        spike = pygame.draw.polygon(screen, "red",selected_spike)
        
        if actualPlayer.collide(spike):
            actualScene.set_scene_row(1)
            set_up(actualScene.get_scene_row(),240,180)
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
    move(actualPlayer.get_vel_x())
    actualPlayer.set_fall_tick(actualPlayer.get_fall_tick() + 1)

    dt = clock.tick(60) / 1000

pygame.quit()

# #pretend game.py is real
# # import Game
# # if __name__ == "__main__":
# #     game = Game()
# #     game.runGame()

# import pygame
# from GameScene import GameScene
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