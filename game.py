from Factories.PlayerFactory import create_new_player
from Systems import StageLoader
from Systems import MovementSystem
from Systems import InventorySystem
from Systems import ProgressionSystem
from Systems import UISystem

player_name, player_class, player_bonus_points = UISystem.get_player_info()
player = create_new_player(player_name, player_class, player_bonus_points)

gameMap = StageLoader.load(1, player)

while True:
    # checks if player is dead
    if player.healthPoints <= 0:
        break
    # checks if player reached last stage
    if gameMap == None:
        break
    room = gameMap.currentRoom

    UISystem.show_map(gameMap)
    UISystem.show_main_menu_options(gameMap)
    choice = input("> ")

    if choice == "1":
        MovementSystem.move_left(gameMap, player)

    elif choice == "2":
        MovementSystem.move_right(gameMap, player)

    elif choice == "3":
        MovementSystem.move_back(gameMap, player)

    elif choice == "4":
        InventorySystem.player_menu_actions(player)

    elif choice == "5":
        gameMap = ProgressionSystem.try_enter_next_stage(player, gameMap)      
         
    elif choice == "0":
        break



# QOL: dmg numbers .2f

# add merchant at room 1 after defeating enemies
# merchant sells: 
#               -> every potion - OK
# merchant buys:
#               -> armors and weapons (value based on rarity) - OK
# merchant tradeup:
#               -> potion toka koka -> switches HP/SP - OK
#               -> armor toka koka -> 1 armor for 1 weapon (same tier) - OK
#               -> weapon toka koka -> 1 weapon for 1 armor (same tier) - OK
# merchant upgrades:
#               -> 2 weapons for 1 weapon next rarity (weapons must be same rarity) - OK
#               -> 2 armors for 1 armor next rarity (armors must be same rarity) - OK


#  - MERCHANT TESTING LIST -
#✅ Try to buy a potion without enough XP.
#✅ Try to swap a potion without enough XP.
#✅ Try to swap equipment without enough XP.
#✅ Try to upgrade with mismatched rarities.
#❌ Try to upgrade tier 4 equipment.
#✅ Try to upgrade tier 1 → tier 2 on Stage 1.
#✅ Try to upgrade tier 2 → tier 3 on Stage 1.
#✅ Same upgrade on Stage 2.
#❌ Try tier 3 → tier 4 upgrade on Stage 2.
#✅ Same upgrade on Stage 3.
#✅ God weapon → Gold armor swap on Stage 3.
#✅ Gold armor → God weapon swap on Stage 3.
#✅ Try selling your equipped weapon when you have no spare weapon.
#✅ Try selling your equipped armor when you have no spare armor.
#✅ Try swapping/upgrading with an empty inventory slot.


#  * BUGS FOUND *
# ->SWAPING POTIONS WITHOUT POTIONS LISTS NO POTIONS - INVESTIGATE