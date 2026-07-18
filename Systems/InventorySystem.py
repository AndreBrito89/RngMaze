import UISystem

# player gets a weapon drop
def obtain_weapon(player, newWeapon):
    # checks if the player have an available slot
    if player.inventoryWeapon == None:
        player.inventoryWeapon = newWeapon
        return
    playerDiscardedWeapon = UISystem.choose_weapon_to_discard(player, newWeapon)

    match playerDiscardedWeapon:
        case "1":
            print(f"Voce descartou {player.equippedWeapon.weaponName}!\n {player.inventoryWeapon.weaponName} foi equipada!")
            player.equippedWeapon = player.inventoryWeapon
            player.inventoryWeapon = newWeapon
        case "2":
            print(f"Voce descartou {player.inventoryWeapon.weaponName}!")
            player.inventoryWeapon = newWeapon
        case "3":
            print(f"Voce descartou {newWeapon.weaponName}!")
            pass

def obtain_armor(player, newArmor):
    # checks if the player have an available slot
    if player.inventoryArmor == None:
        player.inventoryArmor = newArmor
        return
    playerDiscardedArmor = UISystem.choose_armor_to_discard(player, newArmor)

    match playerDiscardedArmor:
        case "1":
            print(f"Voce descartou {player.equippedArmor.armorName}!\n {player.inventoryArmor.armorName} foi equipada!")
            player.equippedArmor = player.inventoryArmor
            player.inventoryArmor = newArmor
        case "2":
            print(f"Voce descartou {player.inventoryArmor.armorName}!")
            player.inventoryArmor = newArmor
        case "3":
            print(f"Voce descartou {newArmor.armorName}!")
            pass

    