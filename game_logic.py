import random

from Consumables.Consumable import HealthPotion, StaminaPotion
from Player.Player import Player
from Player.PlayerClassWarrior import PlayerClassWarrior
from Weapon.Weapon import Weapon
from game_balance import (
    BASE_POINTS,
    BASE_WARRIOR_ARMOR,
    BASE_WARRIOR_ATTACK,
    BASE_WARRIOR_MAX_HP,
    BASE_WARRIOR_MAX_SP,
    DEFAULT_INVENTORY_SIZE,
    STARTING_WEAPON_DAMAGE_MAX,
    STARTING_WEAPON_DAMAGE_MIN,
    STARTING_WEAPON_RARITY,
    STARTING_HEALTH_POTION_HEAL,
    STARTING_HEALTH_POTION_QUANTITY,
    STARTING_STAMINA_POTION_QUANTITY,
    STARTING_STAMINA_POTION_RECOVERY,
    WEAPON_NAMES,
    WEAPON_ROLL_TABLE_DEFAULT,
)


def roll_weapon_by_table(roll_table, roll_value=None):
    if roll_value is None:
        roll_value = random.randint(0, 100)

    for minimum, maximum, rarity, damage_min, damage_max in roll_table:
        if minimum <= roll_value <= maximum:
            damage = random.randint(damage_min, damage_max)
            return rarity, damage

    raise ValueError(f"weapon roll outside table boundaries: {roll_value}")


# CREATE STARTING WEAPON
def createStartingWeapon():
    #assigns random value do the weapon
    weaponDmg = random.randint(STARTING_WEAPON_DAMAGE_MIN, STARTING_WEAPON_DAMAGE_MAX)
    #randomizes starting weapon
    weaponName = random.choice(WEAPON_NAMES)

    weapon = Weapon(weaponDmg, STARTING_WEAPON_RARITY, weaponName)
    return weapon


def createNewWeapon():
    weaponRarity, weaponDmg = roll_weapon_by_table(WEAPON_ROLL_TABLE_DEFAULT)
    weaponName = random.choice(WEAPON_NAMES)

    weapon = Weapon(weaponDmg, weaponRarity, weaponName)
    return weapon


def create_player_from_choice(playerNameInput, choice):
    basePoints = BASE_POINTS
    startingWeapon = createStartingWeapon()

    #                       Name            xp  lvl                  maxHP    hP      maxSP/sP equipedWeapon armor BA
    match choice:
        case 1:
            totalHp = BASE_WARRIOR_MAX_HP + basePoints
            player = Player(playerNameInput, 0, 1, PlayerClassWarrior(totalHp, totalHp, BASE_WARRIOR_MAX_SP, BASE_WARRIOR_MAX_SP, startingWeapon, BASE_WARRIOR_ARMOR, BASE_WARRIOR_ATTACK), DEFAULT_INVENTORY_SIZE)

        case 2:
            totalBA = BASE_WARRIOR_ATTACK + basePoints
            player = Player(playerNameInput, 0, 1, PlayerClassWarrior(BASE_WARRIOR_MAX_HP, BASE_WARRIOR_MAX_HP, BASE_WARRIOR_MAX_SP, BASE_WARRIOR_MAX_SP, startingWeapon, BASE_WARRIOR_ARMOR, totalBA), DEFAULT_INVENTORY_SIZE)

        case 3:
            totalSP = BASE_WARRIOR_MAX_SP + basePoints
            player = Player(playerNameInput, 0, 1, PlayerClassWarrior(BASE_WARRIOR_MAX_HP, BASE_WARRIOR_MAX_HP, totalSP, totalSP, startingWeapon, BASE_WARRIOR_ARMOR, BASE_WARRIOR_ATTACK), DEFAULT_INVENTORY_SIZE)

        case _:
            player = Player(playerNameInput, 0, 1, PlayerClassWarrior(BASE_WARRIOR_MAX_HP, BASE_WARRIOR_MAX_HP, BASE_WARRIOR_MAX_SP, BASE_WARRIOR_MAX_SP, startingWeapon, BASE_WARRIOR_ARMOR, BASE_WARRIOR_ATTACK), DEFAULT_INVENTORY_SIZE)

    _give_starting_consumables(player)

    return player


def _give_starting_consumables(player):
    player.inventory.add(HealthPotion(STARTING_HEALTH_POTION_HEAL), STARTING_HEALTH_POTION_QUANTITY)
    player.inventory.add(StaminaPotion(STARTING_STAMINA_POTION_RECOVERY), STARTING_STAMINA_POTION_QUANTITY)


def list_player_consumables(player):
    return player.inventory.list_usable_slots()


def use_player_consumable(player, slotIndex):
    return player.inventory.use_slot(slotIndex, player.playerClass)


def resolve_player_attack(player, enemy):
    damage = player.playerClass.attack()
    applied_damage = enemy.defend(damage)
    return damage, applied_damage


def resolve_enemy_attack(player, enemy):
    damage = enemy.attack()
    applied_damage = player.playerClass.defend(damage)
    return damage, applied_damage


def attempt_player_escape(player, escape_value=None):
    if escape_value is None:
        escape_value = random.randint(1, 100)
    return player.playerClass.escape(escape_value)
