from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.review import Review
import repositories.review_repository as review_repository
import repositories.user_repository as user_repository
import repositories.film_repository as film_repository

reviews_blueprint = Blueprint("reviews", __name__)