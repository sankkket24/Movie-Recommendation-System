package com.sampleproject

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button

class MainActivity : AppCompatActivity() {

   private lateinit var movieBtn: Button
   private lateinit var titleBtn:Button
   private lateinit var genresBtn: Button

    private fun connectView(){
        this.movieBtn = this.findViewById(R.id.movies_btn)
        this.titleBtn = this.findViewById(R.id.movie_title_btn)
        this.genresBtn = this.findViewById(R.id.genres_movie_btn)
    }

    private fun callBackFns(){
        this.movieBtn.setOnClickListener {

            this.supportFragmentManager.beginTransaction()
                .replace(R.id.vertical_layout_main,TopMoviesFragment())
                .commit()
        }

        this.titleBtn.setOnClickListener {

            this.supportFragmentManager.beginTransaction()
                .replace(R.id.vertical_layout_main,TitleFragment())
                .commit()
        }

        this.genresBtn.setOnClickListener {

            this.supportFragmentManager.beginTransaction()
                .replace(R.id.vertical_layout_main,GenresFragment()).commit()
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        connectView()
        callBackFns()
    }



}