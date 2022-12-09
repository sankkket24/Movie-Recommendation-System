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
    return "WelCome to Movie Recommedation System"

@app.route("/TopMovies")
def topMovies():
    data = movie.get_index_from_popularity()
    #print(data)
    return jsonify(data)

@app.route("/title",methods=["POST"])
def findLikeMovies():
    try:
        jsonData=request.get_json()
        print(jsonData)
        data = movie.get_index_from_title(jsonData)
        return jsonify(data)
    except:
        return jsonify(["Wrong Title"])
        


@app.route("/genres", methods=["POST"])
def findMoviesInGenres():
    try:
        jsonData=request.get_json()
        data = movie.get_index_from_genre(jsonData)
        return jsonify(data)
    except:
        return jsonify(["Wrong Genres"])
    

if __name__ == '__main__':
   app.run(host='0.0.0.0') 