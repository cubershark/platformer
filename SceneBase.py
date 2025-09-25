class SceneBase():
  def __init__(self):
    self.next = self

  def Update(self):
    pass

  def ProcessInput(self, events, key_pressed):
    pass

  def Render(self,screen):
    pass

  def SwitchToScene(self, next_scene):
    self.next = next_scene

  def Terminate(self):
    self.SwitchToScene(None)