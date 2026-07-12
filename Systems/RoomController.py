import random
from Map.Room import RoomType
from Systems import CombatSystem
from Systems import StageLoader

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


# marks room as cleared
def clear_room(room):
    room.cleared = True
    room.enemies.clear()
    print("Room cleared!")


# attempts to escape
def try_escape(player, room):

    # Boss rooms never allow escape
    if room.roomType == RoomType.EXIT:
        print("You cannot escape from a boss fight!")
        return False

    return player.escape(random.randint(1,100))