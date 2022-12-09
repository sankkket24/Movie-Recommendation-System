package com.sampleproject

import com.google.gson.GsonBuilder
import retrofit2.Call
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface MovieApplication {

    @GET("TopMovies")
    fun topMovies() :Call<List<String>>

    @POST("title")
    fun findLikeMovies(@Body title:String):Call<List<String>>

    @POST("genres")
    fun findMoviesInGenres(@Body genres:String): Call<List<String>>

    companion object{
        private var BASE_URL = "http://10.0.2.2:5000/"

        fun create() : MovieApplication{
            val gson = GsonBuilder().setLenient().create()
            val retrofit = Retrofit.Builder()
                .addConverterFactory(GsonConverterFactory.create(gson))
                .baseUrl("$BASE_URL")
                .build()
            return retrofit.create(MovieApplication::class.java)

        }
    }
}