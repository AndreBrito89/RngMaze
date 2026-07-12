from Player.Player import Player
from Items.Armor import Armor
from Factories.WeaponFactory import create_starting_melee_weapon
from Factories.WeaponFactory import create_starting_catalyst_weapon


# create new player
def create_new_player(playerName, playerClass, playerBonusPoints):
 
    # assigns base stats based on the player's class
    match playerClass:
            
        case "1":
            newPlayerClass = 'Warrior'
            baseHp = 37
            baseSp = 15
            startingWeapon = create_starting_melee_weapon()
            startingArmor = Armor('Leather', 1)
            baseAttack = 1
               
        case "2":
            newPlayerClass = 'Mage'
            baseHp = 19
            baseSp = 24
            startingWeapon = create_starting_catalyst_weapon()
            startingArmor = Armor('No', 0)
            baseAttack = 4  
                
    # assigns bonus points to the attribute selected by the player
    match playerBonusPoints:
        #Health Points
        case "1":
            baseHp += 5
        #Base Attack
        case "2":
            baseAttack += 5
        #Stamina/Special Points
        case "3":
            baseSp += 5
    
        
    newPlayer = Player(playerName, 0, 1, newPlayerClass, baseHp, baseHp, baseSp, baseSp, startingWeapon, startingArmor, baseAttack) 
    return newPlayer
