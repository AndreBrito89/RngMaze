from Items.Potion import Potion
from Items.Armor import Armor
from WeaponFactory import catalyst_generator
from WeaponFactory import melee_weapon_generator
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
            newArmorDefenseValue = 5
        case 'Silver':
            newArmorDefenseValue = 8
        case 'Gold':
            newArmorDefenseValue = 14
    newArmor = Armor(armorName, newArmorDefenseValue)
    return newArmor


######################
## creates a potion ##
######################
def potion_generator():
    #60% chance of beeing Large
    potionSizeValue = random.randint(1,10)
    potionSize = 'Large' if potionSizeValue > 4 else 'Small'

    #70% chance of beeing HP
    potionTypeValue = random.randint(1,10)
    potionType = 'HP' if potionTypeValue > 3 else 'SP'

    newPotion = Potion(potionSize, potionType)
    return newPotion


#####################
## creates a chest ##
#####################
def create_chest(playerClass):
    #70% potion
    #10% armor
    #20% weapon
    
    chestItemValue = random.randint(1,10)
    chestLoot =''
    #armor
    if (chestItemValue == 10):
        chestLoot = armor_generator(chest_armor_name_generator())
    #weapon
    elif (chestItemValue == 9 or chestItemValue == 8):
        if playerClass == 'Warrior' : 
            chestLoot = melee_weapon_generator('Chest')
        if playerClass == 'Mage':
            chestLoot = catalyst_generator('Chest')
        return chestLoot
    #potion
    else:      
        chestLoot = potion_generator()
        return chestLoot



###########################
## armor chest drop rate ##
###########################
def chest_armor_name_generator():
    
    armorRarityValue = random.randint(1,100)

    match armorRarityValue:
        #50% Leather
        case x if 1 <= x <= 50:
            newArmorName = 'Leather'
        #30% Iron
        case x if 51 <= x <= 80:
            newArmorName = 'Iron'
        #10% Bronze
        case x if 81 <= x <= 90:
            newArmorName = 'Bronze'
        #8% Silver
        case x if 91 <= x <= 98:
            newArmorName = 'Silver'
        #2% Gold
        case x if 99 <= x <= 100 :
            newArmorName = 'Gold'
    return newArmorName


###########################
## armor boss drop rate ##
###########################
def boss_armor_name_generator():

    armorRarityValue = random.randint(1,100)
    
    match armorRarityValue:
        #70% Bronze
        case x if 1 <= x <= 70:
            newArmorName = 'Bronze'
        #23% Silver
        case x if 71 <= x <= 93:
            newArmorName = 'Silver'
        #7% Gold
        case x if 94 <= x <= 100:
            newArmorName = 'Gold'
    return newArmorName