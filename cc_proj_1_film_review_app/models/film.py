class Film:
    def __init__(self, name, rating_in_stars, rating_text, genre, critic_review, id = None):
        self.name = name
        self.rating_in_stars =  rating_in_stars
        self.rating_text = rating_text
        self.genre = genre
        self.critic_review = critic_review
        self.id = id