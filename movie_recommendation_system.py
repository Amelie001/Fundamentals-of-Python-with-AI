# Movie recommendation system 

print("MOVIE RECOMMENDATION SYSTEM")

action = {
    "Avengers",
    "John Wick",
    "Batman",
    "Mission Impossible",
    "Mad Max",
    "Terminator",
    "The Matrix",
    "Top Gun",
    "The Bourne Identity",
    "Kill Bill"
}

comedy = { 
    "Mr Bean",
    "Jumanji",
    "Home Alone",
    "Free Guy",
    "The Mask",
    "Bend it Like Beckham",
    "Clueless",
    "Airplane!"
}

scifi = {
    "Avatar",
    "Interstellar",
    "Dune",
    "Avengers",
    "The Matrix",
    "Terminator",
    "Jurassic Park"
}

horror = {
    "Conjuring",
    "Evil Dead",
    "Insidious",
    "Smile",
    "The Exorcist",
    "Sinister",
    "Host",
    "The Silence of the Lambs",
    "Halloween",
    "Psycho"
}

thriller = {
    "The Dark Knight",
    "Psycho",
    "Seven",
    "The Silence",
    "Zodiac",
    "The Silence of the Lambs",
    "Gone Girl",
    "The Shutter",
    "Get Out",
    "Nightcrawler"
}

drama = {
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "The Lord of the Rings",
    "Forrest Gump",
    "All Quiet on the Western Front",
    "The Karate Kid",
    "The Drama"
}

while True: 
    print("\n========== MENU ==========")
    print("1. View Action Movies")
    print("2. View Comedy Movies")
    print("3. View Sci-Fi Movies")
    print("4. View Horror Movies")
    print("5. View Thriller Movies")
    print("6. View Drama Movies")
    print("7. Search Movie")
    print("8. Show Movies in Multiple Genre")
    print("9. Show All Movies")
    print("10. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1: 
        print("\nAction Movies:")
        for movie in action:
            print("-", movie)

    elif choice == 2: 
        print("\nComedy Movies:")
        for movie in comedy:
            print("-", movie)

    elif choice == 3:
        print("\nSci-Fi Movies:")
        for movie in scifi: 
            print("-", movie)

    elif choice == 4:
        print("\nHorror Movies:")
        for movie in horror: 
            print("-", movie)

    elif choice == 5:
        print("\nThriller Movies:")
        for movie in thriller: 
            print("-", movie)

    elif choice == 6:
        print("\nDrama Movies:")
        for movie in drama: 
            print("-", movie)

    elif choice == 7:
        movie_name = input("\nEnter movie name: ")

        if movie_name in action:
            print(f"{movie_name} is in Action genre.")

        if movie_name in comedy: 
            print(f"{movie_name} is in Comedy genre.")

        if movie_name in scifi: 
            print(f"{movie_name} is in Sci-Fi genre.")

        if movie_name in horror: 
            print(f"{movie_name} is in Horror genre.")

        if movie_name in thriller: 
            print(f"{movie_name} is in Thriller genre.")

        if movie_name in drama: 
            print(f"{movie_name} is in Drama genre.")

        if (movie_name not in action and
            movie_name not in comedy and
            movie_name not in scifi):
            print("Movie not found.")

    elif choice == 8:
        common_movies = action & scifi 

        print("\nMovies in Action and Sci-Fi:")
        if len(common_movies) > 0: 
            for movie in common_movies: 
                print("-", movie)
        else: 
            print("No common movies found.")

    elif choice == 9: 
        all_movies = action | comedy | scifi | horror | thriller | drama

        print("\nAll Available Movies:")
        for movie in sorted(all_movies):
            print("-", movie)

        print("\nTotal Unique Movies:", len(all_movies))

    elif choice == 10:
        print("\nThank you for using Movie Recommendation System!")
        break

    else: 
        print("Invalid choice. Please try again.")