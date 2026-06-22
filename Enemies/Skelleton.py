from Enemies.Enemy import Enemy

class Skelleton(Enemy):
    #constructor
    def __init__(self):
        super().__init__(21, 6, 0, 35) #hp, dmg, armor, xp
    
    #defend
    def defend(self, dmgReceived):
        super().defend(dmgReceived)