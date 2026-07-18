from Items.Potion import Potion
from Items.Armor import Armor
from Systems import InventorySystem

def open_chest(player, room):

    loot = room.chest

    if loot is None:
        print("O bau esta vazio.")
        return

    if isinstance(loot, Potion):
        InventorySystem.obtain_potion(player, loot)

    elif isinstance(loot, Armor):
        InventorySystem.obtain_armor(player, loot)

    else:
        InventorySystem.obtain_weapon(player, loot)
    
    # clears room chest        
    room.chest = None