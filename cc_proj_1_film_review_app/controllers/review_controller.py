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
    user = user_repository.select(request.form['user_id'])
    film = film_repository.select(request.form['film_id'])
    customer_rating = request.form['customer_rating']
    comment = request.form['comment']
    review = Review(user, film, customer_rating, comment)
    review_repository.save(review)
    return redirect('/reviews')

@reviews_blueprint.route("/reviews/<id>/edit")
def edit_review(id):
    review_to_edit = review_repository.select(id)
    return render_template('reviews/edit.html', review_to_edit = review_to_edit)

@reviews_blueprint.route("/reviews/<id>", methods=['POST'])
def update_review(id):
    comment = request.form['comment']
    customer_rating =  request.form['customer_rating']
    review = review_repository.select(id)
    review.comment = comment
    review.customer_rating = customer_rating
    review_repository.update(review)
    print(review.id, review.comment, review.customer_rating, review.user, review.film)
    return redirect('/reviews')

