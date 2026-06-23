class Consumable:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, playerClass):
        raise NotImplementedError("Consumable subclasses must implement use().")


class HealthPotion(Consumable):
    def __init__(self, healAmount):
        super().__init__("Health Potion", f"Recupera {healAmount} de HP")
        self.healAmount = healAmount

    def use(self, playerClass):
        if playerClass.healthPoints >= playerClass.maxHealthPoints:
            return False, "HP ja esta no maximo."

        previous = playerClass.healthPoints
        playerClass.healthPoints = min(playerClass.maxHealthPoints, playerClass.healthPoints + self.healAmount)
        recovered = playerClass.healthPoints - previous
        return True, f"Recuperou {recovered} de HP."


class StaminaPotion(Consumable):
    def __init__(self, staminaAmount):
        super().__init__("Stamina Potion", f"Recupera {staminaAmount} de SP")
        self.staminaAmount = staminaAmount

    def use(self, playerClass):
        if playerClass.sP >= playerClass.maxSP:
            return False, "SP ja esta no maximo."

        previous = playerClass.sP
        playerClass.sP = min(playerClass.maxSP, playerClass.sP + self.staminaAmount)
        recovered = playerClass.sP - previous
        return True, f"Recuperou {recovered} de SP."
