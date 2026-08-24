from Systems import EconomySystem
from Systems import InventorySystem
from Systems import UISystem
from Systems import StageLoader
from Factories import LootFactory
from Factories import WeaponFactory
# main menu
def enter_shop(player, gameMap):

    player_is_shopping = True

    while player_is_shopping:
        stageData = StageLoader.get_stage_data(gameMap.stage)
        UISystem.clear_console()
        selectedMerchantAction = UISystem.merchant_main_menu()

        match selectedMerchantAction:
            # sell potion
            case 1:
                merchant_sell_potion(player)
            # swap potion
            case 2:
                merchant_swap_potion(player)
            # buy equipment
            case 3:
                merchant_buy_menu(player)
            # swap equipment
            case 4:
                merchant_equipment_swap_menu(player, stageData)
            # upgrade equipment
            case 5:
                merchant_equipment_upgrade_menu(player, stageData)
            # exit merchant
            case 6:
                print("Ate nosso proximo encontro, hehe...")
                player_is_shopping = False


# merchant sells potions
def merchant_sell_potion(player):

    # prints player's current xp
    print("-------------------------------------")
    print(f"Voce tem : {player.xpPoints} xp.\n")
    print("-------------------------------------\n")

    print(" - Tabela de Precos - ")
    print("* Small Potions - 25 xp * ")
    print("* Large Potions - 40 xp * \n")

    potionSize = UISystem.merchant_sell_potion_size_selection()

    # checks the potion size
    if 1 <= potionSize <= 2:
        if potionSize == 1:
            potionSize = "Small"
        else:
            potionSize = "Large"

        potionType = UISystem.merchant_sell_potion_type_selection()

        # checks the potion type
        if 1 <= potionType <= 2:
            if potionType == 1:
                potionType = "HP"
            else:
                potionType = "SP"
        else:
            return
    else:
        return

    newPotion = LootFactory.potion_generator(potionSize, potionType)

    potionCost = EconomySystem.potion_sell_price(newPotion)

    if player.xpPoints < potionCost:
        print("Voce nao tem xp suficientes!")
        return
    else:
        player.xpPoints -= potionCost
        InventorySystem.obtain_potion(player, newPotion)

# swap potion type
def merchant_swap_potion(player):

    if not player.potions:
        print("EI! Voce nao tem nenhuma pocao para trocar no momento...")
        return

    # prints player's current xp
    print("-------------------------------------")
    print(f"Voce tem : {player.xpPoints} xp.\n")
    print("-------------------------------------\n")

    print("Esses são meus valores, sem barganhas...")
    print("Small - 10 xp\nLarge - 20 xp")
    
    UISystem.show_player_potions(player)
    selectedSwapPotion = UISystem.select_inventory_potion(player)
    # checks if selected potion is valid
    if selectedSwapPotion == 0:
        return
    # calculates the swap cost
    selectedPotion = player.potions[selectedSwapPotion - 1]
    potionSwapCost = EconomySystem.potion_swap_price(selectedPotion)

    # checks if player has enough xp points
    if player.xpPoints < potionSwapCost:
        print("Voce nao tem xp suficientes!")
        return  
    
    # player pays swap cost
    player.xpPoints -= potionSwapCost

    # removes the potion from the player
    selectedSwapPotion = player.potions.pop(selectedSwapPotion - 1)

    # swaps potion type
    if selectedSwapPotion.potionType == "HP":
        newPotion_Type = "SP"
        newPotion_Size = selectedSwapPotion.potionSize
    elif selectedSwapPotion.potionType == "SP":
        newPotion_Type = "HP"
        newPotion_Size = selectedSwapPotion.potionSize

    InventorySystem.obtain_potion(player, LootFactory.potion_generator(newPotion_Size, newPotion_Type))

# buys equipment from the player
def merchant_buy_menu(player):
    # prints player's current xp
    print("-------------------------------------")
    print(f"Voce tem : {player.xpPoints} xp.\n")
    print("-------------------------------------\n")

    selectedEquipmentType = UISystem.merchant_buy_equipment()

    # buys weapon
    if selectedEquipmentType == 1:
        # checks if player has an extra weapon to sell
        if  player.has_weapon_slot():
            print("Eu nao te deixaria sozinho nesta caverna sem uma arma...")
            return
        else:
            buy_weapon(player)
    # buys armor
    elif selectedEquipmentType == 2:
        # checks if player has an extra armor to sell
        if  player.has_armor_slot():
            print("Eu nao te deixaria sozinho nesta caverna sem uma armadura...")
        else:
            buy_armor(player)
    # return to previous menu
    else:
        return
    
# buys weapon
def buy_weapon(player):

    # Shows prices for each rarity
    print("Quanto eu pago por uma arma?")
    print("           - Tabela de Precos - ")
    print("---------------------------------------------")
    for tier, value in EconomySystem.WEAPON_SELL_PRICE.items():
        print(f"{tier}: {value} xp")
    print("---------------------------------------------")
    print("Estes sao meus valores, sem barganhas...")

    
    #player selects weapon-> swap weapons if equipped weapon was sold-> complete transaction
    selectedWeapon = UISystem.merchant_buy_weapon_selection(player)

    if selectedWeapon == 1:
        selectedWeapon = player.equippedWeapon
        #swaps player weapon and removes the sold weapon
        player.swap_weapons()
        player.inventoryWeapon = None
    elif selectedWeapon == 2:
        selectedWeapon = player.inventoryWeapon
        #removes sold weapon
        player.inventoryWeapon = None
    else:
        return

    weaponValue = EconomySystem.weapon_sell_price(selectedWeapon)
    player.xpPoints += weaponValue
    print(f"Voce recebeu {weaponValue} xp.")
    
# buys armor
def buy_armor(player):
    print("Quanto eu pago por uma armadura?")
    # Shows prices for each rarity
    print("           - Tabela de Precos - ")
    print("---------------------------------------------")
    for tier, value in EconomySystem.ARMOR_SELL_PRICE.items():
        print(f"{tier}: {value} xp")
    print("---------------------------------------------")
    print("Estes sao meus valores, sem barganhas...")

    selectedArmor = UISystem.merchant_buy_armor_selection(player)

    if selectedArmor == 1:
        selectedArmor = player.equippedArmor
        #swaps player weapon and removes the sold armor
        player.swap_armors()
        player.inventoryArmor = None
    elif selectedArmor == 2:
        selectedArmor = player.inventoryArmor
        #removes sold armor
        player.inventoryArmor = None
    else:
        return

    armorValue = EconomySystem.armor_sell_price(selectedArmor)
    player.xpPoints += armorValue
    print(f"Voce recebeu {armorValue} xp.")

# equipment swap menu
def merchant_equipment_swap_menu(player, stageData):

    # prints player's current xp
    print("-------------------------------------")
    print(f"Voce tem : {player.xpPoints} xp.\n")
    print("-------------------------------------\n")


    selectedEquipment = UISystem.merchant_swap_equipment_menu()

    # SWAPS WEAPON        
    if selectedEquipment == 1:
        if player.has_weapon_slot():
            print("Eu nao te deixaria sozinho nesta caverna sem uma arma...")
            return
        # Shows prices for each rarity
        print("Valores para troca por raridade")
        for tier, value in EconomySystem.WEAPON_SWAP_PRICE.items():
            print(f"{tier}: {value} xp")
        print("Estes sao meus valores, sem barganhas...\n")

        selectedEquipment = UISystem.merchant_swap_weapon_selection(player)

        if selectedEquipment == 1:
            selectedEquipment = player.equippedWeapon
            if can_merchant_swap(EconomySystem.WEAPONS_TIER[selectedEquipment.weaponRarity], stageData):
                # calculates the cost
                swapCost = EconomySystem.weapon_swap_price(selectedEquipment)
                # checks if player can pay the transaction
                if player.xpPoints < swapCost:
                    print("Voce nao tem xp suficientes para a troca!")
                    return

                # checks weapon rarity for the armor swap
                newArmorTier = EconomySystem.WEAPONS_TIER[selectedEquipment.weaponRarity]
                newArmor = LootFactory.armor_generator(EconomySystem.armor_name_from_tier(newArmorTier))

                # removes weapon
                player.swap_weapons()
                player.inventoryWeapon = None

                # player pays the cost
                player.xpPoints -= swapCost

                # player receives new armor
                InventorySystem.obtain_armor(player, newArmor)
                
        elif selectedEquipment == 2:
            selectedEquipment = player.inventoryWeapon
            if can_merchant_swap(EconomySystem.WEAPONS_TIER[selectedEquipment.weaponRarity], stageData):
                # calculates the cost
                swapCost = EconomySystem.weapon_swap_price(selectedEquipment)
                # checks if player can pay the transaction
                if player.xpPoints < swapCost:
                    print("Voce nao tem xp suficientes para a troca!")
                    return
                
                # checks weapon rarity for the armor swap
                newArmorTier = EconomySystem.WEAPONS_TIER[selectedEquipment.weaponRarity]
                newArmor = LootFactory.armor_generator(EconomySystem.armor_name_from_tier(newArmorTier))
                
                # player pays the cost
                player.xpPoints -= swapCost

                # removes inventory weapon
                player.inventoryWeapon = None
                
                # player receives new armor
                InventorySystem.obtain_armor(player, newArmor)
                
    # SWAPS ARMOR        
    elif selectedEquipment == 2:
        if player.has_armor_slot():
            print("Eu nao te deixaria sozinho nesta caverna sem sua armadura...")
            return

        # Shows prices for each rarity
        print("Valores para troca por raridade")
        print("           - Tabela de Precos - ")
        print("---------------------------------------------")
        for tier, value in EconomySystem.ARMOR_SWAP_PRICE.items():
            print(f"{tier}: {value} xp")
        print("---------------------------------------------")
        print("Estes sao meus valores, sem barganhas...\n")
        selectedEquipment = UISystem.merchant_swap_armor_selection(player)

        if selectedEquipment == 1:
            selectedEquipment = player.equippedArmor
            if can_merchant_swap(EconomySystem.ARMORS_TIER[selectedEquipment.armorName], stageData):
                # calculates the cost
                swapCost = EconomySystem.armor_swap_price(selectedEquipment)

                # checks if player can pay the transaction
                if player.xpPoints < swapCost:
                    print("Voce nao tem xp suficientes para a troca!")
                    return

                # checks armor rarity for the weapon swap
                newWeaponTier = EconomySystem.ARMORS_TIER[selectedEquipment.armorName]
                newWeaponRarity = EconomySystem.weapon_rarity_from_tier(newWeaponTier)

                # checks player class
                if player.playerClass == "Mage":
                    newWeapon = WeaponFactory.catalyst_generator(newWeaponRarity)
                elif player.playerClass == "Warrior":
                    newWeapon = WeaponFactory.melee_weapon_generator(newWeaponRarity)

                # player pays the cost
                player.xpPoints -= swapCost

                # removes armor
                player.swap_armors()
                player.inventoryArmor = None

                # player receives new weapon
                InventorySystem.obtain_weapon(player, newWeapon)

        elif selectedEquipment == 2:
            selectedEquipment = player.inventoryArmor
            if can_merchant_swap(EconomySystem.ARMORS_TIER[selectedEquipment.armorName], stageData):
                # calculates the cost
                swapCost = EconomySystem.armor_swap_price(selectedEquipment)
                # checks if player can pay the transaction
                if player.xpPoints < swapCost:
                    print("Voce nao tem xp suficientes para a troca!")
                    return

                # checks armor rarity for the weapon swap
                newWeaponTier = EconomySystem.ARMORS_TIER[selectedEquipment.armorName]
                newWeaponRarity = EconomySystem.weapon_rarity_from_tier(newWeaponTier)

                # checks player class
                if player.playerClass == "Mage":
                    newWeapon = WeaponFactory.catalyst_generator(newWeaponRarity)
                elif player.playerClass == "Warrior":
                    newWeapon = WeaponFactory.melee_weapon_generator(newWeaponRarity)

                # removes inventory armor
                player.inventoryArmor = None

                # player pays the cost
                player.xpPoints -= swapCost

                # player receives new weapon
                InventorySystem.obtain_weapon(player, newWeapon)
                
    # CLOSES SWAP MENU
    else:
        return


# equipment UPGRADE menu
def merchant_equipment_upgrade_menu(player, stageData):
    # prints player's current xp
    print("-------------------------------------")
    print(f"Voce tem : {player.xpPoints} xp.\n")
    print("-------------------------------------\n")

    # player selects to upgrade weapon or armor
    selectedEquipment = UISystem.merchant_upgrade_equipment_menu()

    # UPGRADES WEAPON        
    if selectedEquipment == 1:
        if player.has_weapon_slot():
            print("Voce precisa de duas armas para melhora-las...")
            return

        # Shows prices for each rarity
        print("           - Tabela de Precos - ")
        print("---------------------------------------------")
        print("Valores para upgrade por raridade")
        for tier, value in EconomySystem.WEAPON_UPGRADE_PRICE.items():
            print(f"{tier}: {value} xp")
        print("---------------------------------------------")
        print("Estes sao meus valores, sem barganhas...\n")

        # checks if both weapons are the same tier
        equippedWeaponTier = EconomySystem.WEAPONS_TIER[player.equippedWeapon.weaponRarity]
        inventoryWeaponTier = EconomySystem.WEAPONS_TIER[player.inventoryWeapon.weaponRarity]
        if not equippedWeaponTier == inventoryWeaponTier:
            print("Suas duas armas precisam ter a mesma raridade, desculpe...")
            return
        # checks if transaction is available
        if can_merchant_upgrade(equippedWeaponTier, stageData):
                upgradeCost = EconomySystem.weapon_upgrade_price(player.equippedWeapon)
                # checks if player can pay the transaction
                if player.xpPoints >= upgradeCost:
                    # player pays the cost
                    player.xpPoints -= upgradeCost

                    # removes both player's weapons and save the rarity
                    oldWeaponsRarity = player.equippedWeapon.weaponRarity
                    player.equippedWeapon = None
                    player.inventoryWeapon = None

                    # checks weapon rarity for the armor swap
                    newWeaponTier = EconomySystem.WEAPONS_TIER[oldWeaponsRarity]
                    if player.playerClass == 'Mage':
                        newWeapon = WeaponFactory.catalyst_generator(EconomySystem.weapon_rarity_from_tier(newWeaponTier + 1))
                    elif player.playerClass == 'Warrior':
                        newWeapon = WeaponFactory.melee_weapon_generator(EconomySystem.weapon_rarity_from_tier(newWeaponTier + 1))

                    # player receives and equips new weapon
                    print("Esta bem, se afaste enquanto eu trabalho...")
                    UISystem.clear_console()
                    print("Plim! Plim! Plom!")
                    print("Melhorae irmom!")
                    UISystem.clear_console()
                    InventorySystem.obtain_weapon(player, newWeapon)
                    player.swap_weapons()
                else:
                    print("Voce nao tem xp suficientes para a melhoria!")
                    return
        
    # UPGRADES ARMOR        
    elif selectedEquipment == 2:
        if player.has_armor_slot():
            print("Voce precisa de duas armaduras para melhora-las...")
            return

        # Shows prices for each rarity
        print("           - Tabela de Precos - ")
        print("---------------------------------------------")
        print("Valores para upgrade por raridade")
        for tier, value in EconomySystem.ARMOR_UPGRADE_PRICE.items():
            print(f"{tier}: {value} xp")
        print("---------------------------------------------")
        print("Estes sao meus valores, sem barganhas...\n")
        
        # checks if both armors are the same tier
        equippedArmorTier = EconomySystem.ARMORS_TIER[player.equippedArmor.armorName]
        inventoryArmorTier = EconomySystem.ARMORS_TIER[player.inventoryArmor.armorName]
        if not equippedArmorTier == inventoryArmorTier:
            print("Suas duas armaduras precisam ter a mesma raridade, desculpe...")
            return
        if can_merchant_upgrade(EconomySystem.ARMORS_TIER[player.equippedArmor.armorName], stageData):
            # calculates the cost
            upgradeCost = EconomySystem.armor_upgrade_price(player.equippedArmor)
            # checks if player can pay the transaction
            if player.xpPoints >= upgradeCost:
                # player pays the cost
                player.xpPoints -= upgradeCost
                # removes player's armors and save the name
                oldArmorsName = player.equippedArmor.armorName
                player.equippedArmor = None
                player.inventoryArmor = None
                # checks armor rarity for the weapon swap
                newArmorTier = EconomySystem.ARMORS_TIER[oldArmorsName]
                newArmorName = EconomySystem.armor_name_from_tier(newArmorTier + 1)
                newArmor = LootFactory.armor_generator(newArmorName)

                # player receives and equips new armor
                print("Esta bem, se afaste enquanto eu trabalho...")
                UISystem.clear_console()                
                print("Plim! Plim! Plom!")
                print("Melhorae irmom!")
                UISystem.clear_console()
                InventorySystem.obtain_armor(player, newArmor)
                player.swap_armors()
            else:
                print("Voce nao tem xp suficientes para a melhoria!")
                return
    # CLOSES UPGRADE MENU
    else:
        return

# helpers
def can_merchant_swap(equipmentTier, stageData):
    if stageData.MERCHANT_MAX_TRANSACTION_TIER >= equipmentTier:
        return True
    else:
        print("Desculpe, nao sei fazer isso muito bem, este equipamento e muito poderoso para mim...")
        print("Talvez na proxima fase...")
        return False
def can_merchant_upgrade(equipmentTier, stageData):
    if stageData.MERCHANT_MAX_TRANSACTION_TIER >= equipmentTier + 1:
        return True
    else:
        print("Desculpe, nao sei fazer isso muito bem, este equipamento e muito poderoso para mim...")
        print("Talvez na proxima fase...")
        return False