class Potion:
    #constructor
    def __init__(self, potionSize, potionType):
        self.potionSize = potionSize
        self.potionType = potionType
        self.potionName = f"{potionSize} {potionType} {'potion'}"
        self.set_potion_regen_points()

    # assigns regen values based on the size
    def set_potion_regen_points(self):    
        if(self.potionSize == 'Small'):
            self.potionRegenPoints = 8
        if(self.potionSize == 'Large'):
            self.potionRegenPoints = 16
   