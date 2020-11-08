from flask import Flask, render_template

from controllers.review_controller import reviews_blueprint
from controllers.film_controller import films_blueprint
from controllers.user_controller import users_blueprint

app = Flask(__name__)

app.register_blueprint(reviews_blueprint)
app.register_blueprint(films_blueprint)
app.register_blueprint(users_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)