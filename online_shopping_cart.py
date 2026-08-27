# Online Shopping Cart

class ShoppingCart:

    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name    # Public
        self._cart_id = cart_id               # Protected
        self.__total_amount = 0               # Private
        self.products = {}

    # Add a product
    def add_product(self, product, price):
        self.products[product] = price
        self.__total_amount += price
        print(product, "added to cart.")

    # Remove a product
    def remove_product(self, product):
        if product in self.products:
            price = self.products[product]
            del self.products[product]
            self.__total_amount -= price
            print(product, "removed from cart.")
        else:
            print("Product not found.")

    # Apply a discount
    def apply_discount(self, discount):
        if 0 <= discount <= 100:
            self.__total_amount -= self.__total_amount * (discount / 100)
            print(discount, "% discount applied.")
        else:
            print("Invalid discount.")

    # Return total amount
    def get_total(self):
        return self.__total_amount


# Create shopping cart
cart = ShoppingCart("Amelie", 1234)

cart.add_product("Laptop", 800)
cart.add_product("Headphones", 100)

print("Total:", cart.get_total())

cart.remove_product("Headphones")

print("Total:", cart.get_total())

cart.apply_discount(10)

print("Final Total:", cart.get_total())