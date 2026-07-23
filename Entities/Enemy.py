# __________________________________________________
#|  STAGE 1 ENEMIES                                 |
#|__________________________________________________|
#| *rat => (12, 2, 0, 20) #hp, dmg, armor, xp       |
#| *skelleton => (19, 4, 0, 25) #hp, dmg, armor, xp |
#| *goblin => (21, 7, 1, 30) #hp, dmg, armor, xp    |
#| *lich => (69, 10, 3, 100) #hp, dmg, armor, xp    | => BOSS AT THE DOOR
#+--------------------------------------------------+
# __________________________________________________
#|  STAGE 2 ENEMIES                                 |
#|__________________________________________________|
#| *wolf => (14, 3, 0, 25) #hp, dmg, armor, xp      |
#| *zombie => (21, 6, 1, 30) #hp, dmg, armor, xp    |
#| *orc => (30, 8, 2, 35) #hp, dmg, armor, xp      |
#| *giant => (78, 12, 5, 140) #hp, dmg, armor, xp   | => BOSS AT THE DOOR
#+--------------------------------------------------+
# __________________________________________________
#|  STAGE 3 ENEMIES                                 |
#|__________________________________________________|
#| *bear => (16, 5, 2, 35) #hp, dmg, armor, xp      |
#| *wraith => (24, 8, 3, 40) #hp, dmg, armor, xp    |
#| *ogre => (38, 11, 5, 45) #hp, dmg, armor, xp     |
#| *dragon => (92, 18, 11, 200) #hp, dmg, armor, xp | => BOSS AT THE DOOR
#+--------------------------------------------------+

#TO DO
# Create a child class from enemy called `boss` with
# weapon drop that got better rarity rate. (7-3 => weapon/armor)
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
    