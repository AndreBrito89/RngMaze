from Enemies.Enemy import Enemy
from Player.PlayerClassWarrior import PlayerClassWarrior
from Weapon.Weapon import Weapon
from Player.Player import Player
#rng
import random

# CREATE STARTING WEAPON
def createStartingWeapon():
    weaponsList = ['Sword', 'Pike', 'Mace', 'Axe']
    #assigns random value do the weapon
    weaponDmg = random.randint(5,10)
    #randomizes starting weapon
    weaponName = random.choice(weaponsList)
    
    weapon = Weapon(weaponDmg,'Normal', weaponName)
    return weapon


def createNewWeapon():
    #assigns random rarity to a weapon
    weaponRarityValue = random.randint(0,100)
    weaponRarity = ''
    weaponDmg = 0
    match weaponRarityValue:
        case 0 :
            weaponRarity = "God"
            weaponDmg = random.randint(19,24)
        case x if 1 <= x <= 75:
            weaponRarity = "Normal"
            weaponDmg = random.randint(5,10)
        case x if 76 <= x <= 92:
            weaponRarity = "Rare"
            weaponDmg = random.randint(9,15)
        case x if 93 <= x <= 100:
            weaponRarity = "Legendary"
            weaponDmg = random.randint(13,19)
    
    #randomizes weapon type
    weaponsList = ['Sword', 'Pike', 'Mace', 'Axe']
    weaponName = random.choice(weaponsList)

    weapon = Weapon(weaponDmg, weaponRarity, weaponName)
    return weapon

#create new player
def createNewPlayer():
    basePoints = 5
    startingWeapon = createStartingWeapon()
    print("Digite seu nome:")
    playerNameInput = input()
    
    print("Gostaria de usar os pontos extras em")
    print("1 - HP")
    print("2 - DMG")
    choice= input()

    match int(choice):
        case 1:
            player = Player(playerNameInput, 0, 1, PlayerClassWarrior(37 + basePoints, startingWeapon , 1, 2))

        case 2:
            player = Player(playerNameInput, 0, 1, PlayerClassWarrior(37, startingWeapon , 1, 2 + basePoints))

        case _:
            player = Player(playerNameInput, 0, 1, PlayerClassWarrior(37, startingWeapon , 1, 2))


    print(f"Jogador {player.name} criado com sucesso!")
    return player




#battle
def battle(player, enemy):
    while True:

        print()
        print(f"{player.name} HP: {player.playerClass.healthPoints}")
        print(f"{enemy.name} HP: {enemy.healthPoints}")

        enemy.defend(player.playerClass.attack())
        print(f"O jogador {player.name} atacou o {enemy.name} com {player.playerClass.equipedWeapon.weaponName} e o dano foi: {player.playerClass.attack()}")
        player.playerClass.defend(enemy.attack())
        print(f"O {enemy.name} atacou o jogador! O dano recebido foi: {enemy.attackDmg}")

        if (player.playerClass.healthPoints <= 0):
            print("Você morreu!")
            break
        if(enemy.healthPoints <= 0):
            print(f"O {enemy.name} morreu!")
            player.xpPoints += enemy.xpReward
            print(f"Voce recebeu {enemy.xpReward} xp.")
            print()
            break



# enemy
rato = Enemy('Rat', 12, 3, 0, 20)
ogre = Enemy ('Ogre', 21, 9, 1, 50)



# player
jogueidor = createNewPlayer()
print(f"Arma: {jogueidor.playerClass.equipedWeapon.weaponName} | Dano base: {jogueidor.playerClass.equipedWeapon.baseDamage} | Dano total: {jogueidor.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogueidor.playerClass.equipedWeapon.weaponRarity}")

# 1st battle simulation
battle(jogueidor, rato)

# weapon drop simulation
arma = createNewWeapon()
jogueidor.playerClass.equipedWeapon = arma
print("Voce encontrou uma nova arma!")
print(f"Arma: {jogueidor.playerClass.equipedWeapon.weaponName} | Dano base: {jogueidor.playerClass.equipedWeapon.baseDamage} | Dano total: {jogueidor.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogueidor.playerClass.equipedWeapon.weaponRarity}")

# 2nd battle simulation
battle(jogueidor, ogre)


