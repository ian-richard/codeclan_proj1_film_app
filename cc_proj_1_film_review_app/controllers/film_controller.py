from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.film import Film
from models.watchlist import Watchlist
import repositories.film_repository as film_repository
import repositories.user_repository as user_repository
import repositories.watchlist_repository as watchlist_repository

films_blueprint = Blueprint("films", __name__)

@films_blueprint.route("/films")
def films():
    films = film_repository.select_all()
    return render_template("films/index.html", films = films) 

@films_blueprint.route("/films/<id>")
def show(id):
    film = film_repository.select(id)
    users = user_repository.select_all()
    return render_template("films/show.html", film=film, users = users)
        

@films_blueprint.route("/films/<id>/add_to_watchlist", methods=["POST"])
def add_to_watchlist(id):
    user = user_repository.select(request.form['user_id'])
    film = film_repository.select(request.form['film_id'])
    film_to_list = Watchlist(user, film)
    watchlist_repository.save(film_to_list)
    return redirect('/watchlist')