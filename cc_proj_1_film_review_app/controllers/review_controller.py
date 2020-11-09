from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.review import Review
import repositories.review_repository as review_repository
import repositories.user_repository as user_repository
import repositories.film_repository as film_repository

reviews_blueprint = Blueprint("reviews", __name__)

@reviews_blueprint.route("/reviews")
def reviews():
    reviews = review_repository.select_all() 
    return render_template("reviews/index.html", reviews = reviews) 

@reviews_blueprint.route("/reviews/new", methods=['GET'])
def new_review():
    users = user_repository.select_all()
    films = film_repository.select_all()
    return render_template("reviews/new.html", users = users, films = films)

@reviews_blueprint.route("/reviews", methods=['POST'])
def create_review():
    
