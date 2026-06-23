from Player.Inventory import Inventory


class Player:
    def __init__(self, name, xpPoints, playerLevel, playerClass, inventorySize=6):
        self.name = name
        self.xpPoints = xpPoints
        self.playerLevel = playerLevel
        self.playerClass = playerClass
        self.inventory = Inventory(inventorySize)
    