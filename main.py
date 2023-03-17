# TODO: Add a .gitignore file.
# TODO: Add .env file

from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)


# ALL ROUTES
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)