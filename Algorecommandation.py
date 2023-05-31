from collections import defaultdict
from math import sqrt

ratings = defaultdict(dict)
genres = {}

def add_rating(user, movie, rating, genre):
    ratings[user][movie] = rating
    genres[movie] = genre

def compute_similarity(user1, user2):
    common_movies = set(ratings[user1].keys()) & set(ratings[user2].keys())

    if not common_movies:
        return 0.0  # Pas de films en commun, similarité de 0

    ratings1 = [ratings[user1][movie] for movie in common_movies]
    ratings2 = [ratings[user2][movie] for movie in common_movies]

    sum1 = sum(ratings1)
    sum2 = sum(ratings2)
    sum1_sq = sum(rating ** 2 for rating in ratings1)
    sum2_sq = sum(rating ** 2 for rating in ratings2)
    p_sum = sum(ratings1[i] * ratings2[i] for i in range(len(common_movies)))

    n = len(common_movies)
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sq - (sum1 ** 2) / n) * (sum2_sq - (sum2 ** 2) / n))

    if den == 0:
        return 0.0  # Division par zéro, similarité de 0

    return num / den

def recommend_movies(user, num_recommendations):
    recommendations = []
    user_ratings = ratings[user]

    for movie in user_ratings:
        if user_ratings[movie] == 0:
            weighted_sum = 0.0
            similarity_sum = 0.0

            for other_user in ratings:
                if other_user != user and movie in ratings[other_user]:
                    similarity = compute_similarity(user, other_user)
                    weighted_sum += similarity * ratings[other_user][movie]
                    similarity_sum += similarity

            if similarity_sum > 0:
                recommendations.append((movie, weighted_sum / similarity_sum))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    recommended_movies = [movie for movie, _ in recommendations[:num_recommendations]]

    return recommended_movies

def recommend_movies_by_genre(user, num_recommendations, genre):
    all_recommendations = recommend_movies(user, num_recommendations)
    genre_recommendations = [movie for movie in all_recommendations if genres.get(movie) == genre]

    return genre_recommendations


from matplotlib.animation import MovieWriter
def get_movies():
    movies_repository = app_data_source.get_repository(MovieWriter)
    movies = movies_repository.find(select={'title': True, 'date': True, 'id': True})
    return jsonify({'movies': movies})