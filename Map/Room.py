from enum import Enum
# enum roomtype
class RoomType(Enum):
    NORMAL = 1
    TREASURE = 2
    KEY = 3
    EXIT = 4
# class room
class Room:
    # constructor
    def __init__(self, id):

        # identity
        self.id = id

        # navigation
        self.left = None
        self.right = None
        self.parent = None

        # contents
        self.enemies = []
        self.chest = None
        self.roomType = RoomType.NORMAL

        # flags
        self.visited = False
        self.cleared = False
        self.hasKey = False
        self.hasChest = False
