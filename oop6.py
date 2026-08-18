# Laptop 

class Laptop: 
    def __init__(self, brand, processor, ram, price):
        self.brand = brand 
        self.processor = processor 
        self.ram = ram 
        self.price = price 

    def display(self): 
        print("\nBrand:", self.brand)
        print("Processor:", self.processor)
        print("RAM:", self.ram)
        print("Price:", self.price)

    def discount(self, percent): 
        self.price = self.price - (self.price * percent / 100)
        print("New price:", self.price)

lap1 = Laptop("Dell", "i5", 16, 1000)

lap1.display()
lap1.discount(10)
lap1.display()