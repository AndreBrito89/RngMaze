from Systems import EconomySystem
from Systems import InventorySystem
from Systems import UISystem
from Factories import LootFactory
# main menu
def enter_shop(player, stageData):

    UISystem.clear_console()
    selectedMerchantAction = UISystem.merchant_main_menu()

    match selectedMerchantAction:
        # sell potion
        case 1:
            sell_potion(player)
        # swap potion
        case 2:
            swap_potion(player)
        # buy equipment
        case 3:
            buy_menu(player)
        # swap equipment
        # upgrade equipment
        # exit merchant
        case 6:
            print("Ate nosso proximo encontro, hehe...")
            return


# merchant sells potions
def sell_potion(player):

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
def swap_potion(player):
    print("Esses são meus valores, sem barganhas...")
    print("Small - 10 xp\nLarge - 20 xp")

    UISystem.show_player_potions(player)
    selectedSwapPotion = UISystem.select_inventory_potion(player)
    # checks if selected potion is valid
    if selectedSwapPotion == 0:
        return
    
    # removes the potion from the player
    selectedSwapPotion = player.potions.pop(selectedSwapPotion - 1)
    potionSwapCost = EconomySystem.potion_swap_price(selectedSwapPotion)

    # checks if player has enough xp points
    if player.xpPoints < potionSwapCost:
        print("Voce nao tem xp suficientes!")
        return
    # player pays swap cost
    player.xpPoints -= potionSwapCost
    # swaps potion type
    if selectedSwapPotion.potionType == "HP":
        newPotion_Type = "SP"
        newPotion_Size = selectedSwapPotion.potionSize
    elif selectedSwapPotion.potionType == "SP":
        newPotion_Type = "HP"
        newPotion_Size = selectedSwapPotion.potionSize

    InventorySystem.obtain_potion(player, LootFactory.potion_generator(newPotion_Size, newPotion_Type))

# buys equipment from the player
def buy_menu(player):

    selectedEquipmentType = UISystem.merchant_buy_equipment()

    # buys weapon
    if selectedEquipmentType == 1:
        # checks if player has an extra weapon to sell
        if not player.has_weapon_slot():
            print("Voce nao pode vender a arma equipada!")
            return
        else:
            buy_weapon(player)
    # buys armor
    elif selectedEquipmentType == 2:
        # checks if player has an extra armor to sell
        if not player.has_armor_slot():
            print("Voce nao pode vender a armadura equipada")
        else:
            buy_armor(player)
    # return to previous menu
    else:
        return
    
# buys weapon
def buy_weapon(player):
    # Shows prices for each rarity
    for tier, value in EconomySystem.WEAPON_PRICE.items():
        print(f"{tier}: {value} xp")
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
    # Shows prices for each rarity
    for tier, value in EconomySystem.ARMOR_PRICE.items():
        print(f"{tier}: {value} xp")
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

    
    