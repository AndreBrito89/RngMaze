from Map.Room import Room
from Map.Map import Map

POSSIBLE_KEY_ROOMS = [2,7,9,11]
POSSIBLE_EXIT_ROOMS = [12,13,14,15]
TREASURE_RATE = 40

def create():
    # list of rooms
    rooms = {}
    # creates an instance of Room for each room of the stage
    for i in range(1, 16):
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

    rooms[5].left = rooms[11]
    rooms[5].right = rooms[10]
    rooms[5].parent = rooms[2]

    rooms[6].left = rooms[13]
    rooms[6].right = rooms[12]
    rooms[6].parent = rooms[3]

    rooms[7].left = rooms[15]
    rooms[7].right = rooms[14]
    rooms[7].parent = rooms[3]

    # dead end rooms
    rooms[8].parent = rooms[4]
    rooms[9].parent = rooms[4]
    rooms[10].parent = rooms[5]
    rooms[11].parent = rooms[5]
    rooms[12].parent = rooms[6]
    rooms[13].parent = rooms[6]
    rooms[14].parent = rooms[7]
    rooms[15].parent = rooms[7]


    return Map(3, rooms[1], rooms)