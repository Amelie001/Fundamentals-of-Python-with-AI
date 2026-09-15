# Online Food Delivery System

class RestaurantOrder:

    def __init__(self, customer_name, order_id, item, quantity):
        self.customer_name = customer_name
        self.order_id = order_id
        self.item = item
        self.quantity = quantity

        self.price = 0
        self.delivery_charge = 0
        self.discount = 0
        self.total = 0
        self.final_bill = 0


    def calculate_total(self):
        self.total = (self.price * self.quantity) + self.delivery_charge


    def calculate_discount(self):
        return 0


    def place_order(self):

        self.calculate_total()

        self.discount = self.calculate_discount()

        self.final_bill = self.total - self.discount

        print("\n------ ORDER INVOICE ------")
        print("Customer:", self.customer_name)
        print("Order ID:", self.order_id)
        print("Item:", self.item)
        print("Quantity:", self.quantity)
        print("Price per item: £", self.price)
        print("Delivery charge: £", self.delivery_charge)
        print("Total: £", self.total)
        print("Discount: £", self.discount)
        print("Final bill: £", self.final_bill)


class PizzaOrder(RestaurantOrder):

    def __init__(self, customer_name, order_id, item, quantity):
        super().__init__(customer_name, order_id, item, quantity)

        self.price = 12
        self.delivery_charge = 3


    def calculate_discount(self):

        if self.total > 50:
            return self.total * 0.15

        return 0


class BurgerOrder(RestaurantOrder):

    def __init__(self, customer_name, order_id, item, quantity):
        super().__init__(customer_name, order_id, item, quantity)

        self.price = 8
        self.delivery_charge = 2


    def calculate_discount(self):

        if self.total > 50:
            return self.total * 0.10

        return 0


class IndianFoodOrder(RestaurantOrder):

    def __init__(self, customer_name, order_id, item, quantity):
        super().__init__(customer_name, order_id, item, quantity)

        self.price = 10
        self.delivery_charge = 4


    def calculate_discount(self):

        if self.total > 75:
            return self.total * 0.12

        return 0


pizza_order = PizzaOrder("Jane", 101, "Margherita Pizza", 2)

burger_order = BurgerOrder("Alex", 102, "Veggie Burger", 7)

indian_order = IndianFoodOrder("Sam", 103, "Chana Masala", 8)


pizza_order.place_order()

burger_order.place_order()

indian_order.place_order() 