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
    values = [review.user.id, review.film.id, review.customer_rating, review.comment]
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
        review = Review(user, film, row['customer_rating'], row['customer_comment'], row['id'])
        reviews.append(review)
    return reviews

def select(id):
    sql = "SELECT * FROM reviews WHERE id = %s"
    values  = [id]
    result  = run_sql(sql, values)[0]
    user = user_repository.select(result['user_id'])
    film = film_repository.select(result['film_id'])
    review = Review(user, film, result['customer_rating'], result['customer_comment'], result['id'])
    return review

def update(review):
    sql = "UPDATE reviews SET (customer_rating, customer_comment) = (%s,%s) WHERE id = %s"
    values = [review.customer_rating, review.comment, review.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM reviews WHERE id = %s"
    values = [id]
    run_sql(sql, values)