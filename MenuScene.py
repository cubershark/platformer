from SceneBase import SceneBase
import pygame

black = pygame.Color(0,0,0)
red = pygame.Color(255,0,0)
blue = pygame.Color(0,0,255)
class MenuScene(SceneBase):
  def __init__(self):
    SceneBase.__init__(self)
    self.play_button = pygame.Rect(190,270,100,50)

  def Update(self):
    pass

  def Render(self, screen):
    screen.fill(black)
    self.createTitle(screen)
    self.create_button(screen)
    pygame.display.update()
  def SwitchToScene(self, next_scene):
    self.next = next_scene
    
  def create_button(self,screen):
    font2 = pygame.font.Font('freesansbold.ttf', 30)
    play_button = pygame.draw.rect(screen,red,self.play_button)
    play = font2.render("Play", True,blue )
    textRect2 = play.get_rect()
    textRect2.center = (240,290)
    screen.blit(play,textRect2)
  def createTitle(self, screen):
    font = pygame.font.Font('freesansbold.ttf', 75)
    text = font.render("platformer", True, red,black)

    textRect = text.get_rect()
    textRect.center = (240,100)
    screen.blit(text,textRect)
  def get_play_button(self):
    return self.play_button