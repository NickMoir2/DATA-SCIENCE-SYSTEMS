from pymongo import MongoClient

client = MongoClient("mongodb+srv://bfkiwikid:Ptas0ZeFtipKJm9J@ds2002.gdqny.mongodb.net/?retryWrites=true&w=majority&appName=DS2002")
db = client["sample_mflix"]
collection = db["movies"]

action_movie = collection.find_one({"genres": "Action"},{"title": 1, "_id": 0})
movies_after_2000 = collection.find({"year": {"$gt": 2000}}, {"title": 1, "_id": 0}).limit(5)
high_rated_movies = collection.find({"imdb.rating": {"$gt": 8.5}},{"title": 1, "_id": 0}).limit(5)
action_adventure_movies = collection.find({"genres": {"$all": ["Action", "Adventure"]}}, {"title": 1, "_id": 0}).limit(5)

print("First action movie: ", action_movie)
print("5 movies released after 2000: ")
for movies in movies_after_2000:
    print(movies)
print("5 movies rated 8.5 or higher: ")
for movies in high_rated_movies:
    print(movies)
print("5 action adventure movies: ")
for movies in action_adventure_movies:
    print(movies)

sorted_comedy_movies = collection.find({"genres": "Comedy"}, {"title": 1, "_id": 0}).sort("imdb.rating", -1).limit(5)
sorted_drama_movies = collection.find({"genres": "Drama"}, {"title": 1, "_id": 0}).sort("year", 1).limit(5)

print("Top 5 rated comedy movies: ")
for movies in sorted_comedy_movies:
    print(movies)
print("Top 5 oldest drama movies: ")
for movies in sorted_drama_movies:
    print(movies)

avg_rating_by_genre = collection.aggregate([{"$unwind": "$genres"}, {"$group": {"_id": "$genres", "avg_rating": {"$avg": "$imdb.rating"}}}, {"$sort": {"avg_rating": -1}}, {"$limit": 5}])
top_directors = collection.aggregate([{"$group": {"_id": "$directors", "avg_rating": {"$avg": "$imdb.rating"}}}, {"$sort": {"avg_rating": -1}}, {"$limit": 5}])
movies_per_year = collection.aggregate([{"$group": {"_id": "$year", "total_movies": {"$sum": 1}}},{"$sort": {"_id": 1}}])

print("Top 5 genres by average rating: ")
for genres in avg_rating_by_genre:
    print(genres)
print("Top 5 directors by average rating: ")
for directors in top_directors:
    print(directors)
print("How many movies released each year: ")
for movies in movies_per_year:
    print(movies)

collection.update_one({"title": "The Godfather"}, {"$set": {"imdb.rating": 9.5}})
collection.update_many({"genres": "Horror", "imdb.rating": {"$exists": False}}, {"$set": {"imdb.rating": 6.0}})
collection.delete_many({"year": {"$lt": 1950}})

love_movies = collection.find({"title": {"$regex": " love ", "$options": "i"}}, {"title": 1, "_id": 0}).limit(5)
war_movies = collection.find({"$text": {"$search": "war"}},{"title": 1, "_id": 0}).sort("imdb.rating", -1).limit(5)

print("5 movies with 'love' in the title: ")
for movies in love_movies:
    print(movies)
print("Top 5 Movies with 'war' in the title or plot: ")
for movies in war_movies:
    print(movies)

action_high_rated_movies = collection.find({"genres": "Action", "imdb.rating": {"$gt": 8}}, {"title": 1, "_id": 0}).sort("year", -1)
nolan_movies = collection.find({"directors": "Christopher Nolan", "imdb.rating": {"$gt": 8}}, {"title": 1, "_id": 0}).sort("imdb.rating", -1).limit(3)

print("Top action movies with an IMDB score of 8 or higher: ")
for movies in action_high_rated_movies:
    print(movies)
print("Top 3 Christopher Nolana movies with an IMDB score of 8 or higher: ")
for movies in nolan_movies:
    print(movies)