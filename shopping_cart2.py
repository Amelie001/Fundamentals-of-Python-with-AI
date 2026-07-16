# Shopping cart

wishlist = {"Laptop", "Shoes", "Perfume"}
cart = {"Shoes", "Bottle", "Laptop"}
purchased = {"Bag", "Watch"}

while True:
    print("\n===== Shopping Cart Manager =====")
    print("1. Add product to cart")
    print("2. Remove product from cart")
    print("3. Display cart")
    print("4. Show products in both wishlist and cart")
    print("5. Show wishlist products not yet purchased")
    print("6. Show all unique products")
    print("7. Find products in exactly one list")
    print("8. Count products in each list")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product to add: ")
        cart.add(product)
        print(product, "added to cart.")

    elif choice == "2":
        product = input("Enter product to remove: ")
        if product in cart:
            cart.remove(product)
            print(product, "removed from cart.")
        else:
            print("That product is not in the cart.")

    elif choice == "3":
        print("Cart:", cart)

    elif choice == "4":
        both = wishlist.intersection(cart)
        print("In both wishlist and cart:", both)

    elif choice == "5":
        not_purchased = wishlist.difference(purchased)
        print("Wishlist products not purchased:", not_purchased)

    elif choice == "6":
        unique_products = wishlist.union(cart, purchased)
        print("All unique products:", unique_products)

    elif choice == "7":
        exactly_one = wishlist.symmetric_difference(cart).symmetric_difference(purchased)
        print("Products in exactly one list:", exactly_one)

    elif choice == "8":
        print("Wishlist count:", len(wishlist))
        print("Cart count:", len(cart))
        print("Purchased count:", len(purchased))

    elif choice == "9":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")