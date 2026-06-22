class PlayerClassWarrior:
    #constructor
    def __init__(self, healthPoints, equipedWeapon, armor, baseAttack):
        self.healthPoints = healthPoints
        self.baseAttack = baseAttack
        self.equipedWeapon = equipedWeapon
        self.armor = armor
    #attack
    def attack(self):
        return self.equipedWeapon.totaldmgValue + self.baseAttack
    #
    def defend(self, dmgReceived):
        totalDmgReceived = dmgReceived - self.armor
        self.healthPoints -= totalDmgReceived