DROP TABLE reviews;
DROP TABLE films;
DROP TABLE users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);


CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    film_name VARCHAR(255),
    rating_in_stars VARCHAR(255),
    genre VARCHAR(255),
    critic_review TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    film_id INT REFERENCES films(id),
    customer_rating VARCHAR(255),
    customer_comment TEXT
);

