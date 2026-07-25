#   table of dmg value ranges for weapons
#  +--------------------------------------+
#  |======|Normal| Rare |Legendary|  God  |    
#  +--------------------------------------+
#  |mace  | 4-9  | 9-14 |  12-18  | 19-24 |
#  |axe   | 3-11 | 7-18 |  12-22  | 15-28 |
#  |pike  | 7-9  | 12-15|  16-19  | 22-25 |
#  |sword | 6-10 | 11-16|  14-20  | 21-26 |
#  +--------------------------------------+
# table of drop rate value for weapons
#  +---------------------------------------+
#  |======|Normal | Rare |Legendary|  God  |    
#  +---------------------------------------+
#  |chest | 70%  |  20%  |    9%   |   1%  |
#  |boss  |  -%  |  75%  |   20%   |   5%  |
#  +---------------------------------------+
class Melee:
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
                self.dmgModifier = 1.2
            case 'Legendary':
                self.dmgModifier = 1.4
            case 'God':
                self.dmgModifier = 1.6
            case _:
                self.dmgModifier = 0

