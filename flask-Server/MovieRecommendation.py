# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:37:24 2022

@author: shahanesanket24
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movie_dataset.csv")
class MovieRecommendation:
    
    def __init__(self):
        features = ['keywords', 'cast', 'genres', 'director']
        for feature in features:
            df[feature] = df[feature].fillna('')
        
        df["combined_features"] = df.apply(self.combined_features, axis =1)
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df["combined_features"])
        self.cosine_sim = cosine_similarity(count_matrix)
        
    
    def get_index_from_title(self,title):
        movie_index = df[df.title == title]["index"].values[0]
        similar_movies = list(enumerate(self.cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)
        i=0
        moviesList = []
        for movie in sorted_similar_movies:
           # print(self.get_title_from_index(movie[0]))
            moviesList.append(self.get_title_from_index(movie[0]))
            i=i+1
            if i>15:
                break
        
        return moviesList
    
    def get_index_from_popularity(self):
        top10Movies = pd.DataFrame(data=df,columns=["index","popularity"]).sort_values(by=["popularity"],ascending=False)
        movie_index = top10Movies["index"]
        i=0
        moviesList = []
        for movie in movie_index:
            #print(self.get_title_from_index(movie))
            moviesList.append(self.get_title_from_index(movie))
            i=i+1
            if i>20:
                break
        
        return moviesList
    
    def get_index_from_genre(self,genre):
        movie_index =  df[df.genres == genre]["index"].values[0]
        similar_movies = list(enumerate(self.cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)
        i=0
        moviesList = []
        for movie in sorted_similar_movies:
           # print(self.get_title_from_index(movie[0]))
            moviesList.append(self.get_title_from_index(movie[0]))
            i=i+1
            if i>15:
                break
        
        return moviesList

        
    def get_title_from_index(self,index):
        return df[df.index == index]["title"].values[0]
    
    def combined_features(self,row):
        return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
 