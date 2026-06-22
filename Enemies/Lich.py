from Enemies.Enemy import Enemy
#BOSS
class Lich(Enemy):
    #constructor
    def __init__(self):
        super().__init__(69, 11, 4, 100) #hp, dmg, armor, xp
    
    #defend
    def defend(self, dmgReceived):
        super().defend(dmgReceived)
