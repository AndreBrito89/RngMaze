from Entities.Enemy import Enemy
import random

##############################
## list of enemies by stage ##
##############################
ENEMIES = {
    # stage 1
    1: [
        ("Rat", 12, 3, 0, 20),
        ("Skeleton", 19, 6, 0, 25),
        ("Goblin", 21, 9, 1, 30),
    ],

    # stage 2
    2: [
        ("Wolf", 14, 4, 0, 25),
        ("Zombie", 21, 7, 1, 30),
        ("Orc", 32, 10, 2, 35),
    ],

    # stage 3
    3: [
        ("Bear", 16, 5, 2, 35),
        ("Wraith", 25, 8, 4, 40),
        ("Ogre", 38, 11, 6, 45),
    ]
}
#############################
## list of bosses by stage ##
#############################
BOSSES = {

    1: ("Lich",69,12,4,100),

    2: ("Giant",72,14,5,110),

    3: ("Dragon",80,16,11,200)
}


# creates an enemy based on the stage
def create_enemy(stage):

    enemyData = random.choice(ENEMIES[stage])

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