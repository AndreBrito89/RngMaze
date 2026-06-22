# __________________________________________________
#|  STAGE 1 ENEMIES                                 |
#|__________________________________________________|
#| *rat => (12, 3, 0, 20) #hp, dmg, armor, xp       |
#| *skelleton => (19, 6, 0, 35) #hp, dmg, armor, xp |
#| *ogre => (21, 9, 1, 50) #hp, dmg, armor, xp      |
#| *lich => (69, 12, 4, 100) #hp, dmg, armor, xp    | => BOSS AT THE DOOR
#|---------------------------------------------------
# __________________________________________________
#|  STAGE 2 ENEMIES                                 |
#|__________________________________________________|
#| * => (14, 4, 0, 25) #hp, dmg, armor, xp       |
#| * => (21, 7, 1, 40) #hp, dmg, armor, xp |
#| * => (25, 10, 2, 60) #hp, dmg, armor, xp      |
#| *giant => (72, 14, 5, 110) #hp, dmg, armor, xp   | => BOSS AT THE DOOR
#|---------------------------------------------------
# __________________________________________________
#|  STAGE 3 ENEMIES                                 |
#|__________________________________________________|
#| * => (15, 5, 1, 25) #hp, dmg, armor, xp       |
#| * => (22, 8, 2, 45) #hp, dmg, armor, xp |
#| * => (27, 11, 4, 65) #hp, dmg, armor, xp      |
#| *dragon => (80, 16, 9, 200) #hp, dmg, armor, xp  | => BOSS AT THE DOOR
#|---------------------------------------------------

#TO DO
# Create a child class from enemy called `boss` with
# weapon drop that got better dmg and rarity rate.
class Enemy:
    #constructor
    def __init__(self, name, healthPoints, attackDmg, armor, xpReward):
        self.name = name
        self.healthPoints = healthPoints
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
    