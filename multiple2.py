# Movie recommendation system 

class Movie: 
    def __init__(self, title, genre): 
        self.title = title 
        self.genre = genre 

class Rating: 
    def __init__(self, rating): 
        self.rating= rating 

class MovieReview(Movie, Rating): 
    def __init__(
            self, 
            title,
            genre,
            rating
    ): 
        Movie.__init__( 
            self, 
            title,
            genre
        )

        Rating.__init__(
            self,
            rating
        )

    def recommend(self): 
        print("Movie:", self.title)
        print("Genre:", self.genre)
        print("Rating:", self.rating, "/ 10")

        if self.rating >= 8: 
            print("Highly Recommended!")
        elif self.rating >= 6: 
            print("Worth Watching!")
        else: 
            print("You can skip this one.")


movie1 = MovieReview(
    "Interstellar",
    "Sci-Fi",
    5.5
)

movie2 = MovieReview(
    "Project Hail Mary",
    "Sci-Fi",
    7.5
)

movie3 = MovieReview(
    "The Exorcist", 
    "Horror",
    9       
)

movie4 = MovieReview(
    "Bend it Like Beckham",
    "Comedy",
    9.2
)

movie5 = MovieReview(
    "Se7en", 
    "Thriller",
    9.5
)

movie1.recommend()
movie2.recommend()
movie3.recommend()
movie4.recommend()
movie5.recommend()