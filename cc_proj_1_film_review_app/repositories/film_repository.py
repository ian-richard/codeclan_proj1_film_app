from db.run_sql import run_sql
from models.film import Film
from models.user import User

def delete_all():
    sql = "DELETE FROM films"
    run_sql(sql)

def save(film):
    sql = "INSERT INTO films(film_name, rating_in_stars, rating_text, genre, critic_review) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [film.name, film.rating_in_stars, film.rating_text, film.genre, film.critic_review]
    results = run_sql( sql, values )
    film.id = results[0]['id']
    return film

def select(id):
    film = None
    sql = "SELECT * FROM films WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        film = Film(result['film_name'], result['rating_in_stars'], result['rating_text'], result['genre'], result['critic_review'], result['id'])
    return film

def select_all():
    films = []

    sql = "SELECT * FROM films"
    results = run_sql(sql)

    for row in results:
        film = Film(row['film_name'], row['rating_in_stars'], row['rating_text'], row['genre'], row['critic_review'], row['id'])
        films.append(film)
    return films