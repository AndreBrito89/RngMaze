from dataclasses import dataclass
import random

from Enemies.Enemy import Boss, Enemy
from game_logic import create_player_from_choice


@dataclass(frozen=True)
class EnemyTemplate:
    id: str
    name: str
    max_hp: int
    attack: int
    armor: int
    xp_reward: int
    min_stage: int
    max_stage: int
    weight: int
    sprite_key: str
    is_boss: bool = False


ENEMY_TEMPLATES = [
    EnemyTemplate("rat", "Rat", 12, 3, 0, 20, 1, 2, 50, "rat"),
    EnemyTemplate("imp", "Imp", 15, 4, 0, 25, 1, 3, 35, "imp"),
    EnemyTemplate("ogre", "Ogre", 21, 9, 1, 50, 2, 4, 35, "ogre"),
    EnemyTemplate("revenant", "Revenant", 27, 11, 3, 70, 3, 5, 25, "revenant"),
    EnemyTemplate("lich_boss", "Lich", 69, 12, 4, 100, 3, 5, 100, "lich", True),
]


HERO_ROLE_CONFIGS = {
    "guardian": {"label": "Guardian", "creation_choice": 1, "description": "Foco em HP"},
    "berserker": {"label": "Berserker", "creation_choice": 2, "description": "Foco em dano"},
    "scout": {"label": "Scout", "creation_choice": 3, "description": "Foco em SP"},
    "soldier": {"label": "Soldier", "creation_choice": 0, "description": "Balanceado"},
}


def create_hero_by_role(role_key, player_name):
    role = HERO_ROLE_CONFIGS.get(role_key, HERO_ROLE_CONFIGS["soldier"])
    player = create_player_from_choice(player_name, role["creation_choice"])
    player.hero_role = role["label"]
    player.hero_role_key = role_key if role_key in HERO_ROLE_CONFIGS else "soldier"
    return player


class EnemyGenerator:
    def __init__(self, seed=None):
        self._rng = random.Random(seed)

    def _eligible_templates(self, stage, boss_only=False):
        templates = [
            template
            for template in ENEMY_TEMPLATES
            if template.min_stage <= stage <= template.max_stage and template.is_boss == boss_only
        ]

        if templates:
            return templates

        return [template for template in ENEMY_TEMPLATES if template.is_boss == boss_only]

    def _pick_template(self, stage, boss_only=False):
        templates = self._eligible_templates(stage, boss_only=boss_only)
        weights = [template.weight for template in templates]
        return self._rng.choices(templates, weights=weights, k=1)[0]

    def create_enemy_from_template(self, template):
        enemy_class = Boss if template.is_boss else Enemy
        enemy = enemy_class(
            template.name,
            template.max_hp,
            template.max_hp,
            template.attack,
            template.armor,
            template.xp_reward,
        )
        enemy.template_id = template.id
        enemy.sprite_key = template.sprite_key
        enemy.stage_min = template.min_stage
        enemy.stage_max = template.max_stage
        return enemy

    def generate_sector_enemy(self, stage, is_boss_sector=False):
        template = self._pick_template(stage, boss_only=is_boss_sector)
        return self.create_enemy_from_template(template)

    def generate_campaign(self, total_sectors):
        if total_sectors <= 0:
            return []

        campaign = []
        for stage in range(1, total_sectors + 1):
            is_boss_sector = stage == total_sectors
            campaign.append(self.generate_sector_enemy(stage, is_boss_sector=is_boss_sector))
        return campaign
