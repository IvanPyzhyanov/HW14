from flask import Flask, request, render_template, send_from_directory, jsonify, redirect
import os
from pathlib import Path
import sqlite3
from functions import search_title, search_years, search_rating, rating_exist, search_genre, genre_exist, search_actors, some_movies

app = Flask("HW_14")


@app.route("/")
def main_page():
    return render_template("index.html", rating_list=rating_exist(), genre_list=genre_exist())


@app.route("/movie/title/", methods=["GET"])
def movie_by_title():
    s = request.args.get("movie_title")
    if s:
        return render_template("index.html", data_film=search_title(s), rating_list=rating_exist(), genre_list=genre_exist())
    return redirect(f"/", code = 302)


@app.route("/movie/year/", methods=["GET"])
def movie_by_year():
    year_1 = request.args.get("years_from")
    year_2 = request.args.get("years_to")
    if year_1 and year_2:
        return render_template("index.html", data_year=search_years(year_1, year_2), rating_list=rating_exist(), genre_list=genre_exist())
    return redirect(f"/", code = 302)


@app.route("/movie/rating/", methods=["GET"])
def movie_by_rating():
    tag = request.args.get("rating_tag")
    if tag:
        return render_template("index.html", data_rating=search_rating(tag), rating_list=rating_exist(), genre_list=genre_exist())
    return redirect(f"/", code = 302)


@app.route("/movie/genre/", methods=["GET"])
def movie_by_genre():
    tag = request.args.get("genre_tag")
    if tag:
        return render_template("index.html", data_genre=search_genre(tag), rating_list=rating_exist(), genre_list=genre_exist())
    return redirect(f"/", code = 302)


@app.route("/movie/actors/", methods=["GET"])
def actors_by_actors():
    actor_1 = request.args.get("actor_1")
    actor_2 = request.args.get("actor_2")
    if actor_1 and actor_2:
        return render_template("index.html", data_actors=search_actors(actor_1, actor_2), rating_list=rating_exist(), genre_list=genre_exist())
    return redirect(f"/", code = 302)


@app.route("/movie/movies/", methods=["GET"])
def movie_by_params():
    type_tag = request.args.get("movie_type")
    year_tag = request.args.get("movie_year")
    genre_tag = request.args.get("movie_genre")
    if type_tag and year_tag and genre_tag:
        return render_template("index.html", data_movies=some_movies(type_tag, year_tag, genre_tag), rating_list=rating_exist(), genre_list=genre_exist())
    return redirect(f"/", code = 302)


if __name__ == "__main__":
    os.chdir(Path(os.path.abspath(__file__)).parent)
    app.run(debug=True)

