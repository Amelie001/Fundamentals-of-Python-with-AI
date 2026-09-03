# Food Delivery System

class Order: 

    def __init__(self, orderID, customer_name): 
        self.orderID = orderID 
        self.customer_name = customer_name 

    def show_order(self): 
        print("Order ID:", self.orderID)
        print("Customer:", self.customer_name)

class FoodOrder(Order): 

    def __init__(
            self,
            orderID, 
            customer_name,
            restaurant, 
            food_price, 
            delivery_charge
    ): 
        super().__init__(orderID, customer_name)

        self.restaurant = restaurant 
        self.food_price = food_price 
        self.delivery_charge = delivery_charge 

    def calculate_bill(self): 
        total = self.food_price + self.delivery_charge 

        print("Restaurant:", self.restaurant)
        print("Food Price: £", self.food_price)
        print("Delivery Charge: £", self.delivery_charge)
        print("Total: £", total)

class PremiumFoodOrder(FoodOrder): 

    def __init__(
            self,
            orderID,
            customer_name, 
            restaurant, 
            food_price,
            delivery_charge, 
            discount
    ): 
        super().__init__(
            orderID,
            customer_name,
            restaurant, 
            food_price, 
            delivery_charge
        )

        self.discount = discount 

    def calculate_premium_bill(self): 
        discount_amount = self.food_price * self.discount / 100 

        # Premium users get free delivery 

        final_bill = self.food_price - discount_amount 

        print("Premium Discount:", self.discount, "%")
        print("Discount Amount: £", discount_amount)
        print("Delivery Charge: £ 0")
        print("Final Bill: £", final_bill)

order = PremiumFoodOrder(
    "ORD501", 
    "Aisha",
    "Burger House", 
    15, 
    3,
    2
)

print("----- FOOD ORDER -----")

order.show_order()

print()

order.calculate_premium_bill()