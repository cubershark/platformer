import pygame
class GameScene():
    def __init__(self):
        self.selected_coins = []
        self.scene_row = 1
    
    def get_selected_coins(self):
        return self.selected_coins
    
    def append_coins(self,coin):
        self.selected_coins.append(coin)
    
    def clear_selected_coins(self):
        self.selected_coins.clear()

    def change_scene_row(self,x):
        self.scene_row += x

    def get_scene_row(self):
        return self.scene_row

    def remove_coin(self,coin):
        self.selected_coins.remove(coin)