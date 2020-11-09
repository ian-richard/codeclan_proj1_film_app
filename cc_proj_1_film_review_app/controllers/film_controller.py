from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.film import Film
import repositories.film_repository as film_repository

films_blueprint = Blueprint("films", __name__)

@films_blueprint.route("/films")
def films():
    
    return render_template("films/index.html") 