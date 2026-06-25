from Enemies.Enemy import Enemy
from Player.PlayerClasses.Warrior import Warrior
from Weapon.Weapon import Weapon
from Player.Player import Player
from Items.Potion import Potion
#rng
import random

# CREATE STARTING WEAPON
def createStartingWeapon():
    startingWeaponDmg = 0

    #randomizes starting weapon
    weaponsList = ['Sword', 'Pike', 'Mace', 'Axe']
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

    newWeapon = Weapon(startingWeaponDmg,'Normal', startingWeaponName)
    return newWeapon

def createNewWeapon():
    #local variables
    newWeaponRarity
    newWeaponDmg = 0

    #randomizes weapon type
    weaponsList = ['Sword', 'Pike', 'Mace', 'Axe']
    newWeaponName = random.choice(weaponsList)

    #assigns random rarity to a weapon
    weaponRarityValue = random.randint(1,100)
    match weaponRarityValue:
        #70% normal
        case x if 1 <= x <= 70:
            newWeaponRarity = "Normal"
        #20% rare
        case x if 71 <= x <= 90:
            newWeaponRarity = "Rare"
        #9% legendary
        case x if 91 <= x <= 99:
            newWeaponRarity = "Legendary"
        #1% god
        case 100 :
            newWeaponRarity = "God"
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


    newWeapon = Weapon(newWeaponDmg, newWeaponRarity, newWeaponName)
    return newWeapon

#create new player
def createNewPlayer():
    basePoints = 5
    startingWeapon = createStartingWeapon()
    print("Digite seu nome:")
    playerNameInput = input()
    
    print("Gostaria de usar os pontos extras em")
    print("1 - HP")
    print("2 - DMG")
    print("3 - SP")
    choice = input()
    #                       Name            xp  lvl                  maxHP    hP      maxSP/sP equipedWeapon armor BA
    match int(choice):
        case 1:
            totalHp = 37 + basePoints
            player = Player(playerNameInput, 0, 1, Warrior(totalHp, totalHp, 15, 15, startingWeapon, 1, 2)) 

        case 2:
            totalBA = 2 + basePoints
            player = Player(playerNameInput, 0, 1, Warrior(37, 37, 15, 15, startingWeapon, 1, totalBA))

        case 3:
            totalSP = 15 + basePoints
            player = Player(playerNameInput, 0, 1, Warrior(37, 37, totalSP, totalSP, startingWeapon, 1, 2))

        case _:
            player = Player(playerNameInput, 0, 1, Warrior(37, 37, 15, 15, startingWeapon, 1, 2))


    print(f"Jogador {player.name} criado com sucesso!")
    return player

# potion drop
def chestPotionDrop():

    #60% chance of beeing Large
    potionSizeValue = random.randint(1,10)
    potionSize = 'Large' if potionSizeValue > 4 else 'Small'

    #70% chance of beeing HP
    potionTypeValue = random.randint(1,10)
    potionType = 'HP' if potionTypeValue > 3 else 'SP'

    newPotion = Potion(potionSize, potionType)
    return newPotion

def createChest():
    #80% potion
    #10% armor
    #10% weapon
    print("Voce encontrou um bau!")
    chestItemValue = random.randint(1,10)
    chestLoot =''
    #armor
    if (chestItemValue == 10):
        print("work in progress, no armor yet")
    #weapon
    elif (chestItemValue == 9):    
        chestLoot = createNewWeapon()
        print(f"O bau continha: {chestLoot.weaponName} | Dano base: {chestLoot.baseDamage} | Dano total: {chestLoot.totaldmgValue} | Raridade: {chestLoot.weaponRarity}")
        return chestLoot
    #potion
    else:      
        chestLoot = chestPotionDrop()
        print(f'O bau continha: {chestLoot.potionName}. +{chestLoot.potionRegenPoints} {chestLoot.potionType}')
        return chestLoot
#battle
def battle(player, enemy):
    while True:
        escapeState = ''
        
        print()
        print(f"Um {enemy.name} apareceu!")
        print(f"{player.name} HP: {player.playerClass.healthPoints}/{player.playerClass.maxHealthPoints}  |  SP: {player.playerClass.sP}/{player.playerClass.maxSP}")
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
            enemy.defend(player.playerClass.attack())
            print(f"O jogador {player.name} atacou o {enemy.name} com {player.playerClass.equipedWeapon.weaponName} e o dano foi: {player.playerClass.attack()}")
            # enemy attack
            player.playerClass.defend(enemy.attack())
            print(f"O {enemy.name} atacou o jogador! O dano recebido foi: {enemy.attackDmg}")
        # player uses item
        elif(int(choice) == 2):
            escapeState = False
            print("work in progress, cant use items yet")
        # attempts to escape
        elif(int(choice) == 3):
            escapeValue = random.randint(1,100)
            escapeState = player.playerClass.escape(escapeValue)
            if(escapeState):
                print(f"{player.name} escapou!")
            else:
                print(f"Fuga mal sucedida, {enemy.name} errou seu ataque!")


        # after choosing option
        # checks if player successfully escaped
        if(escapeState):
            break
        # checks if player died
        if (player.playerClass.healthPoints <= 0):
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
print(f"Arma: {jogueidor.playerClass.equipedWeapon.weaponName} | Dano base: {jogueidor.playerClass.equipedWeapon.baseDamage} | Dano total: {jogueidor.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogueidor.playerClass.equipedWeapon.weaponRarity}")

# 1st battle simulation
battle(jogueidor, rato)

# weapon drop simulation
#arma = createNewWeapon()
#jogueidor.playerClass.equipedWeapon = arma
#print("Voce encontrou uma nova arma!")
#print(f"Arma: {jogueidor.playerClass.equipedWeapon.weaponName} | Dano base: {jogueidor.playerClass.equipedWeapon.baseDamage} | Dano total: {jogueidor.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogueidor.playerClass.equipedWeapon.weaponRarity}")

# 2nd battle simulation
#battle(jogueidor, ogre)




# potion testing
#pocaoBau1 = chestPotionDrop()
#pocaoBau2 = chestPotionDrop()
#print(f'{pocaoBau1.potionName}. +{pocaoBau1.potionRegenPoints} {pocaoBau1.potionType} ')
#print(f'{pocaoBau2.potionName}. +{pocaoBau2.potionRegenPoints} {pocaoBau2.potionType} ')


# potion use simulation
#pocaoBau1 = chestPotionDrop()
#necessitado = Player('sofrido', 0, 1, Warrior(40, 20, 15, 10, Weapon(12,'Normal', 'consolo'), 1, 2))
#print(f"Jogador {necessitado.name} | {necessitado.playerClass.healthPoints}/{necessitado.playerClass.maxHealthPoints}HP| {necessitado.playerClass.sP}/{necessitado.playerClass.maxSP}SP")

#necessitado.playerClass.usePotion(pocaoBau1)
#print('apos potion')
#print(f"Jogador {necessitado.name} | {necessitado.playerClass.healthPoints}/{necessitado.playerClass.maxHealthPoints}HP| {necessitado.playerClass.sP}/{necessitado.playerClass.maxSP}SP")