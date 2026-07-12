from Map import Room
class Map:
    def __init__(self, stage: int, root: Room, rooms, escapeFailMissRate):
        self.stage = stage
        self.root = root
        self.rooms = rooms
        self.currentRoom = root
        self.escapeFailMissRate = escapeFailMissRate