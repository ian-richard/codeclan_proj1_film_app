from db.run_sql import run_sql
from models.film import Film
from models.user import User

def select(id):
    film = None
    sql = "SELECT * FROM films WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        film = Film(result['id'], result['name'], result['rating_stars'], result['rating_text'], result['genre'], result['critic_review'])
    return film