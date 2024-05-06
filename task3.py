import numpy as np

class CollaborativeFiltering:
    def __init__(self, ratings):
        self.ratings = ratings
        self.num_users, self.num_movies = ratings.shape
        
    def calculate_similarity(self):
        self.similarity = np.zeros((self.num_movies, self.num_movies))
        for i in range(self.num_movies):
            for j in range(self.num_movies):
                if i != j:
                    mask = np.logical_and(self.ratings[:, i] != 0, self.ratings[:, j] != 0)
                    if np.any(mask):
                        self.similarity[i, j] = np.corrcoef(self.ratings[mask, i], self.ratings[mask, j])[0, 1]
        
    def recommend_movies(self, user_id, top_n=5):
        user_ratings = self.ratings[user_id, :]
        rated_movies = np.where(user_ratings != 0)[0]
        scores = np.zeros(self.num_movies)
        for movie_id in range(self.num_movies):
            if user_ratings[movie_id] == 0:
                sim_scores = self.similarity[movie_id, rated_movies]
                rated_scores = user_ratings[rated_movies]
                scores[movie_id] = np.sum(sim_scores * rated_scores) / np.sum(np.abs(sim_scores))
        recommended_movies = np.argsort(scores)[::-1][:top_n]
        return recommended_movies

# Example usage
ratings = np.array([[5, 0, 4, 0, 0],
                    [0, 4, 0, 5, 0],
                    [4, 0, 5, 0, 4],
                    [0, 5, 0, 4, 5],
                    [0, 0, 4, 0, 5]])

cf = CollaborativeFiltering(ratings)
cf.calculate_similarity()

user_id = 0
recommended_movies = cf.recommend_movies(user_id)
print("Recommended movies for user", user_id)
for movie_id in recommended_movies:
    print("Movie", movie_id)
