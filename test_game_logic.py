import unittest
from unittest.mock import patch

from Enemies.Enemy import Boss, Enemy
from entity_generator import EnemyGenerator, create_hero_by_role
from Player.Player import Player
from Player.PlayerClassWarrior import PlayerClassWarrior
from sprite_catalog import get_enemy_sprite_data
from Weapon.Weapon import Weapon
from game_logic import (
    attempt_player_escape,
    create_player_from_choice,
    createNewWeapon,
    list_player_consumables,
    resolve_enemy_attack,
    resolve_player_attack,
    use_player_consumable,
)
from mainTestes import read_choice


class TestGameLogic(unittest.TestCase):
    def test_sprite_catalog_returns_rat_sprite(self):
        pattern, palette = get_enemy_sprite_data("rat")

        self.assertEqual(len(pattern), 8)
        self.assertIn("B", palette)
        self.assertIn("E", palette)

    def test_sprite_catalog_fallback_for_unknown_key(self):
        pattern, palette = get_enemy_sprite_data("unknown_key")

        self.assertGreaterEqual(len(pattern), 1)
        self.assertIn("B", palette)

    def test_generate_campaign_has_boss_on_last_sector(self):
        generator = EnemyGenerator(seed=123)

        campaign = generator.generate_campaign(total_sectors=5)

        self.assertEqual(len(campaign), 5)
        self.assertIsInstance(campaign[-1], Boss)

    def test_create_hero_by_role_applies_role_label(self):
        player = create_hero_by_role("scout", "Runner")

        self.assertEqual(player.hero_role, "Scout")
        self.assertEqual(player.name, "Runner")

    @patch("builtins.input", side_effect=["x", "4", "2"])
    def test_read_choice_retries_until_valid(self, _):
        value = read_choice([1, 2, 3])
        self.assertEqual(value, 2)

    def test_enemy_defense_never_heals(self):
        enemy = Enemy("Dummy", 10, 10, 1, 5, 1)

        applied = enemy.defend(2)

        self.assertEqual(applied, 0)
        self.assertEqual(enemy.healthPoints, 10)

    def test_new_player_starts_with_consumables(self):
        player = create_player_from_choice("Hero", 1)

        consumables = list_player_consumables(player)
        names = [slot.consumable.name for _, slot in consumables]

        self.assertIn("Health Potion", names)
        self.assertIn("Stamina Potion", names)

    def test_use_health_potion_recovers_hp(self):
        player = create_player_from_choice("Hero", 1)
        player.playerClass.healthPoints = 10

        consumables = list_player_consumables(player)
        health_slot_index = None
        for slot_index, slot in consumables:
            if slot.consumable.name == "Health Potion":
                health_slot_index = slot_index
                break

        self.assertIsNotNone(health_slot_index)
        success, message = use_player_consumable(player, health_slot_index)

        self.assertTrue(success)
        self.assertIn("Recuperou", message)
        self.assertGreater(player.playerClass.healthPoints, 10)

    def test_player_defense_never_heals(self):
        weapon = Weapon(5, "Normal", "Sword")
        warrior = PlayerClassWarrior(37, 37, 15, 15, weapon, 5, 2)

        applied = warrior.defend(2)

        self.assertEqual(applied, 0)
        self.assertEqual(warrior.healthPoints, 37)

    def test_resolve_player_attack_returns_raw_and_effective_damage(self):
        weapon = Weapon(10, "Normal", "Sword")
        warrior = PlayerClassWarrior(37, 37, 15, 15, weapon, 1, 2)
        player = Player("Hero", 0, 1, warrior)
        enemy = Enemy("Rat", 12, 12, 3, 3, 20)

        raw, effective = resolve_player_attack(player, enemy)

        self.assertEqual(raw, 12)
        self.assertEqual(effective, 9)
        self.assertEqual(enemy.healthPoints, 3)

    def test_resolve_enemy_attack_returns_raw_and_effective_damage(self):
        weapon = Weapon(5, "Normal", "Sword")
        warrior = PlayerClassWarrior(37, 37, 15, 15, weapon, 2, 2)
        player = Player("Hero", 0, 1, warrior)
        enemy = Enemy("Ogre", 20, 20, 9, 1, 50)

        raw, effective = resolve_enemy_attack(player, enemy)

        self.assertEqual(raw, 9)
        self.assertEqual(effective, 7)
        self.assertEqual(player.playerClass.healthPoints, 30)

    def test_escape_success_consumes_sp(self):
        weapon = Weapon(5, "Normal", "Sword")
        warrior = PlayerClassWarrior(37, 37, 15, 15, weapon, 1, 2)
        player = Player("Hero", 0, 1, warrior)

        escaped = attempt_player_escape(player, escape_value=10)

        self.assertTrue(escaped)
        self.assertEqual(player.playerClass.sP, 5)

    def test_escape_fails_with_low_sp(self):
        weapon = Weapon(5, "Normal", "Sword")
        warrior = PlayerClassWarrior(37, 37, 15, 12, weapon, 1, 2)
        player = Player("Hero", 0, 1, warrior)

        escaped = attempt_player_escape(player, escape_value=10)

        self.assertFalse(escaped)
        self.assertEqual(player.playerClass.sP, 12)

    def test_new_weapon_is_within_expected_ranges(self):
        for _ in range(500):
            weapon = createNewWeapon()
            self.assertIn(weapon.weaponName, ["Sword", "Pike", "Mace", "Axe"])
            self.assertIn(weapon.weaponRarity, ["Normal", "Rare", "Legendary", "God"])

            if weapon.weaponRarity == "Normal":
                self.assertGreaterEqual(weapon.baseDamage, 5)
                self.assertLessEqual(weapon.baseDamage, 10)
            elif weapon.weaponRarity == "Rare":
                self.assertGreaterEqual(weapon.baseDamage, 9)
                self.assertLessEqual(weapon.baseDamage, 15)
            elif weapon.weaponRarity == "Legendary":
                self.assertGreaterEqual(weapon.baseDamage, 13)
                self.assertLessEqual(weapon.baseDamage, 19)
            elif weapon.weaponRarity == "God":
                self.assertGreaterEqual(weapon.baseDamage, 19)
                self.assertLessEqual(weapon.baseDamage, 24)

    def test_boss_drop_weapon_uses_boss_ranges(self):
        boss = Boss("Lich", 69, 69, 12, 4, 100)

        legendary_drop = boss.drop_weapon(roll_value=20)
        self.assertEqual(legendary_drop.weaponRarity, "Legendary")
        self.assertGreaterEqual(legendary_drop.baseDamage, 16)
        self.assertLessEqual(legendary_drop.baseDamage, 23)

        god_drop = boss.drop_weapon(roll_value=0)
        self.assertEqual(god_drop.weaponRarity, "God")
        self.assertGreaterEqual(god_drop.baseDamage, 22)
        self.assertLessEqual(god_drop.baseDamage, 28)


if __name__ == "__main__":
    unittest.main()
