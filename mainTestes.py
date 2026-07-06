from Enemies.Enemy import Enemy
from Weapons.Catalyst import Catalyst
from Weapons.Melee import Melee
from Player.Player import Player
from Items.Potion import Potion
from Items.Armor import Armor
#rng
import random

MELEE_WEAPONS = ['Sword', 'Pike', 'Mace', 'Axe']
CATALYSTS_WEAPONS = ['Staff', 'Wand', 'Grimoire']

#############################################
############# RNG BASED  LOGIC ##############
#############################################


# STARTING GEAR
# CREATES STARTING MELEE WEAPON
def createStartingMeleeWeapon(weaponsList):
    startingWeaponDmg = 0

    #randomizes starting weapon
    startingWeaponName = random.choice(weaponsList)
    
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
def createStartingCatalystWeapon(weaponsList):
    startingCatalystDmg = 0

    #randomizes starting weapon
    startingCatalystName = random.choice(weaponsList)
    
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


# potion drop
def PotionGenerator():
    #60% chance of beeing Large
    potionSizeValue = random.randint(1,10)
    potionSize = 'Large' if potionSizeValue > 4 else 'Small'

    #70% chance of beeing HP
    potionTypeValue = random.randint(1,10)
    potionType = 'HP' if potionTypeValue > 3 else 'SP'

    newPotion = Potion(potionSize, potionType)
    return newPotion
#########################
## CHEST RELATED LOGIC ##
#########################
# creates a chest after battle
def createChest():
    #80% potion
    #10% armor
    #10% weapon
    print("Voce encontrou um bau!")
    chestItemValue = random.randint(1,10)
    chestLoot =''
    #armor
    if (chestItemValue == 10):
        chestLoot = chestArmorGenerator()
        print(f"O bau continha: {chestLoot.armorName} | Dano reduzido: {chestLoot.armorDefenseValue}")
    #weapon
    elif (chestItemValue == 9):    
        chestLoot = chestMeleeWeaponGenerator(MELEE_WEAPONS)
        print(f"O bau continha: {chestLoot.weaponName} | Dano base: {chestLoot.baseDamage} | Dano total: {chestLoot.totaldmgValue} | Raridade: {chestLoot.weaponRarity}")
        return chestLoot
    #potion
    else:      
        chestLoot = PotionGenerator()
        print(f'O bau continha: {chestLoot.potionName}. +{chestLoot.potionRegenPoints} {chestLoot.potionType}')
        return chestLoot
    
###################
## CHEST WEAPONS ##
###################
# GERERATES A RARITY FOR A CHEST WEAPON
def chestWeaponRarityGenerator():
    #assigns random rarity to a weapon
    weaponRarityValue = random.randint(1,100)
    newWeaponRarity
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
# CREATES A CATALYST WITH CHEST DROP RATES
def chestCatalystGenerator(weaponsList):
    newCatalystDmg = 0

    newCatalystName = random.choice(weaponsList)
    newCatalystRarity = chestWeaponRarityGenerator()

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

# CREATES A MELEE WEAPON WITH CHEST DROP RATES
def chestMeleeWeaponGenerator(weaponsList):
    
    newWeaponDmg = 0
    newWeaponName = random.choice(weaponsList)
    newWeaponRarity = chestWeaponRarityGenerator()
    
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
                    newWeaponDmg = random.randint(21,24)
        #maces
        case 'Mace':
            match newWeaponRarity:
                case 'Normal':
                    newWeaponDmg = random.randint(4,9)
                case 'Rare':
                    newWeaponDmg = random.randint(9,14)
                case 'Legendary':
                    newWeaponDmg = random.randint(14,18)
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
                    newWeaponDmg = random.randint(15,26)


    newWeapon = Melee(newWeaponDmg, newWeaponRarity, newWeaponName)
    return newWeapon

#CREATES NEW ARMOR WITH CHEST DROP RATES
def chestArmorGenerator():

        armorRarityValue = random.randint(1,100)
        match armorRarityValue:
            #50% Leather
            case x if 1 <= x <= 50:
                newArmorName = 'Leather'
            #20% rare
            case x if 51 <= x <= 80:
                newArmorName = 'Iron'
            #9% legendary
            case x if 81 <= x <= 90:
                newArmorName = 'Bronze'
            case x if 91 <= x <= 99:
                newArmorName = 'Silver'
            #1% god
            case 100 :
                newArmorName = "Gold"
        match newArmorName:
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
        newArmor = Armor(newArmorName, newArmorDefenseValue)
            

############################################
############# MAIN GAME LOGIC ##############
############################################

#create new player
def createNewPlayer():
    bonusPoints = 5
    # player name
    print("Digite seu nome:")
    playerNameInput = input()
    
    # player class
    while True:
        print("Selecione sua classe:")
        print("1 - Warrior")
        print("2 - Mage")
        newPlayerClass = input()    

        match newPlayerClass:
            
            case "1":
                newPlayerClass = 'Warrior'
                baseHp = 37
                baseSp = 15
                startingWeapon = createStartingMeleeWeapon(MELEE_WEAPONS)
                startingArmor = Armor('Leather', 1)
                baseAttack = 1
                break
            
            case "2":
                newPlayerClass = 'Mage'
                baseHp = 19
                baseSp = 24
                startingWeapon = createStartingCatalystWeapon(CATALYSTS_WEAPONS)
                startingArmor = Armor('No', 0)
                baseAttack = 4  
                break


    # bonus points
    print("Gostaria de usar os pontos extras em")
    print("1 - HP")
    print("2 - DMG")
    print("3 - SP")
    selectedBonusPoints = input()

    #                       Name            xp  lvl                  maxHP    hP      maxSP/sP equipedWeapon armor BA
    match selectedBonusPoints:
        case "1":
            totalHp = baseHp + bonusPoints
            player = Player (playerNameInput, 0, 1, newPlayerClass, totalHp, totalHp, baseSp, baseSp, startingWeapon, startingArmor, baseAttack) 

        case "2":
            totalBA = baseAttack + bonusPoints
            player = Player (playerNameInput, 0, 1, newPlayerClass, baseHp, baseHp, baseSp, baseSp, startingWeapon, startingArmor, totalBA) 
            

        case "3":
            totalSP = baseSp + bonusPoints
            player = Player (playerNameInput, 0, 1, newPlayerClass, baseHp, baseHp, totalSP, totalSP, startingWeapon, startingArmor, baseAttack) 
            

        case _:
            player = Player (playerNameInput, 0, 1, newPlayerClass, baseHp, baseHp, baseSp, baseSp, startingWeapon, startingArmor, baseAttack) 


    print(f"Jogador {player.name} criado com sucesso!")
    return player


#battle
def battle(player, enemy):
    while True:
        escapeState = ''
        
        print()
        print(f"Um {enemy.name} apareceu!")
        print(f"{player.name} HP: {player.healthPoints}/{player.maxHealthPoints}  |  SP: {player.sP}/{player.maxSP}")
        print(f"{enemy.name} HP: {enemy.healthPoints}/{enemy.maxHealthPoints}")
        print()
        print("O que deseja fazer?")
        print("1 - Attack")
        print("2 - Use item")
        print("3 - Attempt to escape")
        choice = input()
        
        # player attack
        if(int(choice) == 1):
            escapeState = False
            enemy.defend(player.attack())
            print(f"O jogador {player.name} atacou o {enemy.name} com {player.equipedWeapon.weaponName} e o dano foi: {player.attack()}")
            # enemy attack
            player.defend(enemy.attack())
            print(f"O {enemy.name} atacou o jogador! O dano recebido foi: {enemy.attackDmg}")
        # player uses item
        elif(int(choice) == 2):
            escapeState = False
            print("work in progress, cant use items yet")
        # attempts to escape
        elif(int(choice) == 3):
            escapeValue = random.randint(1,100)
            escapeState = player.escape(escapeValue)
            if(escapeState):
                print(f"{player.name} escapou!")
            else:
                print(f"Fuga mal sucedida, {enemy.name} errou seu ataque!")


        # after choosing option
        # checks if player successfully escaped
        if(escapeState):
            break
        # checks if player died
        if (player.healthPoints <= 0):
            print("Você morreu!")
            break
        # checks if enemy died
        if(enemy.healthPoints <= 0):
            print(f"O {enemy.name} morreu!")
            player.xpPoints += enemy.xpReward
            print(f"Voce recebeu {enemy.xpReward} xp.")
            print()
            createChest()
            break



# enemy
rato = Enemy('Rat', 12, 12, 3, 0, 20) #name, maxHp, hp, dmg, armor, xp
ogre = Enemy ('Ogre', 21, 21, 9, 1, 50)





# player
jogueidor = createNewPlayer()
print(f"Arma: {jogueidor.equipedWeapon.weaponName} | Dano base: {jogueidor.equipedWeapon.baseDamage} | Dano total: {jogueidor.equipedWeapon.totaldmgValue} | Raridade: {jogueidor.equipedWeapon.weaponRarity}")

# 1st battle simulation
battle(jogueidor, rato)

# weapon drop simulation
#arma = createNewWeapon()
#jogueidor.equipedWeapon = arma
#print("Voce encontrou uma nova arma!")
#print(f"Arma: {jogueidor.equipedWeapon.weaponName} | Dano base: {jogueidor.equipedWeapon.baseDamage} | Dano total: {jogueidor.equipedWeapon.totaldmgValue} | Raridade: {jogueidor.equipedWeapon.weaponRarity}")

# 2nd battle simulation
#battle(jogueidor, ogre)




# potion testing
#pocaoBau1 = chestPotionDrop()
#pocaoBau2 = chestPotionDrop()
#print(f'{pocaoBau1.potionName}. +{pocaoBau1.potionRegenPoints} {pocaoBau1.potionType} ')
#print(f'{pocaoBau2.potionName}. +{pocaoBau2.potionRegenPoints} {pocaoBau2.potionType} ')


# potion use simulation
#pocaoBau1 = chestPotionDrop()
#necessitado = Player('sofrido', 0, 1, 40, 20, 15, 10, Weapon(12,'Normal', 'consolo'), 1, 2)
#print(f"Jogador {necessitado.name} | {necessitado.healthPoints}/{necessitado.maxHealthPoints}HP| {necessitado.sP}/{necessitado.maxSP}SP")

#necessitado.usePotion(pocaoBau1)
#print('apos potion')
#print(f"Jogador {necessitado.name} | {necessitado.healthPoints}/{necessitado.maxHealthPoints}HP| {necessitado.sP}/{necessitado.maxSP}SP")