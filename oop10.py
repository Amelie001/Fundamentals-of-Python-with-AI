class Product: 

    def __init__(self, name, price, quantity): 
        self.name = name 
        self.price = price 
        self.quantity = quantity

    def calculate_total(self): 
        return self.price * self.quantity 

    def display_product(self): 
        print("\nProduct:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total:", self.calculate_total())

class DiscountedProduct(Product): 

    def __init__(self, name, price, quantity, discount): 
        super().__init__(name, price, quantity)
        self.discount = discount 

    def calculate_total(self): 
        total = super().calculate_total()
        discount_amount = total * self.discount / 100 
        return total - discount_amount 

    def display_discount(self): 
        print("Discount:", self.discount, "%")

product = DiscountedProduct(
    "Wireless Headphones", 
    2500,
    2,
    15
)

product.display_product()
product.display_discount()