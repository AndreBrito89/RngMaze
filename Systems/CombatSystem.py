import random
from Systems import UISystem
from Systems import RoomController
from Systems import InventorySystem
from Factories import LootFactory

# combat flow:
# checks room for enemies-> combat UI -> player turn -> resolve action -> enemy turn -> checks if someone died -> loop previous part -> victory

# start combat
def start_combat(player, room, escapeFailMissRate):
    # main loop, stops when there are no enemies in room.enemies[]
    while room.enemies:
        # checks for the result of player_turn, if true stays in the main loop
        combatContinues, enemyMisses = player_turn(player, room, escapeFailMissRate)
        # checks if combat should start based on the return of previous line
        if not combatContinues:
            return
        # checks if all the enemies in the room are dead after player turn
        if not room.enemies:
            break
        # checks if enemy missed attack due to failed attempt escape
        if enemyMisses:
            continue
        # starts enemy turn
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
def player_turn(player, room, escapeFailMissRate):
    # prevents the user from breaking the game with a string input
    while True :
        enemy = current_enemy(room)
        # prints combat options
        UISystem.combat_options(player, enemy)
        choice = input()

        # validates that the input is numeric
        if not choice.isdigit():    
            print("Opcao invalida!")
            continue
        # action based on the player selection
        match int(choice):
            case 1:
                player_attack(player, room)
                return True, False
            case 2:
                player_use_potion(player)
                return True, False
            case 3:
                return player_escape_attempt_result(player, room, escapeFailMissRate)
            case _:
                print("Opcao invalida!")

# player attacks
def player_attack(player, room):

    enemy = current_enemy(room)

    player_damage = player.attack()

    enemy.defend(player_damage)

    print(f"{player.name} atacou {enemy.name} usando {player.equippedWeapon.weaponName}! O dano foi: {player_damage}!")

    if enemy.healthPoints <= 0:
        print(f"{enemy.name} morreu!")
        print(f"Voce ganhou {enemy.xpReward} xp!")
        player.xpPoints += enemy.xpReward

        room.enemies.remove(enemy)


# player uses potion
def player_use_potion(player):
    InventorySystem.use_potion(player)


# player attempts to escape
def player_escape_attempt_result(player, room, escapeFailMissRate):
    # true/false from roomcontroller
    escaped = RoomController.try_escape(player, room)

    if escaped:
        print("Voce fugiu!")
        return False, False

    print("Fuga mal sucedida!")

    # checks if enemy whiffs the attack based on the escape fail miss rate from the stage
    enemyMisses = (random.randint(1,100) <= escapeFailMissRate)

    if enemyMisses:
        print(f"{current_enemy(room).name} errou o ataque!")

    return True, enemyMisses
#############
## ENEMIES ##
#############

# enemy turn
def enemy_turn(player, room):
    enemy = current_enemy(room)
    
    #calculates damage
    enemy_damage = enemy.attack()
    player.defend(enemy_damage)

    # prints damage received after armor reduction
    total_enemy_damage = max(0, enemy_damage - player.equippedArmor.armorDefenseValue)

    print(f"{enemy.name} atacou! O dano recebido foi: {total_enemy_damage}")
    
# current enemy helper
def current_enemy(room):
    return room.enemies[0]

#############
## RESULTS ##
#############

# player clears room
def victory(player, room):
    
    print("Victory!")

    if room.hasChest:
        room.hasChest = False
        room.chest = LootFactory.create_chest(player.playerClass)
        print("Um bau apareceu!")

    if room.hasKey:
        player.hasKey = True
        room.hasKey = False
        print("Voce obteve a chave!")

    RoomController.clear_room(room)

# player dies (restart run?)
def player_death(player):

    print(f"\n* {player.name} lutou bravamente até a morte. *\n")
    print("+------------+")
    print("| Game Over. |")
    print("+------------+")
    
    return False 