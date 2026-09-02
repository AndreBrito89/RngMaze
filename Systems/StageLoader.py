import random
from Map.Room import RoomType
import Map.Stage1 as Stage1
import Map.Stage2 as Stage2
import Map.Stage3 as Stage3
import Map.Stage4 as Stage4
from Systems import RoomController
from Factories import LootFactory
from Factories.EnemyFactory import create_enemy
from Factories.EnemyFactory import create_boss


# stage dictionary
STAGES  = {
    1: Stage1,
    2: Stage2,
    3: Stage3,
    4: Stage4
}
# helper
def get_stage_data(stage):
    return STAGES[stage]

# load stage
def load(stage, player):
    
    # assigns current player stage to a variable
    currentStage = STAGES[stage]
    # gameMap receives an empty stage
    gameMap = currentStage.create()
    

    if gameMap.stage == 4:
        # populates last stage with 3 bosses
        populate_last_stage(gameMap, player)
    else:
        # assigns room types
        assign_room_types(gameMap, currentStage.POSSIBLE_KEY_ROOMS, currentStage.POSSIBLE_EXIT_ROOMS, currentStage.TREASURE_RATE)
        # populates map based on the room types
        populate(gameMap, player)
    
    # marks first room as visited
    gameMap.root.visited = True
    RoomController.enter_room(player, gameMap.root, gameMap)
    return gameMap
        
# populate stage based on the room type
def populate(gameMap, player):

    for room in gameMap.rooms.values():

        match room.roomType:
            # creates 1 enemy
            case RoomType.NORMAL:
                room.enemies = create_normal_encounter(gameMap.stage)

            # creates 2 enemies + chest after victory
            case RoomType.TREASURE:
                room.enemies = create_treasure_encounter(gameMap.stage)
                room.hasChest = True
                room.chest = LootFactory.create_chest(player.playerClass)

            # creates 2 enemies + chest and key after victory
            case RoomType.KEY:
                room.enemies = create_key_encounter(gameMap.stage)
                room.hasKey = True
                room.hasChest = True
                room.chest = LootFactory.create_chest(player.playerClass)

            # creates a boss with an exit door. Player can go through to the next stage if they've got the key
            case RoomType.EXIT:
                room.enemies = [create_boss(gameMap.stage)]
                room.hasChest = True
                room.hasPlayerSearchedRoom = True
                room.chest = LootFactory.create_boss_chest(player.playerClass)

# populates last stage                   
def populate_last_stage(gameMap, player):

    
    gameMap.rooms[1].roomType = RoomType.NORMAL
    gameMap.rooms[1].hasPlayerSearchedRoom = True
    gameMap.rooms[1].cleared = True

    gameMap.rooms[2].enemies = [create_boss(1)]
    gameMap.rooms[2].roomType = RoomType.NORMAL
    gameMap.rooms[2].hasChest = True
    gameMap.rooms[2].chest = LootFactory.create_boss_chest(player.playerClass)

    gameMap.rooms[3].enemies = [create_boss(2)]
    gameMap.rooms[3].roomType = RoomType.NORMAL
    gameMap.rooms[3].hasChest = True
    gameMap.rooms[3].hasKey = True
    gameMap.rooms[3].chest = LootFactory.create_boss_chest(player.playerClass)

    
    gameMap.rooms[4].enemies = [create_boss(3)]
    gameMap.rooms[4].roomType = RoomType.EXIT
    gameMap.rooms[4].hasChest = True
    gameMap.rooms[4].hasPlayerSearchedRoom = True
    gameMap.rooms[4].chest = LootFactory.create_boss_chest(player.playerClass)


# randomly assigns room types
def assign_room_types(gameMap, possibleKeys, possibleExits, treasureRate):
    # assigns key room
    roomKey = random.choice(possibleKeys)
    gameMap.rooms[roomKey].roomType = RoomType.KEY
    # assigns exit room
    roomExit = random.choice(possibleExits)
    gameMap.rooms[roomExit].roomType = RoomType.EXIT

    # iterates to assign normal and treasure rooms for the
    # other rooms
    for room in gameMap.rooms.values():
        #prevents first room from beeing a treasure room
        if room.id == 1:
            room.hasPlayerSearchedRoom = True
            continue
        # ignores exit and key rooms
        if(room.roomType == RoomType.NORMAL):
            roomRandomValue = random.randint(1,100)
            # checks for stage treasure rate
            if roomRandomValue <= treasureRate : 
                room.roomType = RoomType.TREASURE

#############
## HELPERS ##
#############

# random enemy
def create_normal_encounter(stage):
    return [
        create_enemy(stage)
    ]

# 1x tier1 enemy + random enemy
def create_treasure_encounter(stage):
    return [
        create_enemy(stage, 1),
        create_enemy(stage, random.choice([1, 2, 3]))
    ]

# 1x tier1 enemy + tier2 OR tier3
def create_key_encounter(stage):
    return [
        create_enemy(stage, 1),
        create_enemy(stage, random.choice([2, 3]))
    ]