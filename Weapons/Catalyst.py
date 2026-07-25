#   table of dmg value ranges for Catalysts
#  +-------------------------------------------+
#  |=========|Normal| Rare | Legendary |  God  |    
#  +-------------------------------------------+
#  |staff    | 8-11  | 15-17 |  21-24  | 24-28 |
#  |grimoire | 7-14  | 11-23 |  15-26  | 19-32 |
#  |wand     | 8-13  | 16-21 |  19-25  | 26-30 |
#  +-------------------------------------------+
# table of drop rate value for Catalysts
#  +---------------------------------------+
#  |======|Normal | Rare |Legendary|  God  |    
#  +---------------------------------------+
#  |chest | 70%  |  20%  |    9%   |   1%  |
#  |boss  |  -%  |  75%  |   20%   |   5%  |
#  +---------------------------------------+
class Catalyst:
    #constructor
    def __init__(self, baseDamage, weaponRarity, weaponName):
        self.baseDamage = baseDamage
        self.weaponName = weaponName
        self.weaponRarity = weaponRarity
        self.rarity_modifier_bonus(weaponRarity)
        self.totaldmgValue = self.baseDamage * self.dmgModifier
    
    #checks weapon rarity to assign a dmg modifier
    def rarity_modifier_bonus(self, weaponRarity):
        match weaponRarity:
            case 'Normal':
                self.dmgModifier = 1
            case 'Rare':
                self.dmgModifier = 1.3
            case 'Legendary':
                self.dmgModifier = 1.5
            case 'God':
                self.dmgModifier = 1.7
            case _:
                self.dmgModifier = 0

