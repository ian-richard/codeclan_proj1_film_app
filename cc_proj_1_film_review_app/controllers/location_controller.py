from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.film import Film
import repositories.film_repository as film_repository

films_blueprint = Blueprint("films", __name__)