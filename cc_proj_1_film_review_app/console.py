import pdb
from models.film import Film
from models.user import User
from models.review import Review

import repositories.film_repository as film_repository
import repositories.user_repository as user_repository
import repositories.review_repository as review_repository

review_repository.delete_all()
film_repository.delete_all()
user_repository.delete_all()

# pdb.set_trace()