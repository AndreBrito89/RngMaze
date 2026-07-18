from Map.Room import RoomType
import os
import subprocess

# helper
def clear_console():
    input("pressione enter para continuar...")
    if os.name == 'nt':
        # Windows requires executing 'cls' through the command interpreter
        subprocess.run(['cmd', '/c', 'cls'])
    else:
        # Mac and Linux can call 'clear' directly
        subprocess.run(['clear'])

###########
## MENUS ##
###########

# prints combat options
def combat_options(player, enemy):
        clear_console()
        print("========================================================================================")
        print("---------------------------------------------------------------------------------------")
        print(f"Jogador: {player.name}")
        print(f"HP: {player.healthPoints}/{player.maxHealthPoints} | SP: {player.sP}/{player.maxSP}")
        print("---------------------------------------------------------------------------------------")
        # prints enemy status
        print(f"Inimigo: {enemy.name}")
        # prints player status
        print(f"HP: {enemy.healthPoints}/{enemy.maxHealthPoints}")
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

    # player class
    while True:
        print("Selecione sua classe:")
        print("1-> Warrior")
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
    
    # bonus points
    while True:
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


######################
### PLAYER RELATED ###
######################

# prints player status
def show_player_status(player):
    print("        ---- STATUS ----")
    print("================================")
    print(f"Jogador: {player.name}")
    print("------------------------------------------------")
    print(f"HP: {player.healthPoints}/{player.maxHealthPoints}")
    print(f"SP: {player.sP}/{player.maxSP}")
    print("------------------------------------------------")
    print(f"Arma: {player.equippedWeapon.weaponName} | Dano: {player.equippedWeapon.totaldmgValue}")
    print(f"Armadura: {player.equippedArmor.armorName}| Dano reduzido: {player.equippedArmor.armorDefenseValue}")
    print("------------------------------------------------")
    print(f"Key: {'Yes' if player.hasKey else 'No'}")
    print("================================")

# player chooses which weapon to discard after receiving a drop
def choose_weapon_to_discard(player, newWeapon):
    while True:
        print("Escolha uma arma para descartar:")
        print("\n* Lista de armas *")
        print("+----------------------------------------------------------------------------------------------------------------------------------------+")
        print(f"|1 -> Equipada: {player.equippedWeapon.weaponName} | Dano: {player.equippedWeapon.totalDmgValue} | Raridade: {player.equippedWeapon.weaponRarity} |")
        print(f"|2 -> Inventario: {player.inventoryWeapon.weaponName} | Dano: {player.inventoryWeapon.totalDmgValue} | Raridade: {player.inventoryWeapon.weaponRarity}")
        print(f"|3 -> Nova: {newWeapon.weaponName} | Dano: {newWeapon.totalDmgValue} | Raridade: {newWeapon.weaponRarity}")
        print("+----------------------------------------------------------------------------------------------------------------------------------------+")
        
        player_discarded_weapon = input()

        if not player_discarded_weapon.isdigit():
            print("Opcao invalida!")
            continue
        
        match player_discarded_weapon:
            case "1":
                break
            case "2":
                break
            case "3":
                break
        
    return player_discarded_weapon


# player chooses which armor to discard after receiving a drop
def choose_armor_to_discard(player, newArmor):
    while True:
        print("Escolha uma armadura para descartar:")
        print("\n* Lista de armaduras *")
        print("+-------------------------------------------------------------------------------------------------------+")
        print(f"|1 -> Equipada: {player.equippedArmor.armorName} | Dano reduzido: {player.equippedArmor.armorDefenseValue} |")      
        print(f"|2 -> Inventario: {player.inventoryArmor.armorName} | Dano Reduzido: {player.inventoryArmor.armorDefenseValue} |")       
        print(f"|3 -> Nova: {newArmor.armorName} | Dano Reduzido: {newArmor.armorDefenseValue} |")       
        print("+-------------------------------------------------------------------------------------------------------+")
        player_discarded_armor = input()

        if not player_discarded_armor.isdigit():
            print("Opcao invalida!")
            continue
        
        match player_discarded_armor:
            case "1":
                break
            case "2":
                break
            case "3":
                break
        
    return player_discarded_armor


##################
## MAP RELATED ###
##################

# prints map
def show_map(gameMap):
    clear_console()
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