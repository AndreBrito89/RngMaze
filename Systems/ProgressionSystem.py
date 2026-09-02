from Map import Room
from Systems import UISystem
from Systems import StageLoader
from Systems import MerchantSystem
from Systems import InventorySystem
from Factories import LootFactory


# ammount of xp needed for each level up
def xp_required_for_next_level(playerLevel):
    return 100 + (playerLevel - 1) * 20

# extra points gained based on player level
def level_up_extra_points(player, selectedStat):

    # Levels 2-4
    if player.playerLevel <= 4:
        if player.playerClass == "Warrior":
            hpBonus = 8
            spBonus = 4
            dmgBonus = 1
        if player.playerClass == "Mage":
            hpBonus = 4
            spBonus = 8
            dmgBonus = 2
    # Levels 5-8
    elif player.playerLevel <= 8:
        if player.playerClass == "Warrior":
            hpBonus = 6
            spBonus = 3
            dmgBonus = 2
        if player.playerClass == "Mage":
            hpBonus = 3
            spBonus = 5
            dmgBonus = 1
    # Levels 9-15
    else:
        if player.playerClass == "Warrior":
            hpBonus = 5
            spBonus = 1
            dmgBonus = 1
        if player.playerClass == "Mage":
            hpBonus = 2
            spBonus = 2
            dmgBonus = 0.5

    match selectedStat:
        # HP
        case 1:
            player.maxHealthPoints += hpBonus
        # SP
        case 2:
            player.maxSP += spBonus
        # DMG
        case 3:
            player.baseAttack += dmgBonus

# search hidden door
def search_hidden_door_action(player, gameMap):

    room = gameMap.currentRoom

    # enters merchant shop
    if room.cleared == True and room.id == 1:
        MerchantSystem.enter_shop(player, gameMap)
        return gameMap

    # checks if the enemies are still alive
    if room.enemies:
        print("Voce nao consegue vasculhar a sala com inimigos ainda vivos!")
        UISystem.clear_console()
        return gameMap
    
    # check if theres a potion in the room
    if not room.hasPlayerSearchedRoom:
        # checks if theres is a drop
        room_drop = LootFactory.room_potion_drop(LootFactory.does_room_have_potion())
        if isinstance(room_drop, str):
            room.hasPlayerSearchedRoom = True
            print(room_drop)
            UISystem.clear_console()
            return gameMap
        else:
            print("Voce encontrou uma pocao atras de uma pilha de ossos!")
            InventorySystem.obtain_potion(player, room_drop)
            UISystem.clear_console()
            room.hasPlayerSearchedRoom = True
            return gameMap

    # player enters next stage
    if player.hasKey and room.roomType == Room.RoomType.EXIT:
       return try_enter_next_stage(player, gameMap)
    
    # checks if player is on the exit room and doesnt have the key
    if not player.hasKey and room.roomType == Room.RoomType.EXIT:
        print("Voce precisa da chave.")
        UISystem.clear_console()
        return gameMap

    # checks if player already searched the room
    if room.hasPlayerSearchedRoom:
        print("Nao ha nada nesta sala, apenas rochas e ossos...")
        UISystem.clear_console()
        return gameMap


# stage progression
def try_enter_next_stage(player, gameMap):

    if gameMap.stage == 4:
        UISystem.clear_console()
        UISystem.ending_screen(player)
        return None

    player.hasKey = False

    nextStage = gameMap.stage + 1

    print(f"Entrando na fase {nextStage}...")

    return StageLoader.load(nextStage, player)