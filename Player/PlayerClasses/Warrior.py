# base points for warrior class lvl 1
# - maxHealthPoints = 37
# - armor = 1
# - base attack = 2
# - sp = 15
class Warrior:
    #constructor
    def __init__(self, maxHealthPoints, healthPoints, maxSP ,sP, equipedWeapon, equipedArmor, baseAttack):
        self.maxHealthPoints = maxHealthPoints
        self.healthPoints = healthPoints
        self.maxSP = maxSP
        self.sP = sP
        self.baseAttack = baseAttack
        self.equipedWeapon = equipedWeapon
        self.equipedArmor = equipedArmor
    
    #attack
    def attack(self):
        return self.equipedWeapon.totaldmgValue + self.baseAttack
    
    #defend
    def defend(self, dmgReceived):
        totalDmgReceived = dmgReceived - self.equipedArmor.armorDefenseValue
        self.healthPoints -= totalDmgReceived

    #escape function
    def escape(self, escapeAttemptValue):
        #lose stamina for a 35% chance
        #of escaping the fight to next node
        if(self.sP<10):
            print("SP insuficientes para escapar!")
            return False
        
        self.sP -= 10
        if(escapeAttemptValue<36):
            return True
        else:
            return False
        
    #use potion function
    def usePotion(self, potion):
        match potion.potionType:
            #Health potion
            case 'HP':
                self.healthPoints = min(
                self.healthPoints + potion.potionRegenPoints,
                self.maxHealthPoints)

            #Stamina potion
            case 'SP':
                self.sP = min(
                self.sP + potion.potionRegenPoints,
                self.maxSP)
    # lvl up
    def levelUp(self, xpReceived):
        #kd a logica
        pass
