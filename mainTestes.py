from Enemies.Rat import Rat
from Player.PlayerClassWarrior import PlayerClassWarrior
from Weapon.Weapon import Weapon
from Enemies.Ogre import Ogre
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



    return player




#battle rat
def battleRat(jogador, rato):
    while True:

        rato.defend(jogador.playerClass.attack())
        print(f"O jogador {jogador.name} atacou o rato com {jogador.playerClass.equipedWeapon.weaponName} e o dano foi: {jogador.playerClass.attack()}")
        jogador.playerClass.defend(rato.attack())
        print(f"O rato atacou o jogador! O dano recebido foi: {rato.attackDmg}")

        if (jogador.playerClass.healthPoints <= 0):
            print("Você morreu!")
            break
        if(rato.healthPoints <= 0):
            print("O rato morreu!")
            jogador.xpPoints += rato.xpReward
            print(f"Voce recebeu {rato.xpReward} xp.")
            break



#enemy
rato = Rat()
ogre = Ogre()



jogueidor = createNewPlayer()
print(f"Jogador1 HP: {jogueidor.playerClass.healthPoints}")
print(f"Rato HP: {rato.healthPoints}")
print(f"Arma: {jogueidor.playerClass.equipedWeapon.weaponName} | Dano base: {jogueidor.playerClass.equipedWeapon.baseDamage} | Dano total: {jogueidor.playerClass.equipedWeapon.totaldmgValue} | Raridade: {jogueidor.playerClass.equipedWeapon.weaponRarity}")

battleRat(jogueidor, rato)
print(jogueidor.xpPoints)




#print("Ogre apareceu!")
#print(f"Jogador1 HP: {jogador1.healthPoints}")
#print(f"Ogre HP: {ogre.healthPoints}")

#attacking
#ogre.defend(jogador1.attack())
#jogador1.defend(ogre.attack())

#print("* after attack *")
#print(f"Jogador1 HP: {jogador1.healthPoints}")
#print(f"Ogre HP: {ogre.healthPoints}")



