class Room:
    # constructor
    def __init__(self, id):

        self.id = id

        self.left = None
        self.right = None
        self.parent = None

        self.enemy = None
        self.chest = None

        self.has_key = False
        self.is_exit = False

        self.visited = False