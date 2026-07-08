import random
from Map.Room import RoomType

# player enter a room
def enter_room(player, room):

    # marks room as visited
    room.visited = True

    # check if the room is already clear
    if room.cleared:
        return
    
    # starts combat if there are enemies
    if room.enemies:
        
        print("Combat starts here later.")
        #clears room after combat ends
        clear_room(room)
    
    # spawn chest
    if room.hasChest:
        print("Chest available.")

    #gives player the key
    if room.hasKey:
        print("Key obtained.")

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