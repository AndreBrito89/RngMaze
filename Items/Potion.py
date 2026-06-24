class Potion:
    def __init__(self, potionSize, potionType):
        self.potionSize = potionSize
        self.potionType = potionType
        self.potionName = f"{potionSize} {potionType} {'potion'}"
        self.setPotionRegenPoints()


    

    def setPotionRegenPoints(self):    
        if(self.potionSize == 'Small'):
            self.potionRegenPoints = 8
        if(self.potionSize == 'Large'):
            self.potionRegenPoints = 16
   