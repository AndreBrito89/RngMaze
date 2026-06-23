# base points for warrior class lvl 1
# - maxHealthPoints = 37
# - armor = 1
# - base attack = 2
# - sp = 15
from game_balance import ESCAPE_MIN_SP_REQUIRED, ESCAPE_SP_COST, ESCAPE_SUCCESS_ROLL_MAX


class PlayerClassWarrior:
    #constructor
    def __init__(self, maxHealthPoints, healthPoints, maxSP ,sP, equipedWeapon, armor, baseAttack):
        self.maxHealthPoints = maxHealthPoints
        self.healthPoints = healthPoints
        self.maxSP = maxSP
        self.sP = sP
        self.baseAttack = baseAttack
        self.equipedWeapon = equipedWeapon
        self.armor = armor
    #attack
    def attack(self):
        return self.equipedWeapon.totaldmgValue + self.baseAttack
    #defend
    def defend(self, dmgReceived):
        # Prevent negative damage from healing the target.
        totalDmgReceived = max(0, dmgReceived - self.armor)
        self.healthPoints -= totalDmgReceived
        return totalDmgReceived
    def escape(self, escapeAttemptValue):
        #lose stamina for a 35% chance
        #of escaping the fight to next node
        if(self.sP < ESCAPE_MIN_SP_REQUIRED):
            print("SP insuficientes para escapar!")
            return False
        
        self.sP -= ESCAPE_SP_COST
        if(escapeAttemptValue <= ESCAPE_SUCCESS_ROLL_MAX):
            return True
        else:
            return False