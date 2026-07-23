from Entities.Enemy import Enemy
import random

##############################
## list of enemies by stage ##
##############################
ENEMIES = {
    # stage 1
    1: [
        ("Rat", 12, 2, 0, 20),
        ("Skeleton", 19, 4, 0, 25),
        ("Goblin", 21, 7, 1, 30),
    ],

    # stage 2
    2: [
        ("Wolf", 14, 3, 0, 25),
        ("Zombie", 21, 6, 1, 30),
        ("Orc", 30, 8, 2, 35),
    ],

    # stage 3
    3: [
        ("Bear", 16, 5, 2, 35),
        ("Wraith", 24, 8, 3, 40),
        ("Ogre", 38, 11, 5, 45),
    ]
}
#############################
## list of bosses by stage ##
#############################
BOSSES = {

    1: ("Lich", 69, 10, 3, 100),

    2: ("Giant", 78, 12, 5, 140),

    3: ("Dragon", 92, 18, 11, 200)
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

    #switch to boss later
    return Enemy(*BOSSES[stage])