from Map.Room import RoomType
from Systems import MovementSystem
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
# MAIN MENU OPTIONS
def show_main_menu_options(gameMap):

    # assigns current room to room
    room = MovementSystem.current_room(gameMap)

    # prints its id
    print(f"\nSala {room.id}")

    # prints possible movement options
    if room.left:
        print("1 - Esquerda")

    if room.right:
        print("2 - Direita")

    if room.parent:
        print("3 - Voltar")
    
    # extra options
    print("4 - Status do Jogador")
    print("5 - Inventario")
    print("0 - Exit game")

# inventory menu options
def show_inventory_menu_options():
    clear_console()
    while True:
        print("1 -> Pochete de Pocoes")
        print("2 -> Trocar arma")
        print("3 -> Trocar armadura")

        selectedInventoryOption = input()

        if not selectedInventoryOption.isdigit():
            print("Opcao invalida")
            continue
        #int conversion
        selectedInventoryOption = int(selectedInventoryOption)

        if 1 <= selectedInventoryOption <= 3:
            return selectedInventoryOption
        
        print("Opcao invalida")
        


# prints combat options
def combat_options(player, enemy):
        clear_console()
        print("========================================================================================")
        print(f"Jogador: {player.name}")
        print(f"HP: {player.healthPoints}/{player.maxHealthPoints} | SP: {player.sP}/{player.maxSP}")
        print("---------------------------------------------------------------------------------------")
        # prints enemy status
        print(f"Inimigo: {enemy.name}")
        # prints player status
        print(f"HP: {enemy.healthPoints}/{enemy.maxHealthPoints}")
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
    print(f"Jogador: {player.name} | XP: {player.xpPoints}")
    print("------------------------------------------------")
    print(f"HP: {player.healthPoints}/{player.maxHealthPoints}")
    print(f"SP: {player.sP}/{player.maxSP}")
    print("------------------------------------------------")
    print(f"Arma: {player.equippedWeapon.weaponName} | Dano: {player.equippedWeapon.totaldmgValue} | Raridade: {player.equippedWeapon.weaponRarity}")
    print(f"Armadura: {player.equippedArmor.armorName}| Dano reduzido: {player.equippedArmor.armorDefenseValue}")
    print("------------------------------------------------")
    print(f"Key: {'Yes' if player.hasKey else 'No'}")
    print("================================")
    clear_console()

# shows player's available weapons
def show_player_weapons(player):
    print("        ---- ARMAS ----")
    print("==========================================================================")
    print(f"Equipada: {player.equippedWeapon.weaponName} | Dano: {player.equippedWeapon.totaldmgValue} | Raridade: {player.equippedWeapon.weaponRarity}")
    if not player.has_weapon_slot():
        print(f"Inventario: {player.inventoryWeapon.weaponName} | Dano: {player.inventoryWeapon.totaldmgValue} | Raridade: {player.inventoryWeapon.weaponRarity}")
    print("==========================================================================")

# shows player's available armors
def show_player_armors(player):
    print("        ---- ARMADURAS ----")
    print("=====================================================================================")
    print(f"Equipada: {player.equippedArmor.armorName} | Dano Reduzido: {player.equippedArmor.armorDefenseValue}")
    if not player.has_armor_slot():
        print(f"Equipada: {player.inventoryArmor.armorName} | Dano Reduzido: {player.inventoryArmor.armorDefenseValue}")
    print("=====================================================================================")
    

# shows the list of the player's potions
def show_player_potions(player):
        
        print("Pochete de pocoes")
        print("----------------------------------")
        # iterates instance of potion in player.potions
        for i, potion in enumerate(player.potions, start=1):
            print(f"{i} -> {potion.potionName} | +{potion.potionRegenPoints} {potion.potionType}")   
        print("----------------------------------")

# selects a potion from inventory to consume
def select_inventory_potion(player):
        while True:
            print("Qual das pocoes acima gostaria de consumir?")
            player_selected_potion = input()

            if not player_selected_potion.isdigit():
                print("Opcao invalida!")
                continue
            # int conversion
            player_selected_potion = int(player_selected_potion)

            # validates if the potion exists in the player's inventory
            if 1 <= player_selected_potion <= len(player.potions):
                return player_selected_potion
        
            print("Opcao invalida!")   

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
        
        if player_discarded_weapon in ("1", "2", "3"):
            return player_discarded_weapon

        print("Opcao invalida!")


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
        
        if player_discarded_armor in ("1", "2", "3"):
            return player_discarded_armor

        print("Opcao invalida!")

# player chooses a potion from either their inventory or the new one
def choose_new_potion_option(player):
    # player chooses a potion
    while True:
        print("Voce nao pode carregar mais pocoes!")
        print("Selecione uma pocao")

        show_player_potions(player)
        
        player_selected_potion = input()

        if not player_selected_potion.isdigit():
            print("Opcao invalida!")
            continue
        player_selected_potion = int(player_selected_potion)

        if 1 <= player_selected_potion <= 6:
            return player_selected_potion
        
        print("Opcao invalida!")

# player chooses to either discard or consume a potion
def choose_potion_action():
    while True:
        print("Deseja consumir ou descartar esta pocao?")
        print("1 -> Consumir")
        print("2 -> Descartar")

        potionOption = input()

        if potionOption in ("1", "2"):
            return potionOption

        print("Opcao invalida!")                  

##################
## MAP RELATED ###
##################
# prints map
def show_map(gameMap):
    # prints map
    print("\n============ MAPA ============")
    draw_room(gameMap.root, "", True, gameMap.currentRoom)
    print("\n============================")

    # prints room symbol
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