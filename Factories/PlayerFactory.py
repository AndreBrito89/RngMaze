from Entities.Player import Player
from Items.Armor import Armor
from Factories.WeaponFactory import create_starting_melee_weapon
from Factories.WeaponFactory import create_starting_catalyst_weapon
from Factories import WeaponFactory


# create new player
def create_new_player(playerName, playerClass, playerBonusPoints):
 
    # assigns base stats based on the player's class
    match playerClass:
            
        case "1":
            newPlayerClass = 'Warrior'
            baseHp = 40
            baseSp = 16
            startingWeapon = create_starting_melee_weapon()
            startingArmor = Armor('Leather', 1)
            baseAttack = 1.5
               
        case "2":
            newPlayerClass = 'Mage'
            baseHp = 19
            baseSp = 25
            startingWeapon = create_starting_catalyst_weapon()
            startingArmor = Armor('Leather', 0)
            baseAttack = 3
        case "3":
            newPlayerClass = 'Mage'
            baseHp = 19
            baseSp = 25
            startingWeapon = WeaponFactory.catalyst_generator(WeaponFactory.boss_weapon_rarity_generator())
            startingArmor = Armor('Silver', 6)
            baseAttack = 25            
    # assigns bonus points to the attribute selected by the player
    match playerBonusPoints:
        #Health Points
        case "1":
            baseHp += 5
        #Stamina/Special Points
        case "2":
            baseSp += 5
        #Base Attack
        case "3":
            baseAttack += 2
    
        
    newPlayer = Player(playerName, 0, 1, newPlayerClass, baseHp, baseHp, baseSp, baseSp, startingWeapon, startingArmor, baseAttack) 
    return newPlayer
