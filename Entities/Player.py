# base points for warrior class lvl 1   || base points for mage class lvl 1
#=======================================||=======================================
# - maxHealthPoints = 37                || - maxHealthPoints = 19
# - armor = 1                           || - armor = 0
# - base attack = 1                     || - base attack = 4
# - sp = 15                             || - sp = 24
ESCAPE_COST = 10
MAX_POTIONS = 5
class Player:
    #CONSTRUCTOR
    def __init__(self, name, xpPoints, playerLevel, playerClass, maxHealthPoints, healthPoints, maxSP, sP, equippedWeapon, equippedArmor, baseAttack):
        self.name = name
        #stats
        self.xpPoints = xpPoints
        self.playerLevel = playerLevel
        self.playerClass = playerClass
        self.maxHealthPoints = maxHealthPoints
        self.healthPoints = healthPoints
        self.maxSP = maxSP
        self.sP = sP
        self.baseAttack = baseAttack
        #inventory
        self.equippedWeapon = equippedWeapon
        self.equippedArmor = equippedArmor
        self.inventoryArmor = None
        self.inventoryWeapon = None
        self.potions = []
        self.hasKey = False
    #FUNCTIONS
    #attack
    def attack(self):
        return self.equippedWeapon.totaldmgValue + self.baseAttack
    
    #defend
    def defend(self, dmgReceived):
        totalDmgReceived = dmgReceived - self.equippedArmor.armorDefenseValue
        if totalDmgReceived <= 0:
            print(f"Sua {self.equippedArmor.armorName} absorveu o dano recebido!")
            return
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
    # swaps inventory weapon and equipped weapon
    def swap_weapons(self):
        self.equippedWeapon, self.inventoryWeapon = ( self.inventoryWeapon, self.equippedWeapon)
    
    # swaps inventory armor and equipped amor
    def swap_armors(self):
        self.equippedArmor, self.inventoryArmor = (self.inventoryArmor, self.equippedArmor)

    # checks for available slots
    def has_weapon_slot(self):
        return self.inventoryWeapon is None
    
    def has_armor_slot(self):
        return self.inventoryArmor is None
    
    def has_potion_slot(self):
        return len(self.potions) < MAX_POTIONS

    # lvl up
    def level_up(self, xpReceived):
        #kd a logica
        pass
