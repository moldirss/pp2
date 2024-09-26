# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
# 1. Function to check if a movie's IMDB score is above 5.5
def is_high_score(movie):
    return movie['imdb'] > 5.5

# 2. Function to return a sublist of movies with an IMDB score above 5.5
def high_score_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

# 3. Function to return movies under a specific category
def movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

# 4. Function to compute the average IMDB score of all movies
def average_imdb(movies):
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

# 5. Function to compute the average IMDB score for a specific category
def average_imdb_by_category(movies, category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    if category_movies:
        total_score = sum(movie['imdb'] for movie in category_movies)
        return total_score / len(category_movies)
    return 0

# Example Usage:

# 1. Check if the first movie's IMDB score is above 5.5
print(is_high_score(movies[0]))  # Output: True for "Usual Suspects"

# 2. Get the list of movies with an IMDB score above 5.5
high_score_list = high_score_movies(movies)
print(f"Movies with an IMDB score above 5.5: {len(high_score_list)}")
for movie in high_score_list:
    print(f"{movie['name']} - {movie['imdb']}")

# 3. Get the list of Romance movies
romance_movies = movies_by_category(movies, "Romance")
print("\nRomance Movies:")
for movie in romance_movies:
    print(f"{movie['name']} - {movie['imdb']}")

# 4. Calculate the average IMDB score of all movies
average_score = average_imdb(movies)
print(f"\nAverage IMDB score of all movies: {average_score:.2f}")

# 5. Calculate the average IMDB score of Romance movies
average_romance_score = average_imdb_by_category(movies, "Romance")
print(f"Average IMDB score of Romance movies: {average_romance_score:.2f}")