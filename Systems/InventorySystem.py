from Systems import UISystem

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
    selectedPotion = UISystem.choose_new_potion_option(player, newPotion)

    # asks if player wants to consume or discard the selected potion
    potionAction = UISystem.choose_potion_action()

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
def player_inventory_actions(player):

    #receives selection from UI
    selectedInventoryAction = UISystem.show_inventory_menu_options()
    
    # opens use potion menu
    if selectedInventoryAction == 1:
        use_potion(player)
    # player swaps weapons
    elif selectedInventoryAction == 2:
        UISystem.show_player_weapons(player)
        swap_weapons(player)
    # player swaps armors
    elif selectedInventoryAction == 3:
        UISystem.show_player_armors(player)
        swap_armors(player)

#############
## HELPERS ##
#############
# use potion
def use_potion(player):
    # checks if the player has any potions
    if len(player.potions) == 0:
        print("Voce nao possui pocoes!")
        return

    UISystem.show_player_potions(player)

    selectedPotion = UISystem.select_inventory_potion(player)
    # assigns the removed potion to the potion variable
    potion = player.potions.pop(selectedPotion - 1)

    player.use_potion(potion)

    print(f"Voce consumiu {potion.potionName}!")

# swap weapons
def swap_weapons(player):
    #checks if player has another weapon in the inventory
    if player.has_weapon_slot():
        print("Voce nao possui arma no inventario")
        return
    player.swap_weapons()
    print(f"Voce equipou {player.equippedWeapon.weaponName}!")

# swap armor
def swap_armors(player):
    #checks if player has another armor in the inventory
    if player.has_armor_slot():
        print("Voce nao possui armadura no inventario")
        return
    player.swap_armors()
    print(f"Voce equipou {player.equippedArmor.armorName}!")