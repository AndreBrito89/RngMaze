from Factories.PlayerFactory import create_new_player
from Systems import StageLoader
from Systems import MovementSystem
from Systems import InventorySystem
from Systems import ProgressionSystem
from Systems import UISystem

UISystem.game_start_header()
# player info
player_name, player_class, player_bonus_points = UISystem.get_player_info()
player = create_new_player(player_name, player_class, player_bonus_points)

gameMap = StageLoader.load(1, player)

while True:
    # checks if player is dead
    if player.healthPoints <= 0:
        break
    # checks if player reached last stage
    if gameMap == None:
        break
    room = gameMap.currentRoom

    UISystem.show_map(gameMap)
    UISystem.show_main_menu_options(gameMap)
    choice = input("> ")

    if choice == "1":
        MovementSystem.move_left(gameMap, player)

    elif choice == "2":
        MovementSystem.move_right(gameMap, player)

    elif choice == "3":
        MovementSystem.move_back(gameMap, player)

    elif choice == "4":
        InventorySystem.player_menu_actions(player)

    elif choice == "5":
        gameMap = ProgressionSystem.try_enter_next_stage(player, gameMap)      
         
    elif choice == "0":
        break




# -> QoL:
#       
# -> logic:
#       * MOVE CHEST CREATION TO STAGELOADER -> REMOVE IT FROM COMBATSYSTEM -> FIX HACK
#       teleport player to boss room with 'search secret door' option if player has key and defeated the boss
#       add hidden potion in rooms, max 1 attempt using 'search secret door', 45% chance

