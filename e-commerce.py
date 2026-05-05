#---database--- 

customers = (
    (1, "Nameerah", "India"), 
    (2, "Amelie", "UK"), 
    (3, "Sarah", "US")
)

products = (
    ("P101", "Jewellery", 9),
    ("P102", "Jeans", 15),
    ("P103", "Shoes", 15), 
    ("P104", "Top", 7)
)

orders = (
    (1001, 1, "P101", 2),
    (1002, 2, "P103", 1),
    (1003, 1, "P104", 3),
    (1004, 3, "P102", 1),
    (1005, 2, "P101", 1)
)

#---helper functions---

def get_customer_name(cid): 
    for c in customers: 
        if c[0] == cid: 
            return c[1]
        
def get_product_details(pid): 
    for p in products: 
        if p[0] == pid: 
            return p 
        
#---view orders---

def view_orders(): 
    print("\n---All Orders---")
    for order in orders: 
        oid, cid, pid, qty = order 

        cname = get_customer_name(cid)
        product = get_product_details(pid)
        pname, price = product[1], product[2]

        total = price * qty

        print(f"Order {oid} | {cname} | {pname} x {qty} | {total} pounds")

#---customer analysis---

def customer_spending(): 
    print("\n---Customer Spending---")

    for c in customers: 
        cid, name, city = c 
        total_spent = 0 

        for o in orders: 
            oid, ocid, pid, qty = 0 
            if ocid == cid: 
                product = get_product_details(pid)
                total_spent += product[2] * qty

        print(f"{name} | Total Spent: {total_spent} pounds")

#---top customer---

def top_customer(): 
    best = ("", 0)

    for c in customers:
        cid, name, city = c 
        total = 0 

        for o in orders: 
            oid, ocid, pid, qty = 0 
            if ocid == cid: 
                product = get_product_details(pid)
                total += product|[2] * qty 

        if total > best[1]: 
            best = (name, total)

    print(f"\nTop Customer: {best[0]} | {best[1]} pounds")

#---product sales--- 

def product_sales(): 
    print("\n---Product Sales---")

    for p in products: 
        pid, name, price = p
        total_qty = 0

        for o in orders: 
            oid, cid, opid, qty = 0 

            if opid == pid: 
                total_qty += qty 

        print(f"{name} | Sold: {total_qty}")

#---revenue analysis---

def total_revenue(): 
    revenue = 0 

    for o in orders: 
        oid, cid, pid, qty = 0 
        product = get_product_details(pid)
        revenue += product[2] * qty 

    print(f"\nTotal Revenue: {revenue} pound")

#---country filter---

def filter_by_country():
    country_input = input("Enter Country: ").lower()
    print("\n---Orders from Countries---")

    for o in orders:
        oid, cid, pid, qty = o

        for c in customers:
            if c[0] == cid and c[2].lower() == country_input:
                product = get_product_details(pid)
                print(f"Order {oid} | {c[1]} | {product[1]} x {qty}")

#---ranking system--- 

def product_ranking():
    ranking = []

    for p in products:
        pid, name, price = p
        total = 0

        for o in orders:
            if o[2] == pid:
                total += o[3]

        ranking.append((name, total))

    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    print("\n---Product Ranking---")

    for i, r in enumerate(ranking, start=1):
        print(f"{i}, {r[0]} - Sold {r[1]}")

def main():
    while True:
        print("\n=== E-COMMERCE SYSTEM ===")
        print("1. View Orders")
        print("2. Customer Spending")
        print("3. Top Customer")
        print("4. Product Sales")
        print("5. Total Revenue")
        print("6. Filter by City")
        print("7. Product Ranking")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1": 
            view_orders()
        elif choice == "2": 
            customer_spending()
        elif choice == "3": 
            top_customer()
        elif choice == "4": 
            product_sales()
        elif choice == "5": 
            total_revenue()
        elif choice == "6": 
            filter_by_country()
        elif choice == "7": 
            product_ranking()
        elif choice == "8": 
            print("Exiting...")
            break 
        else: 
            print("Invalid choice.")

main()