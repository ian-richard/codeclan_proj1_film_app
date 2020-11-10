from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.review import Review
import repositories.review_repository as review_repository
import repositories.user_repository as user_repository
import repositories.film_repository as film_repository
import repositories.watchlist_repository as watchlist_repository

watchlist_blueprint = Blueprint("watchlist", __name__)

@watchlist_blueprint.route("/watchlist")
def watchlist():
    watchlist_list = watchlist_repository.select_all() 
    return render_template("watchlist/index.html", watchlist_list = watchlist_list) 

@watchlist_blueprint.route('/watchlist/<id>/delete', methods=['POST'])
def delete_watchlist(id):
    watchlist_repository.delete(id)
    return redirect("/watchlist")