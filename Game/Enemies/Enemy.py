class Enemy:
    #constructor
    def __init__(self, healthPoints, attackDmg, armor, xpReward):
        self.healthPoints = healthPoints
        self.attackDmg = attackDmg
        self.armor = armor
        self.xpReward = xpReward
    #attack
    def attack(self):
        return self.attackDmg
    #defend
    def defend(self, dmgReceived):
        totalDmgReceived = dmgReceived - self.armor
        self.healthPoints -= totalDmgReceived
    