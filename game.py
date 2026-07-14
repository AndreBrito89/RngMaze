from Factories.PlayerFactory import create_new_player
from Systems import StageLoader
from Systems import MovementSystem
from Systems import UISystem

player_name, player_class, player_bonus_points = UISystem.get_player_info()
player = create_new_player(player_name, player_class, player_bonus_points)

gameMap = StageLoader.load(1, player)

while True:
    # checks if player is dead
    if player.healthPoints <= 0:
        break
    room = gameMap.currentRoom

    print(f"\nYou are in room {room.id}")

    MovementSystem.show_options(gameMap)

    choice = input("> ")

    if choice == "1":
        MovementSystem.move_left(gameMap, player)

    elif choice == "2":
        MovementSystem.move_right(gameMap, player)

    elif choice == "3":
        MovementSystem.move_back(gameMap, player)

    elif choice == "4":
        UISystem.show_player_status(player)

    elif choice == "5":
        UISystem.show_map(gameMap)

    elif choice == "0":
        break