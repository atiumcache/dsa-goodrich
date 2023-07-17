class Flower: 
    
    def __init__(self, name, petalCount, price):
        """Create a new flower instance"""
        self.name = name
        self.petalCount = petalCount
        self.price = price

    def get_name(self): 
        return self.name
    
    def get_petal_count(self):
        return self.petalCount
    
    def get_price(self):
        return self.price
    
    def set_name(self, name):
        self.name = name

    def set_petal_count(self, petalCount):
        self.petalCount = petalCount
    
    def set_price(self, price):
        self.price = price

tulip = Flower('tulip', 8, 5.50)
print(tulip.get_name())