import pygame
class GameScene():
    def __init__(self):
        self.selected_coins = []
    def get_selected_coins(self):
        return self.selected_coins
    def append_coins(self,coin):
        self.selected_coins.append(coin)
    def clear_selected_coins(self):
        self.selected_coins.clear()