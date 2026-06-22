from Enemies.Rat import Rat
from Player.PlayerClassWarrior import PlayerClassWarrior
from Weapon.Weapon import Weapon
from Enemies.Ogre import Ogre
from Player.Player import Player
#rng
import random


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

#assigns random rarity to a weapon
weaponRarityValue = random.randint(0,100)
weaponRarity = ''
match weaponRarityValue:
    case 0 :
        weaponRarity = "God"
    case x if 1 <= x <= 75:
        weaponRarity = "Normal"
    case x if 76 <= x <= 92:
        weaponRarity = "Rare"
    case x if 93 <= x <= 100:
        weaponRarity = "Legendary"


#assigns random value do the weapon
sword1Dmg = random.randint(5,10)
#dmg value ranges for weapons
# normal = 5-10
# rare = 9-15
# legendary = 13-19
# god = 19-24


#weapons
espada = Weapon(sword1Dmg,weaponRarity,'espada')
#lanca = Weapon(sword2Dmg, 'Normal','lanca')
#machado = Weapon(sword3Dmg, 'Normal','maxado')

#player
preier = Player("Maiconsuel", 0, 1, PlayerClassWarrior(39, espada, 1, 5))
jogador1 = PlayerClassWarrior(42, espada, 2, 4)
#enemy
rato = Rat()
ogre = Ogre()


print(f"Jogador1 HP: {jogador1.healthPoints}")
print(f"Rato HP: {rato.healthPoints}")
print(f"Dano base: {espada.baseDamage} | Dano total: {espada.totaldmgValue} | Raridade: {espada.weaponRarity}")



battleRat(preier, rato)
print(preier.xpPoints)




#print("Ogre apareceu!")
#print(f"Jogador1 HP: {jogador1.healthPoints}")
#print(f"Ogre HP: {ogre.healthPoints}")

#attacking
#ogre.defend(jogador1.attack())
#jogador1.defend(ogre.attack())

#print("* after attack *")
#print(f"Jogador1 HP: {jogador1.healthPoints}")
#print(f"Ogre HP: {ogre.healthPoints}")



