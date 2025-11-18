
class GameScene():
    def __init__(self):
        self.selected_coins = []
        self.scene_row = 1
        self.spikes = {1:[],2:[[(190,300),(225,260),(260,300)]],3:[[(150,300),(170,270),(190,300)],[(300,300),(320,270),(340,300)]]}
    
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
    
    def set_scene_row(self,x):
        self.scene_row = x
    
    def remove_coin(self,coin):
        self.selected_coins.remove(coin)

    def set_up(self, x, y, scenes, coins, blocks,selected_spikes,player):
        self.list_scenes = []
        self.list_coins = []
        self.list_spikes = []

        list_scenes = scenes[self.get_scene_row()]
        list_spikes = self.spikes[self.get_scene_row()]
        list_coins = coins[self.get_scene_row()]
        blocks.clear()
        selected_spikes.clear()
        self.clear_selected_coins()
        for list_scene in list_scenes:
            blocks.append(list_scene)
        for list_spike in list_spikes:
            selected_spikes.append(list_spike)
        for list_coin in list_coins:
            self.append_coins(list_coin)
        player.update_xy(x,y)