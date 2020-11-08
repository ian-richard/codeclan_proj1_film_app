from db.run_sql import run_sql
from models.review import Review
import repositories.user_repository as user_repository
import repositories.film_repository as film_repository

def select_all():
    reviews = []

    sql = "SELECT * FROM reviews"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        film = film_repository.select(row['film_id'])
        # customer_rating = review_repository.select(row['customer_rating'])
        review = Review(row['id'], user, film, row['review'], row['customer_rating'], row['comment'] )
        review.append(review)
    return reviews

    #next select 