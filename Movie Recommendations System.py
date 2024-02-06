'''4. Movie Recommendation System: Create a program that recommends movies based on user preferences. Use variables to store genre, rating, and release year. Write expressions to compare movies and suggest matches.'''

movie_type=input('Enter Movie Type:')
rating =float(input('Enter Rating of movie:'))
release_year =int(input('Enter Release year of Movie:'))

movies = [
    {"title": "Dhamal", "type": "comedy", "rating": 8.2, "release_year": 2012},
    {"title": "Dabang", "type": "action", "rating": 7.8, "release_year": 2011},
    {"title": "Pakistan Zindabad", "type": "comedy", "rating": 7.9, "release_year": 2010},
    {"title": "Ishq Murshid", "type": "drama", "rating": 8.5, "release_year": 2013},
    {"title": "Ruposh", "type": "love story", "rating": 7.2, "release_year": 2009}
]

matching_movies = []
for movie in movies:
    if (
        movie["type"] == movie_type
        and movie["rating"] >= rating
        and movie["release_year"] >=release_year
    ):
        matching_movies.append(movie["title"])

if len(matching_movies) > 0:
    print("Recommended movies based on your preferences:")
    for movie in matching_movies:
        print("- ", movie)
else:
    print("Sorry, there are no movies that match your preferences.")