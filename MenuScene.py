from SceneBase import SceneBase
import pygame
black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
class MenuScene(SceneBase):
  def __init__(self):
    SceneBase.__init__(self)

  def Update(self):
    pass

  def Render(self, screen):
    screen.fill(black)
    self.createTitle(screen)
    pygame.display.update()

  def SwitchToScene(self, next_scene):
    self.next = next_scene

  def createTitle(self, screen):
    font = pygame.font.Font('freesansbold.ttf', 75)
    text = font.render("platformer", True, red,black)

    textRect = text.get_rect()
    textRect.center = (240,100)
    screen.blit(text,textRect)

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        from GameScene import GameScene
        self.SwitchToScene(GameScene())
        # put our game scene here 
        # from GameScene from GameScene
    