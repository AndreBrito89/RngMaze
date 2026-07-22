from Systems import UISystem
from Systems import ProgressionSystem

# player gets a weapon drop
def obtain_weapon(player, newWeapon):
    # checks if the player have an available slot
    if player.has_weapon_slot():
        print(f"Voce recebeu {newWeapon.weaponName}!")
        player.inventoryWeapon = newWeapon
        return
    playerDiscardedWeapon = UISystem.choose_weapon_to_discard(player, newWeapon)

    match playerDiscardedWeapon:
        case "1":
            print(f"Voce descartou {player.equippedWeapon.weaponName}!\n {player.inventoryWeapon.weaponName} foi equipada!")
            player.swap_weapons()
            player.inventoryWeapon = newWeapon
        case "2":
            print(f"Voce descartou {player.inventoryWeapon.weaponName}!")
            player.inventoryWeapon = newWeapon
        case "3":
            print(f"Voce descartou {newWeapon.weaponName}!")
            pass

# player gets an armor drop
def obtain_armor(player, newArmor):
    # checks if the player have an available slot
    if player.has_armor_slot():
        print(f"Voce recebeu {newArmor.armorName}")
        player.inventoryArmor = newArmor
        return
    playerDiscardedArmor = UISystem.choose_armor_to_discard(player, newArmor)

    match playerDiscardedArmor:
        case "1":
            print(f"Voce descartou {player.equippedArmor.armorName}!\n {player.inventoryArmor.armorName} foi equipada!")
            player.swap_armors()
            player.inventoryArmor = newArmor
        case "2":
            print(f"Voce descartou {player.inventoryArmor.armorName}!")
            player.inventoryArmor = newArmor
        case "3":
            print(f"Voce descartou {newArmor.armorName}!")
            pass

    
# player gets a potion drop
def obtain_potion(player, newPotion):

    # adds potion if player does have an available slot
    if player.has_potion_slot():
        print(f"Voce recebeu {newPotion.potionName}")
        player.potions.append(newPotion)
        return
    
    # selects a potion
    selectedPotion = UISystem.choose_max_potion_option(player)

    # asks if player wants to consume or discard the selected potion
    potionAction = UISystem.choose_max_potion_action()

    if potionAction == "1" and selectedPotion < 6:
        print(f"Voce recebeu +{player.potions[selectedPotion - 1].potionRegenPoints} {player.potions[selectedPotion - 1].potionType}")
        player.use_potion(player.potions[selectedPotion - 1])
        player.potions[selectedPotion - 1] = newPotion
    
    elif potionAction == "1" and selectedPotion == 6:
        print(f"Voce recebeu +{newPotion.potionRegenPoints} {newPotion.potionType}")
        player.use_potion(newPotion)
    
    elif potionAction == "2" and selectedPotion < 6:
        print(f"Voce descartou {player.potions[selectedPotion - 1].potionName} e recebeu {newPotion.potionName}.")
        player.potions[selectedPotion - 1] = newPotion
    elif potionAction == "2" and selectedPotion == 6:
        print(f"Voce descartou {newPotion.potionName}")

# INVENTORY ACTIONS
def player_menu_actions(player):
    # shows player's status
    UISystem.show_player_status(player)

    #receives selection from UI
    selectedInventoryAction = UISystem.show_inventory_menu_options()
    
    # level up
    if selectedInventoryAction == 1:
        player_level_up(player)
    # player swaps weapons
    elif selectedInventoryAction == 2:
        weapon_options(player)
    # player swaps armors
    elif selectedInventoryAction == 3:
        armor_options(player)
    # potion options
    elif selectedInventoryAction == 4:
        potion_options(player)
    # exits inventory menu
    else:
        return


#############
## HELPERS ##
#############
# use potion
def potion_options(player):
    # checks if the player has any potions
    if len(player.potions) == 0:
        print("Voce nao possui pocoes!")
        return

    UISystem.show_player_potions(player)
    print("Gostaria de consumir uma pocao?")
    print("1 - Sim\n2 - Voltar")
    potionConsumptionOption = input()
    
    if potionConsumptionOption == "1":
        selectedPotion = UISystem.select_inventory_potion(player)
        
        # assigns the removed potion to the potion variable
        potion = player.potions.pop(selectedPotion - 1)
        player.use_potion(potion)
        print(f"Voce consumiu {potion.potionName}!")
    
# swap weapons
def weapon_options(player):
    #checks if player has another weapon in the inventory
    if player.has_weapon_slot():
        print("Voce nao possui arma no inventario")
        return
    
    UISystem.show_player_weapons(player)
    
    print("Pressione 1 para trocar de arma, qualquer outra tecla para voltar")
    weaponSwap = input()
    if weaponSwap == "1":
        player.swap_weapons()
        print(f"Voce equipou {player.equippedWeapon.weaponName}!")

# swap armor
def armor_options(player):
    #checks if player has another armor in the inventory
    if player.has_armor_slot():
        print("Voce nao possui armadura no inventario")
        return
    
    UISystem.show_player_armors(player)
    print("Pressione 1 para trocar de arma, qualquer outra tecla para voltar")
    armorSwap = input()
    if armorSwap == "1":
        player.swap_armors()
        print(f"Voce equipou {player.equippedArmor.armorName}!")

def player_level_up(player):

    # checks if player can level up
    can_player_levelup = player.level_up(ProgressionSystem.xp_required_for_next_level(player.playerLevel))

    # player selects attribute for the extra level
    if can_player_levelup:
        # selects extra point
        selectedLevelUpExtraPoints = UISystem.select_levelup_extra_point()
        # assigns extra point based on the player level
        ProgressionSystem.level_up_extra_points(player, selectedLevelUpExtraPoints)
        player.healthPoints = min(player.healthPoints + 10, player.maxHealthPoints)
        player.sP = min(player.sP + 10, player.maxSP)