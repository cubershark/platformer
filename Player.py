class Player():
  def __init__(self, screen) -> None:
    self.x = 240
    self.y = 180
    self.velocity_y = 0
    self.velocity_x = 0
    self.sprite = None
    self.screen = screen
  def move(self, x, scene):
    import pygame
    self.x += x
    self.y -= 3
    self.sprite = pygame.draw.rect(self.screen, "red",
                                  self.x, self.y, 50,50)
    for block in scene:
      if self.sprite.colliderect(block):
        self.x -= x
        self.sprite = pygame.draw.rect(self.screen, "red",
          self.x, self.y, 50,50)
# continue from here later    