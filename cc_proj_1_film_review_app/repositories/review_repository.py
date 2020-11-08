from db.run_sql import run_sql
from models.review import Review
from models.user import User
import repositories.user_repository as user_repository
import repositories.film_repository as film_repository

def delete_all():
    sql = "DELETE FROM reviews"
    run_sql(sql)

def save(review):
    sql = "INSERT INTO reviews ( user_id, film_id, customer_rating, customer_comment) VALUES ( %s, %s, %s, %s ) RETURNING id"
    values = [review.user_id.id, review.film_id.id, review.customer_rating, review.comment]
    results = run_sql( sql, values )
    review.id = results[0]['id']
    return review



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