import pdb
from models.film import Film
from models.user import User
from models.review import Review
from models.watchlist import Watchlist

import repositories.film_repository as film_repository
import repositories.user_repository as user_repository
import repositories.review_repository as review_repository
import repositories.watchlist_repository as watchlist_repository


review_repository.delete_all()
film_repository.delete_all()
user_repository.delete_all()
review_repository.delete_all()
watchlist_repository.delete_all()

user1 = User("Harry")
user_repository.save(user1)

user2 = User("Claire")
user_repository.save(user2)


film1 = Film("James Bond", 4, "****", "Action", "Boozy egomanic goes on violent and womenising binge")
film_repository.save(film1)

film2 = Film("Harry Potter", 4, "****", "Kids", "This HP review...")
film_repository.save(film2)

film3 = Film("La Haine", 5, "*****", "Action", "This 1995 classic film...")
film_repository.save(film3)

film4 = Film("Tom & Jerry", 5, "*****", "Cartoon", "It's a game of cat and mouse")
film_repository.save(film4)

film5 = Film("Lucky Grandma", 5, "****", "Comedy", "chain-smoking Chinese grandma goes all in at the casino, landing herself on the wrong side of luck - and in the middle of a gang war.")
film_repository.save(film5)

film6 = Film("Mank", 5, "*****", "Drama", "Follows screenwriter Herman J. Mankiewicz's tumultuous development of Orson Welles' iconic masterpiece Citizen Kane (1941).")
film_repository.save(film6)

film7 = Film("No Time To Die", 4, "***", "Action", "James Bond has left active service.")
film_repository.save(film7)


review1 =  Review(user1, film1, 2, "Entertaining, however not very woke.")
review_repository.save(review1)

review2 =  Review(user1, film2, 2, "It's a kid's film")
review_repository.save(review2)

review3 =  Review(user1, film3, 5, "Gripping story of young men in the suburbs of Paris")
review_repository.save(review3)

watchlist1 = Watchlist(user2, film3)
watchlist_repository.save(watchlist1)

watchlist2 = Watchlist(user1, film1)
watchlist_repository.save(watchlist2)

# pdb.set_trace()