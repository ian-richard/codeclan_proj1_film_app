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

user1 = User("Harry")
user_repository.save(user1)

film1 = Film("James Bond", 4, "****", "Action", "In this review...")
film_repository.save(film1)

film2 = Film("Harry Potter", 4, "****", "Kids", "This HP review...")
film_repository.save(film2)

film3 = Film("La Haine", 5, "*****", "Action", "This 1995 classic film...")
film_repository.save(film3)

review1 =  Review(user1, film1, 2, "Outdated if you as me...")
review_repository.save(review1)

review1 =  Review(user1, film2, 2, "It's a kid's film")
review_repository.save(review2)

review1 =  Review(user1, film3, 5, "Gripping story of young men in the suburbs of Paris")
review_repository.save(review3)

# pdb.set_trace()