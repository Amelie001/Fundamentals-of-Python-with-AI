# Restaurant Ordering System 

class RestaurantOrder:

    def __init__(self, customer_name): 
        self.customer_name = customer_name
        self.items = []
        self.total = 0

    def add_item(self, item, price): 
        self.items.append(item)
        print(item, "added to the order.")
        self.total += price

    def display(self): 
        print("\nCustomer:", self.customer_name)
        print("Items ordered:")

        for item in self.items: 
            print("-", item)

        print("Total:", self.total)

order = RestaurantOrder("Amelie")

order.add_item("Pasta", 10)
order.add_item("Dumplings", 7)
order.add_item("Juice", 4)

order.display()