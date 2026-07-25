#   table of dmg reduction for armors
#  +-----------------------------------------+
#  |Leather| Iron | Bronze | Silver |  Gold  |    
#  +-----------------------------------------+
#  |   1   |   2  |   3    |   4    |   6   |
#  +-----------------------------------------+
#   table of drop rate for armors
#  +-----------------------------------------+
#  |Leather| Iron | Bronze | Silver |  Gold  |    
#  +-----------------------------------------+
#  |  50%  | 30%  |  10%   |   8%   |   2%   | => CHEST
#  |   -%  |  -%  |  70%   |   23%  |   7%   | => BOSS
#  +-----------------------------------------+
class Armor:
    #constructor
    def __init__(self, armorName, armorDefenseValue):
        self.armorName = f"{armorName} armor"
        self.armorDefenseValue = armorDefenseValue
    
    