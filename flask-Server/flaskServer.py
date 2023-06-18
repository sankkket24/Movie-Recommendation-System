# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:56:31 2022

@author: shahanesanket24
"""

from flask import Flask, jsonify, request
from MovieRecommendation import MovieRecommendation

app = Flask(__name__)

movie = MovieRecommendation()

@app.route('/')
def start():
    return "Welcome to the Movie Recommendation System"

@app.route("/TopMovies")
def topMovies():
    data = movie.get_index_from_popularity()
    return jsonify(data)

@app.route("/title", methods=["POST"])
def findLikeMovies():
    try:
        jsonData = request.get_json()

        # Perform search based on the movie title
        data = movie.get_index_from_title(jsonData["title"])
        return jsonify(data)
    except:
        return jsonify(["Wrong Title"])

@app.route("/genres", methods=["POST"])
def findMoviesInGenres():
    try:
        jsonData = request.get_json()
        movie_genres = jsonData.get("genres")

        # Perform search based on the movie genres
        data = movie.get_index_from_genre(movie_genres)
        return jsonify(data)
    except:
        return jsonify(["Wrong Genres"])

if __name__ == '__main__':
   app.run(host='0.0.0.0')
