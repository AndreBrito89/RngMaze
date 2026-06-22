# base points for warrior class lvl 1
# - maxHealthPoints = 37
# - armor = 1
# - base attack = 2
# - sp = 15
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
        totalDmgReceived = dmgReceived - self.armor
        self.healthPoints -= totalDmgReceived
    def escape(self, escapeAttemptValue):
        #lose stamina for a 35% chance
        #of escaping the fight to next node
        if(self.sP<13):
            print("SP insuficientes para escapar!")
            return False
        
        self.sP -= 10
        if(escapeAttemptValue<36):
            return True
        else:
            return False