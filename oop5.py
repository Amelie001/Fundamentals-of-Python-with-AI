# Shopping Cart 

class ShoppingCart: 
    def __init__(self): 
        self.items = []

    def add_item(self, item): 
        self.items.append(item)

    def remove_item(self, item): 
        if item in self.items: 
            self.items.remove(item)

    def display(self): 
        print("\nShopping Cart")
        for item in self.items: 
            print(item)

cart = ShoppingCart()

cart.add_item("Laptop")
cart.add_item("Mouse")
cart.add_item("Keyboard")

cart.display()

cart.remove_item("Mouse")

cart.display()