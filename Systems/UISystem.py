import os
import subprocess
from collections import deque
from Map.Room import RoomType
from Systems import MovementSystem
from Systems import ProgressionSystem

# map constants
CANVAS_WIDTH = 120
ROW_HEIGHT = 4        # distance between rows
LEAF_SPACING = 8      # horizontal distance between leaf nodes

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
    print(f"\nVoce esta na sala {room.id}\n")

    # prints possible movement options
    if room.left:
        print("1 - Esquerda")

    if room.right:
        print("2 - Direita")

    if room.parent:
        print("3 - Voltar")
    
    # extra options
    print("4 - Status do Jogador")
    print("5 - Procurar Porta Secreta")
    print("0 - Exit game")

# inventory menu options
def show_inventory_menu_options():
    while True:
        print("1 - Level up")
        print("2 -> Trocar arma")
        print("3 -> Trocar armadura")
        print("4 -> Utilizar uma pocao")
        print("5 -> Voltar")

        selectedInventoryOption = input("> ")

        if not selectedInventoryOption.isdigit():
            print("Opcao invalida")
            continue
        #int conversion
        selectedInventoryOption = int(selectedInventoryOption)

        if 1 <= selectedInventoryOption <= 5:
            return selectedInventoryOption
        
        print("Opcao invalida")

########################
### MERCHANT RELATED ###
########################
# main menu
def merchant_main_menu():
    print("Bem-vindo a minha tenda...")
    while True:
            print("\n=== Mercador ===\n")
            print("1 - Comprar Pocoes")
            print("2 - Trocar Pocoes")
            print("3 - Vender Equipamento")
            print("4 - Trocar Equipamento")
            print("5 - Melhorar Equipamento")
            print("6 - Sair")
            merchantSelectedAction = input("> ")

            if not merchantSelectedAction.isdigit():
                print("Opcao invalida")
                continue

            merchantSelectedAction = int(merchantSelectedAction)

            if 1 <= merchantSelectedAction <= 6:
                return merchantSelectedAction

            print("Opcao invalida")
# potion selling
def merchant_sell_potion_size_selection():
    while True:
        print("Selecione o tamanho da pocao")
        print("1 -> Small")
        print("2 -> Large")
        print("3 -> Voltar")

        selectedPotionSize = input("> ")

        if not selectedPotionSize.isdigit():
            print("Opcao invalida")
            continue
        #int conversion
        selectedPotionSize = int(selectedPotionSize)

        if 1 <= selectedPotionSize <= 3:
            return selectedPotionSize
        
        print("Opcao invalida")
# potion selling
def merchant_sell_potion_type_selection():
    while True:
        print("Selecione o tipo da pocao")
        print("1 - HP")
        print("2 - SP")
        print("3 - Voltar")

        selectedPotionType = input("> ")

        if not selectedPotionType.isdigit():
            print("Opcao invalida")
            continue

        selectedPotionType = int(selectedPotionType)

        if 1 <= selectedPotionType <= 3:
            return selectedPotionType

        print("Opcao invalida")
# equipment buying
def merchant_buy_equipment():
    while True:
            print("Entao voce tem tesouros para vender?")
            print("1 - Armas")
            print("2 - Armaduras")
            print("3 - Voltar")
            selectedEquipmentType = input("> ")

            selectedEquipmentType = int(selectedEquipmentType)
            if not selectedEquipmentType.isdigit():
                print("Opcao invalida")
                continue
            if 1 <= selectedEquipmentType <= 3:
                return selectedEquipmentType
            
            print("Opcao invalida")
# sell weapon sub-menu
def merchant_buy_weapon_selection(player):
    while True:
            show_player_weapons(player)
            print("Qual das armas acima gostaria de vender?")
            print(f"1 - {player.equippedWeapon.weaponName}")
            print(f"2 - {player.inventoryWeapon.weaponName}")
            print("3 - Voltar")
            selectedWeapon = input("> ")
            selectedWeapon = int(selectedWeapon)
            if not selectedWeapon.isdigit():
                print("Opcao invalida")
                continue
            if 1 <= selectedWeapon <= 3:
                return selectedWeapon
            
            print("Opcao invalida")
# sell armor sub-menu
def merchant_buy_armor_selection(player):
    while True:
            show_player_armors(player)
            print("Qual das armaduras acima gostaria de vender?")
            print(f"1 - {player.equippedArmor.armorName}")
            print(f"2 - {player.inventoryArmor.armorName}")
            print("3 - Voltar")
            selectedArmor = input("> ")

            selectedArmor = int(selectedArmor)
            if not selectedArmor.isdigit():
                print("Opcao invalida")
                continue
            if 1 <= selectedArmor <= 3:
                return selectedArmor
            
            print("Opcao invalida")            
######################
### PLAYER RELATED ###
######################

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
    newPlayerName = input("> ")

    # player class
    while True:
        print("Selecione sua classe:")
        print("1-> Warrior")
        print("2-> Mage")
        newPlayerClass = input("> ")

        if not newPlayerClass.isdigit():
            print("Opcao invalida!")
            continue
        
        if newPlayerClass in ('1', '2', '3'):
            break
            
    
    # bonus points
    while True:
        print("Selecione um atributo para adicionar pontos extra:")
        print("1-> HP")
        print("2-> SP")
        print("3-> Dano base")
        newPlayerExtraPoints = input("> ")

        if not newPlayerExtraPoints.isdigit():
            print("Opcao invalida!")
            continue
        if newPlayerExtraPoints in ('1','2','3'):
                break

    return newPlayerName, newPlayerClass, newPlayerExtraPoints

# receives player's selected attribute from level up
def select_levelup_extra_point():

    while True:

        print("Escolha um atributo:")
        print("1 - HP")
        print("2 - SP")
        print("3 - Dano")

        playerLevelUpExtraPoints = input("> ")

        if playerLevelUpExtraPoints in ("1", "2", "3"):
            return int(playerLevelUpExtraPoints)

        print("Opcao invalida!")

# prints player status
def show_player_status(player):
    print("        ---- STATUS ----")
    print("================================================")
    print(f"Jogador: {player.name} | Level: {player.playerLevel} | XP: {player.xpPoints}/{ProgressionSystem.xp_required_for_next_level(player.playerLevel)}")
    print("------------------------------------------------")
    print(f"Classe: {player.playerClass}           | Dano Base: {player.baseAttack}")
    print("------------------------------------------------")
    print(f"HP: {player.healthPoints}/{player.maxHealthPoints}")
    print(f"SP: {player.sP}/{player.maxSP}")
    print("------------------------------------------------")
    print(f"Arma: {player.equippedWeapon.weaponName} | Dano: {player.equippedWeapon.totaldmgValue} | Raridade: {player.equippedWeapon.weaponRarity}")
    print(f"Armadura: {player.equippedArmor.armorName}| Dano reduzido: {player.equippedArmor.armorDefenseValue}")
    print("------------------------------------------------")
    print(f"Key: {'Yes' if player.hasKey else 'No'}")
    print("================================================")

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
        print(f"Inventario: {player.inventoryArmor.armorName} | Dano Reduzido: {player.inventoryArmor.armorDefenseValue}")
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
            print("Selecione uma das pocoes acima")
            player_selected_potion = input("> ")

            if not player_selected_potion.isdigit():
                print("Opcao invalida!")
                continue
            # int conversion
            player_selected_potion = int(player_selected_potion)

            # validates if the potion exists in the player's inventory
            if 1 <= player_selected_potion <= len(player.potions) or player_selected_potion == 0:
                return player_selected_potion
        
            print("Opcao invalida!")   

# player chooses which weapon to discard after receiving a drop
def choose_weapon_to_discard(player, newWeapon):
    while True:
        print("Escolha uma arma para descartar:")
        print("\n* Lista de armas *")
        print("+-----------------------------------------------------------------------------------------------------------------+")
        print(f"|1 -> Equipada: {player.equippedWeapon.weaponName} | Dano: {player.equippedWeapon.totaldmgValue} | Raridade: {player.equippedWeapon.weaponRarity} |")
        print(f"|2 -> Inventario: {player.inventoryWeapon.weaponName} | Dano: {player.inventoryWeapon.totaldmgValue} | Raridade: {player.inventoryWeapon.weaponRarity} |")
        print(f"|3 -> Nova: {newWeapon.weaponName} | Dano: {newWeapon.totaldmgValue} | Raridade: {newWeapon.weaponRarity} |")
        print("+-----------------------------------------------------------------------------------------------------------------+")
        
        player_discarded_weapon = input("> ")

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
        player_discarded_armor = input("> ")

        if not player_discarded_armor.isdigit():
            print("Opcao invalida!")
            continue
        
        if player_discarded_armor in ("1", "2", "3"):
            return player_discarded_armor

        print("Opcao invalida!")

# player chooses a potion from either their inventory or the new one
def choose_max_potion_option(player, newPotion):
    # player chooses a potion
    while True:
        print("Voce nao pode carregar mais pocoes!")
        print("Selecione uma pocao\n")

        # shows player's potion and new potion
        show_player_potions(player)
        print(f"{6} -> {newPotion.potionName} | +{newPotion.potionRegenPoints} {newPotion.potionType}")

        player_selected_potion = input("> ")

        if not player_selected_potion.isdigit():
            print("Opcao invalida!")
            continue
        player_selected_potion = int(player_selected_potion)

        if 1 <= player_selected_potion <= 6:
            return player_selected_potion
        
        print("Opcao invalida!")

# player chooses to either discard or consume a potion
def choose_max_potion_action():
    while True:
        print("Deseja consumir ou descartar esta pocao?")
        print("1 -> Consumir")
        print("2 -> Descartar")

        potionOption = input("> ")

        if potionOption in ("1", "2"):
            return potionOption

        print("Opcao invalida!")                  

##################
## MAP RELATED ###
##################
# prints map
def show_map(gameMap):
    # prints map
    print(f"              Fase {gameMap.stage}\n")
    print("============= MAPA =============\n")
    draw_level_map(gameMap.root, gameMap.currentRoom)
    print("==============================")

    # prints room symbol
    print("[P] - posicao atual")
    print("[ ] - sala vazia")
    print("[X] - sala com inimigos ativos")
    print("[B] - sala do chefe")
    print("[K] - sala da chave")
    print("... - caminho inexplorado")
    print("==============================\n")
# room symbol helper
def room_symbol(room, current):

    if room is None:
        return "   "

    if not room.visited:
        return "..."

    if room == current:
        return "[P]"

    if room.cleared:

        if room.roomType == RoomType.KEY:
            return "[K]"

        if room.roomType == RoomType.EXIT:
            return "[B]"

        return "[ ]"

    return "[X]"

# positions
def compute_positions(root):

    positions = {}

    max_depth = get_depth(root)

    leaf = 0

    def visit(node, depth):

        nonlocal leaf

        if node is None:
            return None

        #
        # Unknown room
        #
        if not node.visited:

            x = leaf * LEAF_SPACING

            positions[node] = (x, depth)

            leaf += 1

            return x

        #
        # Leaf
        #
        if node.left is None and node.right is None:

            x = leaf * LEAF_SPACING

            positions[node] = (x, depth)

            leaf += 1

            return x

        #
        # Explore children
        #
        left_x = None
        right_x = None

        if node.left:
            left_x = visit(node.left, depth + 1)

        if node.right:
            right_x = visit(node.right, depth + 1)

        #
        # Center parent
        #
        if left_x is not None and right_x is not None:
            x = (left_x + right_x) // 2

        elif left_x is not None:
            x = left_x + LEAF_SPACING // 2

        else:
            x = right_x + LEAF_SPACING // 2

        positions[node] = (x, depth)

        return x

    visit(root, 0)

    return positions

# HELPER depth of the tree
def get_depth(node):

    if node is None:
        return 0

    return 1 + max(
        get_depth(node.left),
        get_depth(node.right)
    )

# draws map
def draw_level_map(root, current):

    positions = compute_positions(root)

    height = get_depth(root) * ROW_HEIGHT + 2

    canvas = [
        [" "] * CANVAS_WIDTH
        for _ in range(height)
    ]

    #
    # Draw rooms
    #
    for room, (x, depth) in positions.items():

        y = depth * ROW_HEIGHT

        text = room_symbol(room, current)

        for i, c in enumerate(text):

            if 0 <= x + i < CANVAS_WIDTH:
                canvas[y][x + i] = c

    #
    # Draw connections
    #
    for room, (x, depth) in positions.items():

        if not room.visited:
            continue

        y = depth * ROW_HEIGHT

        if room.left and room.left in positions:

            child_x, child_depth = positions[room.left]
            child_y = child_depth * ROW_HEIGHT

            canvas[y + 1][x] = "/"

        if room.right and room.right in positions:

            child_x, child_depth = positions[room.right]
            child_y = child_depth * ROW_HEIGHT

            canvas[y + 1][x + 2] = "\\"

    #
    # Print
    #
    for row in canvas:
        print("".join(row).rstrip())