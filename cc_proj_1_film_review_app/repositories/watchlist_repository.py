from db.run_sql import run_sql
from models.review import Review
from models.user import User
from models.watchlist import Watchlist
from models.film import Film
import repositories.user_repository as user_repository
import repositories.film_repository as film_repository
import repositories.watchlist_repository as watchlist_repository
import repositories.review_repository as review_repository

def delete_all():
    sql = "DELETE FROM watchlist"
    run_sql(sql)

def save(watchlist):
    sql = "INSERT INTO watchlist ( user_id, film_id) VALUES ( %s, %s) RETURNING id"
    values = [watchlist.user.id, watchlist.film.id]
    results = run_sql(sql, values)
    watchlist.id = results[0]['id']
    return watchlist



def select_all():
    watchlist_list = []

    sql = "SELECT * FROM watchlist"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        film = film_repository.select(row['film_id'])
        watchlist = Watchlist(user, film, row['id'])
        watchlist_list.append(watchlist)
    return watchlist_list

def delete(id):
    sql = "DELETE FROM watchlist WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def select(id):
    sql = "SELECT * FROM films WHERE id = %s"
    values  = [id]
    result  = run_sql(sql, values)[0]
    user = user_repository.select(result['user_id'])
    film = film_repository.select(result['film_id'])
    watchlist_item = Watchlist(user, film, result['id'])
    return watchlist_item

