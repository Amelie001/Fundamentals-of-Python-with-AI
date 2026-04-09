travel_data = (
    ("Paris", ("Eiffel Tower", "Croissant", "Spring")), 
    ("India", ("Taj Mahal", "Samosa", "Summer")), 
    ("Berlin", ("Bradenburg Gate", "Pretzels", "Winter")),
    ("Egypt", ("Pyramids of Giza", "Koshary", "Autumn")), 
    ("Peru", ("Machu Picchu", "Mushroom ceviche", "Spring"))
)

print("Welcome to your travel planner!")
print("Choose a city to explore:\n")

for i in range(len(travel_data)):
    print(i + 1, ".", travel_data[i][0])

choice = int(input("\nEnter your choice number: "))
index = choice - 1 
selected_city = travel_data[index]

print("\nTravel details")
print("City:", selected_city[0])
print("Must visit:", selected_city[1][0])
print("Try food:", selected_city[1][1])
print("Best season:", selected_city[1][2])