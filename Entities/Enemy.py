# __________________________________________________
#|  STAGE 1 ENEMIES                                 |
#|__________________________________________________|
#| *rat => (12, 2, 0, 20) #hp, dmg, armor, xp       |
#| *skelleton => (19, 3, 0, 25) #hp, dmg, armor, xp |
#| *goblin => (21, 4, 0, 30) #hp, dmg, armor, xp    |
#| *lich => (69, 6, 2, 160) #hp, dmg, armor, xp    | => BOSS AT THE DOOR
#+--------------------------------------------------+
# __________________________________________________
#|  STAGE 2 ENEMIES                                 |
#|__________________________________________________|
#| *wolf => (14, 3, 0, 25) #hp, dmg, armor, xp      |
#| *zombie => (21, 6, 1, 30) #hp, dmg, armor, xp    |
#| *orc => (30, 8, 2, 35) #hp, dmg, armor, xp      |
#| *giant => (78, 12, 5, 220) #hp, dmg, armor, xp   | => BOSS AT THE DOOR
#+--------------------------------------------------+
# __________________________________________________
#|  STAGE 3 ENEMIES                                 |
#|__________________________________________________|
#| *bear => (16, 7, 2, 35) #hp, dmg, armor, xp      |
#| *wraith => (24, 9, 2, 40) #hp, dmg, armor, xp    |
#| *ogre => (38, 11, 4, 45) #hp, dmg, armor, xp     |
#| *dragon => (92, 19, 9, 450) #hp, dmg, armor, xp | => BOSS AT THE DOOR
#+--------------------------------------------------+

class Enemy:
    #constructor
    def __init__(self, name, maxHealthPoints, attackDmg, armor, xpReward):
        self.name = name
        self.maxHealthPoints = maxHealthPoints
        self.healthPoints = maxHealthPoints
        self.attackDmg = attackDmg
        self.armor = armor
        self.xpReward = xpReward
    #attack
    def attack(self):
        return self.attackDmg
    #defend
    def defend(self, dmgReceived):
        totalDmgReceived = dmgReceived - self.armor
        self.healthPoints -= totalDmgReceived
    