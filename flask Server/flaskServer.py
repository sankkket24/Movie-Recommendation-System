# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 19:56:31 2022

@author: shahanesanket24
"""

from flask import Flask, jsonify, request
from MovieRecommendation import MovieRecommendation
import http.client
import json

app = Flask(__name__)

movie = MovieRecommendation()


conn = http.client.HTTPSConnection("moviesdatabase.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "3e1f1dda8cmshe957d0711f80c46p1e0589jsncc633598dc16",
    'X-RapidAPI-Host': "moviesdatabase.p.rapidapi.com"
}


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
        detailsData=[]
        jsonData=request.get_json()
        data = movie.get_index_from_title(jsonData["title"])
        for d in data:
           details = getMovieDetailsFromAPI(d)
           tp= json.loads(details)
           detailsData.append(tp)
        return detailsData
    except:
        return jsonify(["Wrong Title"])
        


@app.route("/genres", methods=["POST"])
def findMoviesInGenres():
    try:
        detailsData=[]
        jsonData=request.get_json()
        data = movie.get_index_from_genre(jsonData["genre"])
        for d in data:
           details = getMovieDetailsFromAPI(d)
           tp= json.loads(details)
           detailsData.append(tp)
        return detailsData
    except:
        return jsonify(["Wrong Genres"])
    
def getMovieDetailsFromAPI(title):
    title=title.replace(" ","%20")
    conn.request("GET", f"/titles/search/title/{title}?exact=true&titleType=movie", headers=headers)
    res = conn.getresponse()
    data = res.read()
    conn.close()
    return data.decode()
    

if __name__ == '__main__':
   app.run(host='0.0.0.0') 