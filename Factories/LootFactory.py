from Items.Potion import Potion
from Items.Armor import Armor
from Factories.WeaponFactory import catalyst_generator
from Factories.WeaponFactory import melee_weapon_generator
import random


###################
## creates armor ##
###################
def armor_generator(armorName):
    
    match armorName:
        case 'Leather':
            newArmorDefenseValue = 1
        case 'Iron':
            newArmorDefenseValue = 2
        case 'Bronze':
            newArmorDefenseValue = 3
        case 'Silver':
            newArmorDefenseValue = 4
        case 'Gold':
            newArmorDefenseValue = 6
    return Armor(armorName, newArmorDefenseValue)
    


######################
## creates a potion ##
######################
def potion_generator():
    #60% chance of beeing Large
    potionSizeValue = random.randint(1,10)
    potionSize = 'Large' if potionSizeValue > 4 else 'Small'

    #80% chance of beeing HP
    potionTypeValue = random.randint(1,10)
    potionType = 'HP' if potionTypeValue > 2 else 'SP'

    return Potion(potionSize, potionType)


#####################
## creates a chest ##
#####################
def create_chest(playerClass):
    #70% potion
    #10% armor
    #20% weapon
    
    chestItemValue = random.randint(1,10)
    print(f"DEBUG: roll = {chestItemValue}")
    #potion
    if (chestItemValue < 8):
        chestLoot = potion_generator()
        return chestLoot 
    #weapon
    elif (chestItemValue == 9 or chestItemValue == 8):
        if playerClass == 'Warrior':
            chestLoot = melee_weapon_generator('Chest')
        if playerClass == 'Mage':
            chestLoot = catalyst_generator('Chest')
        return chestLoot
    #armor
    else:
        chestLoot = armor_generator(chest_armor_name_generator())
        return chestLoot
        
    
# creates a boss chest    
def create_boss_chest(playerClass):
    #65% weapon
    #35 armor
    bossChestItemValue = random.randint(1,100)
    if (bossChestItemValue > 35):
        if playerClass == "Warrior":
            bossDrop = melee_weapon_generator('Boss')
            return bossDrop
        if playerClass == "Mage":
            bossDrop = catalyst_generator('Boss')
            return bossDrop
    else:
        bossDrop = armor_generator(boss_armor_name_generator())
        return bossDrop



###########################
## armor chest drop rate ##
###########################
def chest_armor_name_generator():
    
    armorRarityValue = random.randint(1,100)

    match armorRarityValue:
        #50% Leather
        case x if 1 <= x <= 50:
            return 'Leather'
        #30% Iron
        case x if 51 <= x <= 80:
            return 'Iron'
        #10% Bronze
        case x if 81 <= x <= 90:
            return 'Bronze'
        #8% Silver
        case x if 91 <= x <= 98:
            return 'Silver'
        #2% Gold
        case x if 99 <= x <= 100 :
            return 'Gold'
    


###########################
## armor boss drop rate ##
###########################
def boss_armor_name_generator():

    armorRarityValue = random.randint(1,100)
    
    match armorRarityValue:
        #70% Bronze
        case x if 1 <= x <= 70:
            return 'Bronze'
        #23% Silver
        case x if 71 <= x <= 93:
            return 'Silver'
        #7% Gold
        case x if 94 <= x <= 100:
            return 'Gold'
    