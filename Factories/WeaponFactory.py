from Weapons.Melee import Melee
from Weapons.Catalyst import Catalyst
import random

MELEE_WEAPONS = ['Sword', 'Pike', 'Mace', 'Axe']
CATALYSTS_WEAPONS = ['Staff', 'Wand', 'Grimoire']

# STARTING GEAR
# CREATES STARTING MELEE WEAPON
def create_starting_melee_weapon():
    startingWeaponDmg = 0

    #randomizes starting weapon
    startingWeaponName = random.choice(MELEE_WEAPONS)
    
    #assigns random dmg value to the weapon
    match startingWeaponName:
        case 'Sword':
            startingWeaponDmg = random.randint(6,10)
        case 'Pike':
            startingWeaponDmg = random.randint(7,9)
        case 'Mace':
            startingWeaponDmg = random.randint(4,9)
        case 'Axe':
            startingWeaponDmg = random.randint(3,11)

    newWeapon = Melee(startingWeaponDmg,'Normal', startingWeaponName)
    return newWeapon

# CREATES STARTING CATALYST
def create_starting_catalyst_weapon():
    startingCatalystDmg = 0

    #randomizes starting weapon
    startingCatalystName = random.choice(CATALYSTS_WEAPONS)
    
    #assigns random dmg value to the weapon
    match startingCatalystName:
        case 'Staff':
            startingCatalystDmg = random.randint(8,11)
        case 'Wand':
            startingCatalystDmg = random.randint(8,13)
        case 'Grimoire':
            startingCatalystDmg = random.randint(7,14)

    newCatalyst = Catalyst(startingCatalystDmg,'Normal', startingCatalystName)
    return newCatalyst

############################
## CHEST WEAPON DROP RATE ##
############################
# GERERATES A RARITY FOR A CHEST WEAPON
def chest_weapon_rarity_generator():
    #assigns random rarity to a weapon
    weaponRarityValue = random.randint(1,100)
    newWeaponRarity = ''

    match weaponRarityValue:
        #70% normal
        case x if 1 <= x <= 70:
            newWeaponRarity = 'Normal'
        #20% rare
        case x if 71 <= x <= 90:
            newWeaponRarity = 'Rare'
        #9% legendary
        case x if 91 <= x <= 99:
            newWeaponRarity = 'Legendary'
        #1% god
        case 100 :
            newWeaponRarity = 'God'
    return newWeaponRarity

###########################
## BOSS WEAPON DROP RATE ##
###########################
# GERERATES A RARITY FOR A BOSS WEAPON
def boss_weapon_rarity_generator():
    #assigns random rarity to a weapon
    bossWeaponRarityValue = random.randint(1,100)
    newBossWeaponRarity = ''

    match bossWeaponRarityValue:
        #75% rare
        case x if 1 <= x <= 74:
            newBossWeaponRarity = 'Rare'
        #20% legendary
        case x if 75 <= x <= 95:
            newBossWeaponRarity = 'Legendary'
        #5% god
        case x if 96 <= x <= 100 :
            newBossWeaponRarity = 'God'
    return newBossWeaponRarity


# CREATES A NEW CATALYST
def catalyst_generator(dropSource):
    newCatalystDmg = 0

    newCatalystName = random.choice(CATALYSTS_WEAPONS)
    if dropSource == 'Boss': newCatalystRarity = boss_weapon_rarity_generator()
    elif dropSource == 'Chest': newCatalystRarity = chest_weapon_rarity_generator()
    else : newWeaponRarity = dropSource
    match newCatalystName:
        # staff
        case 'Staff':
            match newCatalystRarity:
                case 'Normal':
                    newCatalystDmg = random.randint(8,11)
                case 'Rare':
                    newCatalystDmg = random.randint(15,17)
                case 'Legendary':
                    newCatalystDmg = random.randint(21,24)
                case 'God':
                    newCatalystDmg = random.randint(24,28)
        # wands
        case 'Wand':
            match newCatalystRarity:
                case 'Normal':
                    newCatalystDmg = random.randint(8,13)
                case 'Rare':
                    newCatalystDmg = random.randint(16,21)
                case 'Legendary':
                    newCatalystDmg = random.randint(19,25)
                case 'God':
                    newCatalystDmg = random.randint(26,30)
        # grimoire
        case 'Grimoire':
            match newCatalystRarity:
                case 'Normal':
                    newCatalystDmg = random.randint(7,14)
                case 'Rare':
                    newCatalystDmg = random.randint(11,23)
                case 'Legendary':
                    newCatalystDmg = random.randint(15,26)
                case 'God':
                    newCatalystDmg = random.randint(19,32)
                    
    newCatalyst = Catalyst(newCatalystDmg, newCatalystRarity, newCatalystName)
    return newCatalyst

# CREATES A NEW MELEE WEAPON 
def melee_weapon_generator(dropSource):
    
    newWeaponDmg = 0
    newWeaponName = random.choice(MELEE_WEAPONS)
    if dropSource == 'Boss': newWeaponRarity = boss_weapon_rarity_generator()
    elif dropSource == 'Chest': newWeaponRarity = chest_weapon_rarity_generator()
    else : newWeaponRarity = dropSource
    
    
   #assigns random dmg based on rarity and name of the weapon           
    match newWeaponName:
        # swords
        case 'Sword':
            match newWeaponRarity:
                case 'Normal':
                    newWeaponDmg = random.randint(6,10)
                case 'Rare':
                    newWeaponDmg = random.randint(11,16)
                case 'Legendary':
                    newWeaponDmg = random.randint(14,20)
                case 'God':
                    newWeaponDmg = random.randint(21,26)
        # pikes
        case 'Pike':
            match newWeaponRarity:
                case 'Normal':
                    newWeaponDmg = random.randint(7,9)
                case 'Rare':
                    newWeaponDmg = random.randint(12,15)
                case 'Legendary':
                    newWeaponDmg = random.randint(16,19)
                case 'God':
                    newWeaponDmg = random.randint(22,25)
        #maces
        case 'Mace':
            match newWeaponRarity:
                case 'Normal':
                    newWeaponDmg = random.randint(4,9)
                case 'Rare':
                    newWeaponDmg = random.randint(9,14)
                case 'Legendary':
                    newWeaponDmg = random.randint(12,18)
                case 'God':
                    newWeaponDmg = random.randint(19,24)
        #axes
        case 'Axe':
            match newWeaponRarity:
                case 'Normal':
                    newWeaponDmg = random.randint(3,11)
                case 'Rare':
                    newWeaponDmg = random.randint(7,18)
                case 'Legendary':
                    newWeaponDmg = random.randint(12,22)
                case 'God':
                    newWeaponDmg = random.randint(15,28)


    newWeapon = Melee(newWeaponDmg, newWeaponRarity, newWeaponName)
    return newWeapon


