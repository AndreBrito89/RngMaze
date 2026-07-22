
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
            dmgBonus = 1
        if player.playerClass == "Mage":
            hpBonus = 3
            spBonus = 6
            dmgBonus = 1
    # Levels 9-10
    else:
        if player.playerClass == "Warrior":
            hpBonus = 3
            spBonus = 2
            dmgBonus = 1
        if player.playerClass == "Mage":
            hpBonus = 2
            spBonus = 3
            dmgBonus = 1

    match selectedStat:
        # HP
        case 1:
            player.maxHealthPoints += hpBonus
            player.healthPoints += hpBonus
        # SP
        case 2:
            player.maxSP += spBonus
            player.sP += spBonus
        # DMG
        case 3:
            player.baseAttack += dmgBonus