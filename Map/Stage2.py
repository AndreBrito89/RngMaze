from Map.Room import Room
from Map.Map import Map
# merchant
MERCHANT_MAX_TRANSACTION_TIER = 3
# rooms
POSSIBLE_KEY_ROOMS = [5,7,8,9]
POSSIBLE_EXIT_ROOMS = [11,13,14]
TREASURE_RATE = 30
# escape
ESCAPE_FAIL_MISS_RATE = 45
ESCAPE_XP_REWARD = 35
def create():
    # list of rooms
    rooms = {}
    # creates an instance of Room for each room of the stage
    for i in range(1, 15):
        rooms[i] = Room(i)
    
    # assigns correlation between rooms
    rooms[1].left = rooms[3]
    rooms[1].right = rooms[2]

    rooms[2].left = rooms[5]
    rooms[2].right = rooms[4]
    rooms[2].parent = rooms[1]
    
    rooms[3].left = rooms[7]
    rooms[3].right = rooms[6]
    rooms[3].parent = rooms[1]

    rooms[4].left = rooms[9]
    rooms[4].right = rooms[8]
    rooms[4].parent = rooms[2]

    rooms[6].right = rooms[10]
    rooms[6].parent = rooms[3]

    rooms[10].left = rooms[12]
    rooms[10].right = rooms[11]
    rooms[10].parent = rooms[6]

    rooms[12].left = rooms[14]
    rooms[12].right = rooms[13]
    rooms[12].parent = rooms[10]


    # dead end rooms
    rooms[5].parent = rooms[2]
    rooms[7].parent = rooms[3]
    rooms[8].parent = rooms[4]
    rooms[9].parent = rooms[4]
    rooms[11].parent = rooms[10]
    rooms[13].parent = rooms[12]
    rooms[14].parent = rooms[12]
    

    return Map(2, rooms[1], rooms, ESCAPE_FAIL_MISS_RATE)