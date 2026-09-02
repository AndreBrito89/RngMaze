import random
from Map.Room import RoomType
from Systems import CombatSystem
from Systems import StageLoader
from Systems import UISystem


# player enter a room
def enter_room(player, room, gameMap):

    # marks room as visited
    room.visited = True

    # check if the room is already clear
    if room.cleared:
        return

    # starts combat if there are enemies
    if room.enemies:
        stageData = StageLoader.get_stage_data(gameMap.stage)
        CombatSystem.start_combat(player, room, stageData)


# marks room as cleared
def clear_room(room):
    room.cleared = True
    room.enemies.clear()
    print("\nSala concluida!\n")
    UISystem.clear_console()


# attempts to escape
def try_escape(player, room):

    # Boss rooms never allow escape
    if room.roomType == RoomType.EXIT:
        print("Voce nao pode fugir de uma batalha contra o chefe!")
        return False

    return player.escape(random.randint(1,100))