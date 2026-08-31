from Map import Room
from Systems import UISystem
from Systems import StageLoader
from Systems import MerchantSystem

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

# stage progression
def try_enter_next_stage(player, gameMap):

    room = gameMap.currentRoom

    if room.cleared == True and room.id == 1:
        MerchantSystem.enter_shop(player, gameMap)
        return gameMap

    if room.roomType != Room.RoomType.EXIT:
        print("A porta secreta nao esta nesta sala.")
        return gameMap

    if room.enemies:
        print("O chefe ainda esta vivo!")
        return gameMap

    if not player.hasKey:
        print("Voce precisa da chave.")
        return gameMap

    if gameMap.stage == 4:
        UISystem.clear_console()
        UISystem.ending_screen(player)
        return None

    player.hasKey = False

    nextStage = gameMap.stage + 1

    print(f"Entrando na fase {nextStage}...")

    return StageLoader.load(nextStage, player)