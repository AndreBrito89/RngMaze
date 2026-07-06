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
#| *wolf => (14, 4, 0, 25) #hp, dmg, armor, xp      |
#| *zombie => (21, 7, 1, 40) #hp, dmg, armor, xp    |
#| *orc => (32, 10, 2, 60) #hp, dmg, armor, xp      |
#| *giant => (72, 14, 5, 110) #hp, dmg, armor, xp   | => BOSS AT THE DOOR
#|---------------------------------------------------
# __________________________________________________
#|  STAGE 3 ENEMIES                                 |
#|__________________________________________________|
#| *bear => (16, 5, 2, 25) #hp, dmg, armor, xp      |
#| *wraith => (25, 8, 4, 45) #hp, dmg, armor, xp    |
#| * => (38, 11, 6, 65) #hp, dmg, armor, xp   |
#| *dragon => (80, 16, 11, 200) #hp, dmg, armor, xp | => BOSS AT THE DOOR
#|---------------------------------------------------

#TO DO
# Create a child class from enemy called `boss` with
# weapon drop that got better rarity rate. (7-3 => weapon/armor)
class Enemy:
    #constructor
    def __init__(self, name, maxHealthPoints, healthPoints, attackDmg, armor, xpReward):
        self.name = name
        self.maxHealthPoints = maxHealthPoints
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
    