######################
#### TIER TABLES #####
######################
WEAPONS_TIER = {
    "Normal": 1,
    "Rare": 2,
    "Legendary": 3,
    "God": 4
}
ARMORS_TIER = {
    "Leather": 1,
    "Iron": 1,
    "Bronze": 2,
    "Silver": 3,
    "Gold": 4
}
TIER_TO_WEAPON = {
    1: "Normal",
    2: "Rare",
    3: "Legendary",
    4: "God"
}

TIER_TO_ARMOR = {
    1: "Leather",
    1: "Iron",      
    2: "Bronze",
    3: "Silver",
    4: "Gold"
}
##########################
### TRANSACTION VALUES ###
##########################

# SELLING/BUYING
POTIONS_SELL_PRICE = {
    "Small": 25,
    "Large": 40
}
WEAPON_SELL_PRICE = {
    "Normal": 50,
    "Rare": 85,
    "Legendary": 160,
    "God": 360
}
ARMOR_SELL_PRICE = {
    "No": 10,
    "Leather": 40,
    "Iron": 60,
    "Bronze": 120,
    "Silver": 200,
    "Gold": 360
}
# SWAPS
POTIONS_SWAP_PRICE = {
    "Small": 10,
    "Large": 20
}
WEAPON_SWAP_PRICE = {
    "Normal": 35,
    "Rare": 80,
    "Legendary": 150,
    "God": 260   
}
ARMOR_SWAP_PRICE = {
    "Leather": 35,
    "Iron": 35,
    "Bronze": 80,
    "Silver": 150,
    "Gold": 260
}
# UPGRADES
WEAPON_UPGRADE_PRICE = {
    "Normal": 80,
    "Rare": 160,
    "Legendary": 260,
}
ARMOR_UPGRADE_PRICE = {
    "Leather": 90,
    "Iron": 90,
    "Bronze": 180,
    "Silver": 280,
}

###################
#### FUNCTIONS ####
###################

# selling

# potions
def potion_sell_price(potion):
    return POTIONS_SELL_PRICE[potion.potionSize]
# weapons
def weapon_sell_price(weapon):
    return WEAPON_SELL_PRICE[weapon.weaponRarity]
# armor
def armor_sell_price(armor):
    return ARMOR_SELL_PRICE[armor.armorName]

# swaping

# potions
def potion_swap_price(potion):
    return POTIONS_SWAP_PRICE[potion.potionSize]
# weapons
def weapon_swap_price(weapon):
    return WEAPON_SWAP_PRICE[weapon.weaponRarity]
# armor
def armor_swap_price(armor):
    return ARMOR_SWAP_PRICE[armor.armorName]

# upgrades

# weapon
def weapon_upgrade_price(weapon):
    return WEAPON_UPGRADE_PRICE[weapon.weaponRarity]
# armor
def armor_upgrade_price(armor):
    return ARMOR_UPGRADE_PRICE[armor.armorName]

# helpers
def armor_name_from_tier(tier):
    return TIER_TO_ARMOR[tier]
def weapon_rarity_from_tier(tier):
    return TIER_TO_WEAPON[tier]