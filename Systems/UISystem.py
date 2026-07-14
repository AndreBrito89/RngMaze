from Map.Room import RoomType

# prints combat options
def combat_options(player, enemy):
        print("========================================================================================")
        # prints enemy status
        print(f"Inimigo: {enemy.name}")
        # prints player status
        print(f"HP: {enemy.healthPoints}/{enemy.maxHealthPoints}")
        print("---------------------------------------------------------------------------------------")
        print(f"Jogador: {player.name}")
        print(f"HP: {player.healthPoints}/{player.maxHealthPoints} | SP: {player.sP}/{player.maxSP}")
        print("---------------------------------------------------------------------------------------")
        # prints player optios
        print("Escolha sua acao!")
        print("1 - Atacar")
        print("2 - Utilizar pocao")
        print("3 - Tentar fugir")
        print("========================================================================================")

# gets player name, class and extra points
def get_player_info():
    # player name
    print("Digite seu nome:")
    newPlayerName = input()

    while True:
        # player class
        print("Selecione sua classe:")
        print("1 -> Warrior")
        print("2-> Mage")
        newPlayerClass = input()

        if not newPlayerClass.isdigit():
            print("Opcao invalida!")
            continue
        
        match newPlayerClass:
            case "1":
                break
            case "2":
                break
    while True:
        # bonus points
        print("Selecione um atributo para adicionar pontos extra:")
        print("1-> HP")
        print("2-> SP")
        print("3-> Dano base")
        newPlayerExtraPoints = input()

        if not newPlayerExtraPoints.isdigit():
            print("Opcao invalida!")
            continue
        match newPlayerExtraPoints:
            case "1":
                break
            case "2":
                break
            case "3":
                break

    return newPlayerName, newPlayerClass, newPlayerExtraPoints

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
    print("[ ] - sala vazia")
    print("[X] - sala com inimigos ativos")
    print("[B] - sala do chefe")
    print("[K] - sala da chave")
    print("... - caminho inexplorado")
    print("============================\n")

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
        symbol = " "
    else:
        symbol = "X"
    
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
    
    # calls itself recursively drawing one side of the tree, then the other one
    for i, child in enumerate(children):
        draw_room(
            child,
            new_prefix,
            i == len(children)-1,
            current
        )