from Entities.Enemy import Enemy
import random

##############################
## list of enemies by stage ##
##############################
ENEMIES = {
    # stage 1
    1: [
        ("Rat", 12, 2, 0, 20),
        ("Skeleton", 19, 3, 0, 25),
        ("Goblin", 21, 4, 0, 30),
    ],

    # stage 2
    2: [
        ("Wolf", 14, 3, 0, 25),
        ("Zombie", 21, 6, 1, 30),
        ("Orc", 30, 8, 2, 35),
    ],

    # stage 3
    3: [
        ("Bear", 16, 7, 2, 35),
        ("Wraith", 24, 9, 2, 40),
        ("Ogre", 38, 11, 4, 45),
    ]
}
#############################
## list of bosses by stage ##
#############################
BOSSES = {

    1: ("Lich", 69, 6, 2, 160),

    2: ("Giant", 78, 12, 5, 220),

    3: ("Dragon", 92, 19, 9, 450)
}


# creates an enemy based on the stage
def create_enemy(stage, tier=None):

    if tier is None:
        enemyData = random.choice(ENEMIES[stage])
    else:
        enemyData = ENEMIES[stage][tier - 1]

# => *enemyData is equivalent to:
#
#     Enemy(
#        enemy_data[0],
#        enemy_data[1],
#        enemy_data[2],
#        ...
#    )
    return Enemy(*enemyData)

# creates a boss based on the stage
def create_boss(stage):
    return Enemy(*BOSSES[stage])