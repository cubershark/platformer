import pygame
class Player():
  
  def __init__(self, screen) -> None:
    self.x = 240
    self.y = 180
    self.velocity_y = 0
    self.velocity_x = 0
    self.sprite = None
    self.screen = screen
    self.gravity = -0.5
    self.fall_tick = 0
    
  def set_up_sprite(self):
    self.sprite = pygame.draw.rect(self.screen, "orange",(self.x, self.y, 50,50))

  def collide(self, object):
    if self.sprite is not None:
      return self.sprite.colliderect(object)
    else:
      return False
    
  def return_sprite(self):
    return self.sprite
    
  def get_x(self):
    return self.x
    
  def get_y(self):
    return self.y
    
  def update_xy(self, newX, newY):
    self.x = newX
    self.y = newY
    
  def update_vx_vy(self, new_vX, new_vY):
    self.velocity_x = new_vX
    self.velocity_y = new_vY

  def get_vel_x(self):
    return self.velocity_x
    
  def get_vel_y(self):
    return self.velocity_y

  def get_fall_tick(self):
    return self.fall_tick

  def set_fall_tick(self,x):
    self.fall_tick = x
  def move(self, x, scene):
    self.x += x
    self.y -= 3
    self.sprite = pygame.draw.rect(self.screen, "orange",
                                  (self.x, self.y, 50,50))
    self.sprite.colliderect
    for block in scene:
      if self.sprite.colliderect(block):
        self.x -= x
        self.sprite = pygame.draw.rect(self.screen, "orange",
          self.x, self.y, 50,50)
      

  
  def create_eyes(self,x, y, screen):
    pygame.draw.rect(screen,"white",(x + 5,y + 5, 15,20))
    pygame.draw.rect(screen,"white",(x + 30,y + 5, 15,20))
    pygame.draw.rect(screen,"black",(x + 10,y + 10, 5,10))
    pygame.draw.rect(screen,"black",(x + 35,y + 10, 5,10))
    # In the middle of moving gravity and fix overlap

# continue from here later    