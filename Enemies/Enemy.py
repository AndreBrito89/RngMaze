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

import random

from Weapon.Weapon import Weapon
from game_balance import WEAPON_NAMES, WEAPON_ROLL_TABLE_BOSS


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
        # Prevent negative damage from healing the target.
        totalDmgReceived = max(0, dmgReceived - self.armor)
        self.healthPoints -= totalDmgReceived
        return totalDmgReceived


class Boss(Enemy):
    def drop_weapon(self, roll_value=None):
        if roll_value is None:
            roll_value = random.randint(0, 100)

        for minimum, maximum, rarity, damage_min, damage_max in WEAPON_ROLL_TABLE_BOSS:
            if minimum <= roll_value <= maximum:
                damage = random.randint(damage_min, damage_max)
                weapon_name = random.choice(WEAPON_NAMES)
                return Weapon(damage, rarity, weapon_name)

        raise ValueError(f"boss weapon roll outside table boundaries: {roll_value}")
    