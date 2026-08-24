from Map.Room import Room
from Map.Map import Map
# merchant
MERCHANT_MAX_TRANSACTION_TIER = 4
# rooms
POSSIBLE_KEY_ROOMS = [2]
POSSIBLE_EXIT_ROOMS = [3]
TREASURE_RATE = 0
# escape
ESCAPE_FAIL_MISS_RATE = 65
ESCAPE_XP_REWARD = 280

def create():
    # list of rooms
    rooms = {}
    # creates an instance of Room for each room of the stage
    for i in range(1, 4):
        rooms[i] = Room(i)
    
    # assigns correlation between rooms
    rooms[1].left = rooms[2]
    
    rooms[2].left = rooms[3]
    rooms[2].parent = rooms[1]
    
    rooms[3].parent = rooms[2]



    return Map(4, rooms[1], rooms)