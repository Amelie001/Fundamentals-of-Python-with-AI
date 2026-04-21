movies = (
    ("The Hunger Games", "Action", "exciting"),
    ("Inception", "Sci-Fi", "mind-blowing"),
    ("The Big Short", "Drama", "thoughtful"),
    ("Bend it Like Beckham", "Comedy", "funny"),
    ("Interstellar", "Sci-Fi", "emotional"),
    ("The Wolf of Wall Street", "Drama", "wild"),
    ("Gone Girl", "Thriller", "dark"),
    ("The Social Network", "Drama", "motivational"),
    ("Parasite", "Thriller", "dark"),
    ("Taken", "Action", "intense")
)

user_mood = input("Enter your mood (exciting, emotional, intense, dark, thoughtful, motivational, funny, wild, mind-blowing): ").lower()

print("\nRecommended movies:")

found = False

for movie in movies:
    title, genre, mood = movie  

    if mood == user_mood:
        print("-", title, "(", genre, ")")
        found = True

if not found:
    print("No movies found for that mood.")