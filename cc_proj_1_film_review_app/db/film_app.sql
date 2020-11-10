
DROP TABLE watchlist;
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
    rating_in_stars INT,
    rating_text VARCHAR(255),
    genre VARCHAR(255),
    critic_review TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    film_id INT REFERENCES films(id),
    customer_rating INT,
    customer_comment TEXT
);

CREATE TABLE watchlist (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    film_id INT REFERENCES films(id),
    in_watchlist BIT

);
