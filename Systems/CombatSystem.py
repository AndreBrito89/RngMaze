import random
from Systems import UISystem
from Systems import RoomController
from Systems import InventorySystem
from Systems import ChestSystem
from Factories import LootFactory
from Map import Room

# combat flow:
# checks room for enemies-> combat UI -> player turn -> resolve action -> enemy turn -> checks if someone died -> loop previous part -> victory

# start combat
def start_combat(player, room, stageData):
    # main loop, stops when there are no enemies in room.enemies[]
    while room.enemies:
        # checks for the result of player_turn, if true stays in the main loop
        combatContinues, enemyActs = player_turn(player, room, stageData)
        # checks if combat should start based on the return of previous line
        if not combatContinues:
            return
        # checks if all the enemies in the room are dead after player turn
        if not room.enemies:
            break
        # checks if the player used a potion or enemy missed attack due to failed attempt escape 
        if enemyActs:
            enemy_turn(player, room)
        #checks if player died
        if player.healthPoints <= 0:
            player_death(player) 
            return False
    # victory screen after main loop ends (no more enemies in the room)
    victory(player, room)


############
## PLAYER ##
############
# player turn
def player_turn(player, room, stageData):
    # prevents the user from breaking the game with a string input
    while True :
        enemy = current_enemy(room)
        # prints combat options
        UISystem.combat_options(player, enemy)
        choice = input("> ")

        # validates that the input is numeric
        if not choice.isdigit():    
            print("Opcao invalida!")
            continue
        # action based on the player selection
        match int(choice):
            case 1:
                player_attack(player, room)
                return True, True
            case 2:
                usedPotion = player_use_potion(player)
                # checks if the player actually consumed a potion, if so skips enemy turn
                if usedPotion:
                    return True, False
                # otherwise, goes back to previous menu
                continue
            case 3:
                return player_escape_attempt_result(player, room, stageData)
            case _:
                print("Opcao invalida!")

# player attacks
def player_attack(player, room):

    enemy = current_enemy(room)

    player_damage = player.attack()

    enemy.defend(player_damage)

    print(f"{player.name} atacou {enemy.name} usando {player.equippedWeapon.weaponName}! O dano foi: {player_damage:.2f}!")

    if enemy.healthPoints <= 0:
        print(f"{enemy.name} morreu!")
        print(f"Voce ganhou {enemy.xpReward} xp!")
        player.xpPoints += enemy.xpReward

        room.enemies.remove(enemy)


# player uses potion
def player_use_potion(player):
    return InventorySystem.potion_options(player)
    

# player attempts to escape
def player_escape_attempt_result(player, room, stageData):
    # true/false from roomcontroller
    escaped = RoomController.try_escape(player, room)

    if escaped:
        player.xpPoints += stageData.ESCAPE_XP_REWARD
        print("Voce fugiu!")
        print(f"{player.name} recebeu {stageData.ESCAPE_XP_REWARD} xp.")
        UISystem.clear_console()
        return False, False

    print("Fuga mal sucedida!")

    # checks if enemy whiffs the attack based on the escape fail miss rate from the stage
    enemyMissed = (random.randint(1,100) <= stageData.ESCAPE_FAIL_MISS_RATE)

    if enemyMissed:
        print(f"{current_enemy(room).name} errou o ataque!")

    return True, not enemyMissed
#############
## ENEMIES ##
#############

# enemy turn
def enemy_turn(player, room):
    enemy = current_enemy(room)
    
    #calculates damage
    enemy_damage = enemy.attack()
    player.defend(enemy_damage)

    total_enemy_damage = max(0, enemy_damage - player.equippedArmor.armorDefenseValue)

    # prints damage received after armor reduction
    print(f"{enemy.name} atacou! O dano recebido foi: {total_enemy_damage}")
    
# current enemy helper
def current_enemy(room):
    return room.enemies[0]

#############
## RESULTS ##
#############

# player clears room
def victory(player, room):
    
    print("Voce venceu a batalha!")

    if room.hasChest:
        room.hasChest = False
        room.chest = LootFactory.create_chest(player.playerClass)
        print("\nUm bau apareceu!\n")
        ChestSystem.open_chest(player, room)

    if room.hasKey:
        player.hasKey = True
        room.hasKey = False
        print("\n**Voce obteve a chave!**\n")

    if room.roomType == Room.RoomType.EXIT:
        room.chest = LootFactory.create_boss_chest(player.playerClass)
        print("O chefe guardava um baú!")
        ChestSystem.open_chest(player, room)
        
    RoomController.clear_room(room)

# player dies (restart run?)
def player_death(player):

    print(f"\n* {player.name} lutou bravamente até a morte. *\n")
    print("+------------+")
    print("| Game Over. |")
    print("+------------+")
    
    return False 