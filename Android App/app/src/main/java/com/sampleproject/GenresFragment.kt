package com.sampleproject

import android.graphics.Movie
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class GenresFragment : Fragment() {

    private lateinit var genreInput:EditText
    private lateinit var genreSearchbtn: Button
    private lateinit var genreResultText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view= inflater.inflate(R.layout.genres_fragment,container,false)
        this.genreInput= view.findViewById(R.id.genre_movie_title)
        this.genreSearchbtn = view.findViewById(R.id.genres_search_btn)
        this.genreResultText = view.findViewById(R.id.genres_result_txt)

        this.genreSearchbtn.setOnClickListener {
            this.genreResultText.text =""
            this.apiCall(this.genreInput.text.toString())
        }

        return view
    }

    private fun apiCall(genres:String){
        var movieApp = MovieApplication.create().findMoviesInGenres(genres)
        movieApp.enqueue(object: Callback<List<String>>{
            override fun onResponse(call: Call<List<String>>, response: Response<List<String>>) {
                println("Inside on Response Method")
                if(response?.body() != null){
                    for(s in response?.body()!!){
                        genreResultText.append("\n$s")
                    }
                }
            }

            override fun onFailure(call: Call<List<String>>, t: Throwable) {
                println("inside on failure method")
                throw t
            }

        })
    }
}