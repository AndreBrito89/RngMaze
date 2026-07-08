# base points for warrior class lvl 1   || base points for mage class lvl 1
#=======================================||=======================================
# - maxHealthPoints = 37                || - maxHealthPoints = 19
# - armor = 1                           || - armor = 0
# - base attack = 1                     || - base attack = 4
# - sp = 15                             || - sp = 24
ESCAPE_COST = 10

class Player:
    #CONSTRUCTOR
    def __init__(self, name, xpPoints, playerLevel, playerClass, maxHealthPoints, healthPoints, maxSP, sP, equipedWeapon, equipedArmor, baseAttack):
        self.name = name
        self.xpPoints = xpPoints
        self.playerLevel = playerLevel
        self.playerClass = playerClass
        self.maxHealthPoints = maxHealthPoints
        self.healthPoints = healthPoints
        self.maxSP = maxSP
        self.sP = sP
        self.baseAttack = baseAttack
        self.equipedWeapon = equipedWeapon
        self.equipedArmor = equipedArmor
    
    #FUNCTIONS
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
        if(self.sP < ESCAPE_COST):
            print("SP insuficientes para escapar!")
            return False
        
        self.sP -= ESCAPE_COST
        if(escapeAttemptValue < 36):
            return True
        else:
            return False
        
    #use potion function
    def use_potion(self, potion):
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
    def level_up(self, xpReceived):
        #kd a logica
        pass