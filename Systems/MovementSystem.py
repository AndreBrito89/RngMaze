from Systems import RoomController  

# moves player left
def move_left(gameMap, player):

    current = current_room(gameMap)

    # checks if there is a room there to move
    if current.left is None:
        print("Caminho sem saida...")
        return

    # starts enter room from roomcontroller
    move_to(gameMap, player, current.left)
    

# moves player right
def move_right(gameMap, player):
    
    current = current_room(gameMap)

    # checks if there is a room there to move
    if current.right is None:
        print("Caminho sem saida...")
        return

    # starts enter room from roomcontroller
    move_to(gameMap, player, current.right)
    

# moves player to previous room
def move_back(gameMap, player):

    current = current_room(gameMap)

    # checks if you're at at first room
    if current.parent is None:
        print("Voce esta na primeira sala!")
        return

    move_to(gameMap, player, current.parent)

# UI assistant
def show_options(gameMap):

    # assigns current room to room
    room = current_room(gameMap)

    # prints its id
    print(f"\nSala {room.id}")
    # prints possible options and movement
    if room.left:
        print("1 - Esquerda")

    if room.right:
        print("2 - Direita")

    if room.parent:
        print("3 - Voltar")
    
    # prints player status
    print("4 - Player status")
    # prints map
    print("5 - Mapa")
    print("0 - Exit game")

# gives you the current room in which the player is located
def current_room(gameMap):
    return gameMap.currentRoom

# movement assist
def move_to(gameMap, player, new_room):
    # updates the current room
    gameMap.currentRoom = new_room
    RoomController.enter_room(player, new_room, gameMap)