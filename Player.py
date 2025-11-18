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
    self.green = 150
    
    
  def set_up_sprite(self):
    self.sprite = pygame.draw.rect(self.screen, (255,self.green,0),(self.x, self.y, 50,50))

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
    
  def set_green(self,value):
    self.green = value

  def get_green(self):
    return self.green
    
  def set_fall_tick(self,x):
    self.fall_tick = x

  def fix_overlap(self):
    if self.get_vel_y() > 0:
      self.update_xy(self.get_x(),self.get_y() - self.get_vel_y())
      self.update_vx_vy(self.get_vel_x(),0)
      self.set_fall_tick(0)
    elif self.get_vel_y() < 0:
      self.update_xy(self.get_x(),self.get_y() - self.get_vel_y())
      self.update_vx_vy(self.get_vel_x(),0)

  def move(self,x,blocks,scenes,coins,selected_spikes,actualscene,screen):
    self.update_xy(self.get_x() + x,self.get_y() -3)
    player = pygame.draw.rect(screen, "orange", (self.get_x(), self.get_y(), 50, 50))
    for block in blocks:
      if player.colliderect(block):
          self.update_xy(self.get_x() - x,self.get_y())
          player = pygame.draw.rect(screen, "orange",
                                    (self.get_x(), self.get_y(), 50, 50))
          self.update_vx_vy(0,self.get_vel_y())
    self.update_xy(self.get_x(),self.get_y() + 3)
    if self.get_x() > 430:
      if actualscene.get_scene_row() + 1 in scenes:
        actualscene.change_scene_row(1)
        actualscene.set_up(0,self.get_y(),scenes,coins,blocks,selected_spikes,self)
      else:
        self.update_xy(self.get_x() - x,self.get_y())
        self.update_vx_vy(0,self.get_vel_y())
    if self.get_x() < 0:
      if actualscene.get_scene_row() - 1 in scenes:
        actualscene.change_scene_row(-1)
        actualscene.set_up(430,self.get_y(),scenes,coins,blocks,selected_spikes,self)
      else:
        self.update_xy(self.get_x() - x,self.get_y())
        self.update_vx_vy(0,self.get_vel_y())
  
  def create_eyes(self,x, y, screen):
    pygame.draw.rect(screen,"white",(x + 5,y + 5, 15,20))
    pygame.draw.rect(screen,"white",(x + 30,y + 5, 15,20))
    pygame.draw.rect(screen,"black",(x + 10,y + 10, 5,10))
    pygame.draw.rect(screen,"black",(x + 35,y + 10, 5,10))
