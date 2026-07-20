from Items.Potion import Potion
from Items.Armor import Armor
from Systems import InventorySystem

def open_chest(player, room):

    loot = room.chest

    if loot is None:
        print("O bau esta vazio.")
        return

    if isinstance(loot, Potion):
        print("O bau continha uma pocao!")
        InventorySystem.obtain_potion(player, loot)

    elif isinstance(loot, Armor):
        print("O bau continha uma armadura!")
        InventorySystem.obtain_armor(player, loot)

    else:
        print("O bau continha uma arma!")
        InventorySystem.obtain_weapon(player, loot)
    
    # clears room chest        
    room.chest = None