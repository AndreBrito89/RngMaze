class Potion:
    #constructor
    def __init__(self, potionSize, potionType):
        self.potionSize = potionSize
        self.potionType = potionType
        self.potionName = f"{potionSize} {potionType} {'potion'}"
        self.setPotionRegenPoints()

    # assigns regen values based on the size
    def setPotionRegenPoints(self):    
        if(self.potionSize == 'Small'):
            self.potionRegenPoints = 8
        if(self.potionSize == 'Large'):
            self.potionRegenPoints = 16
   