from Enemies.Enemy import Enemy

class Rat(Enemy):
    #constructor
    def __init__(self):
        super().__init__(12, 3, 0, 20) #hp, dmg, armor, xp
    
    #defend
    def defend(self, dmgReceived):
        super().defend(dmgReceived)
