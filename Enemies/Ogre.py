from Enemies.Enemy import Enemy

class Ogre(Enemy):
    #constructor
    def __init__(self):
        super().__init__(21, 9, 1, 50) #hp, dmg, armor, xp
    
    #defend
    def defend(self, dmgReceived):
        super().defend(dmgReceived)
