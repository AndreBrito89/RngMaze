import random
from Map.Room import RoomType
from Systems import CombatSystem
from Systems import StageLoader
from Systems import ChestSystem
# player enter a room
def enter_room(player, room, gameMap):

    # marks room as visited
    room.visited = True

    # check if the room is already clear
    if room.cleared:
        return
    
    # starts combat if there are enemies
    if room.enemies:
        CombatSystem.start_combat(player, room, StageLoader.get_stage_data(gameMap.stage).ESCAPE_FAIL_MISS_RATE)

    # opens chests after battle
    if room.chest:
        ChestSystem.open_chest(player, room)

# marks room as cleared
def clear_room(room):
    room.cleared = True
    room.enemies.clear()
    print("Sala concluida!")


# attempts to escape
def try_escape(player, room):

    # Boss rooms never allow escape
    if room.roomType == RoomType.EXIT:
        print("Voce nao pode fugir de uma batalha contra o chefe!")
        return False

    return player.escape(random.randint(1,100))