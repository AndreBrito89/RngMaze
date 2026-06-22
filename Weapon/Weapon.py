# mace
# axe
# pike
# sword
#dmg value ranges for weapons
    # normal = 5-10
    # rare = 9-15
    # legendary = 13-19
    # god = 19-24
class Weapon:
    def __init__(self, baseDamage, weaponRarity, weaponName):
        self.baseDamage = baseDamage
        self.weaponName = weaponName
        self.weaponRarity = weaponRarity
        self.rarity(weaponRarity)
        self.totaldmgValue = self.baseDamage * self.dmgModifier
    
    #checks weapon rarity to assign a dmg modifier
    def rarity(self, weaponRarity):
        match weaponRarity:
            case "Normal":
                self.dmgModifier = 1
            case "Rare":
                self.dmgModifier = 1.1
            case "Legendary":
                self.dmgModifier = 1.2
            case "God":
                self.dmgModifier = 1.5
            case _:
                self.dmgModifier = 0

