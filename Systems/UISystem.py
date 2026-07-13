from Map.Room import RoomType

# prints player status
def show_player_status(player):
    print("        ---- STATUS ----")
    print("================================")
    print(f"Jogador: {player.name}")
    print("------------------------------------------------")
    print(f"HP: {player.healthPoints}/{player.maxHealthPoints}")
    print(f"SP: {player.sP}/{player.maxSP}")
    print("------------------------------------------------")
    print(f"Arma: {player.equippedWeapon.weaponName} | Dano base: {player.equippedWeapon.totaldmgValue}")
    print(f"Armadura: {player.equippedArmor.armorName}| Dano reduzido: {player.equippedArmor.armorDefenseValue}")
    print("------------------------------------------------")
    print(f"Key: {'Yes' if player.hasKey else 'No'}")
    print("================================")

# prints map
def show_map(gameMap):
    print("\n============ MAP ============")
    draw_room(gameMap.root, "", True, gameMap.currentRoom)
    print("\n============================")
    print("[P] - posicao atual")
    print("[X] - inimigos mortos")
    print("[ ] - inimigos ativos")
    print("[B] - sala do chefe")
    print("[K] - sala da chave")
    print("... - caminho inexplorado")

# draws room
def draw_room(room, prefix, is_last, current):
    # marks player's current room
    if room == current:
        symbol = "P"
    # checks if the cleared room was a key room
    elif room.cleared and room.roomType == RoomType.KEY:
        symbol = "K"
    # checks if the cleared room was a boss room
    elif room.cleared and room.roomType == RoomType.EXIT:
        symbol = "B"
    # checks if the room was cleared
    elif room.cleared:
        symbol = "X"
    else:
        symbol = " "
    
    # ascii lines for room connection
    connector = "└── " if is_last else "├── "
    # checks if the room was visited, if it wasnt, stops printing that maze branch
    if not room.visited:
        print(prefix + connector + "...")
        return

    print(prefix + connector + f"[{symbol}] Room {room.id}")

    children = []
    # checks if there are rooms forward
    if room.left:
        children.append(room.left)

    if room.right:
        children.append(room.right)

    new_prefix = prefix + ("    " if is_last else "│   ")

    for i, child in enumerate(children):
        draw_room(
            child,
            new_prefix,
            i == len(children)-1,
            current
        )