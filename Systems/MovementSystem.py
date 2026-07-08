from Systems import RoomController  

# moves player left
def move_left(gameMap, player):

    current = current_room(gameMap)

    # checks if there is a room there to move
    if current.left is None:
        print("You can't go that way.")
        return

    # starts enter room from roomcontroller
    move_to(gameMap, player, current.left)
    


# moves player right
def move_right(gameMap, player):
    
    current = current_room(gameMap)

    # checks if there is a room there to move
    if current.right is None:
        print("You can't go that way.")
        return

    # starts enter room from roomcontroller
    move_to(gameMap, player, current.right)
    

# moves player to previous room
def move_back(gameMap, player):

    current = current_room(gameMap)

    # checks if there is a room there to move
    if current.parent is None:
        print("You're already at the entrance.")
        return

    # starts enter room from roomcontroller
    move_to(gameMap, player, current.parent)

# UI assistant
def show_options(gameMap):

    # assigns current room to room
    room = current_room(gameMap)

    # prints its id
    print(f"\nRoom {room.id}")
    # prints possible movement
    if room.left:
        print("1 - Left")

    if room.right:
        print("2 - Right")

    if room.parent:
        print("3 - Back")

# gives you the current room in which the player is located
def current_room(gameMap):
    return gameMap.currentRoom

# movement assist
def move_to(gameMap, player, room):
    # updates the current room
    gameMap.currentRoom = room
    RoomController.enter_room(player, room)