import os
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from MovieForms import AddMovie, EditMovie

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app=app)

class Movies(db.Model):
    """Create a table on your database that stores all the data from a movie."""
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String, unique=True, nullable=False)
    director = db.Column(db.String, unique=False)
    opinion = db.Column(db.String, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)



@app.route("/")
def index():
    all_movies = db.session.query(Movies).all()
    return render_template("index.html", movies=all_movies)


@app.route("/add-movie", methods=["GET", "POST"])
def add():
    forms = AddMovie()
    if forms.validate_on_submit():
        movie_title = forms.title.data
        director = forms.director.data
        opinion = forms.opinion.data
        rate = forms.rate.data
        description = forms.description.data
        image = forms.image.data
        new_movie = Movies(movie_title=movie_title,
                           director=director,
                           opinion=opinion,
                           rate=rate,
                           description=description,
                           image=image)
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", forms=forms)


@app.route("/edit", methods=["POST", "GET"])
def edit_movie():
    movie_id = request.args["id_movie"]
    forms = EditMovie()
    movie = Movies.query.filter_by(id=movie_id).first()
    if forms.validate_on_submit():
        rate = forms.rate.data
        opinion = forms.opinion.data
        description = forms.description.data
        if len(rate) == 0:
            pass
        else:
            movie.rate = rate
        if len(opinion) == 0:
            pass
        else:
            movie.opinion = opinion
        if len(description) == 0:
            pass
        else:
            movie.description = description
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", forms=forms, movie_title=movie.movie_title)

@app.route("/delete")
def delete_movie():
    movie_id = request.args["id_movie"]
    movie = Movies.query.filter_by(id=movie_id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
