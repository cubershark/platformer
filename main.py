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

text = None
blocks = [
   
]
selected_spikes = []
selected_coins = []
list_scenes = []
list_coins = []
scenes = {1:[
             pygame.Rect(0, 300, 480, 60),
             pygame.Rect(360, 240, 120, 60),
             pygame.Rect(150, 130, 120, 30),
             pygame.Rect(0, 240, 170, 60),
             pygame.Rect(0, 190, 80, 100),
             pygame.Rect(300, 80, 120, 30)
         ],
         2:[pygame.Rect(0, 300, 480, 60),
            pygame.Rect(0, 240, 170, 60),
            pygame.Rect(260,150,70,150),
            pygame.Rect(260,220,140,100)]}
spikes = {1:[],2:[[(170,300),(215,260),(260,300)]],}

coins = {
    1:[[240,180]],
    2:[]
}

def create_eyes(x,y):
    pygame.draw.rect(screen,"white",(x + 5,y + 5, 15,20))
    pygame.draw.rect(screen,"white",(x + 30,y + 5, 15,20))
    pygame.draw.rect(screen,"black",(x + 10,y + 10, 5,10))
    pygame.draw.rect(screen,"black",(x + 35,y + 10, 5,10))

def set_up(id,x,y):
    global scenes,player_x,player_y,list_scenes,list_spikes,selected_coins,coins,list_coins
    if id in scenes:
        list_scenes = scenes[id]
        list_spikes = spikes[id]
        list_coins = coins[id]
        blocks.clear()
        selected_spikes.clear()
        selected_coins.clear()
        for list_scene in list_scenes:
            blocks.append(list_scene)
        for list_spike in list_spikes:
            selected_spikes.append(list_spike)
        for list_coin in list_coins:
            selected_coins.append(list_coin)
        print(selected_spikes)
        player_x = x
        player_y = y
set_up(scene_row,240,180)
print(selected_coins)
def fix_overlap():
    global velocity_y, player_y, fall_tick
    if velocity_y > 0:
        player_y -= velocity_y
        velocity_y = 0 #- velocity_y / 2
        fall_tick = 0
    elif velocity_y < 0:
        player_y -= velocity_y
        velocity_y = 0


def move(x):
    global velocity_x, player_x, player_y,scene_row
    player_x += x
    player_y -= 3
    player = pygame.draw.rect(screen, "red", (player_x, player_y, 50, 50))
    for block in blocks:
        if player.colliderect(block):
            player_x -= x
            player = pygame.draw.rect(screen, "red",
                                      (player_x, player_y, 50, 50))
            velocity_x = 0
    player_y += 3
    if player_x > 480:
        if scene_row + 1 in scenes:
            scene_row += 1
            set_up(scene_row,0,player_y)
        else:
            player_x += x
            velocity_x = 0
    if player_x < 0:
        if scene_row - 1 in scenes:
            scene_row -= 1
            set_up(scene_row,480,player_y)
        else:
            player_x -= x
            velocity_x = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    velocity_x *= 0.6
    player = pygame.draw.rect(screen, "orange", (player_x, player_y, 50, 50))
    create_eyes(player_x + velocity_x,player_y + velocity_y)
    for block in blocks:
        pygame.draw.rect(screen, "purple", block)
        if player.colliderect(block):
            fix_overlap()
    for selected_spike in selected_spikes:
        spike = pygame.draw.polygon(screen, "red",selected_spike)
        
        if player.colliderect(spike):
            set_up(1,240,180)
    for selected_coin in selected_coins:
        c = pygame.draw.ellipse(screen,(255,212,0),(240,180,40,50))
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