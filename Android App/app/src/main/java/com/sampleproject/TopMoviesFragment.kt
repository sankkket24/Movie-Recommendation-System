package com.sampleproject

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class TopMoviesFragment : Fragment() {

    private lateinit var movieText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.top_movies_fragment,container,false)
        this.movieText=view.findViewById(R.id.top_movies_result_text)
        apiCall()
        return view
    }

    private fun apiCall() {
        println("calling API call")
        val topMovies= MovieApplication.create().topMovies()
        topMovies.enqueue(object : Callback<List<String>> {
            override fun onResponse(call: Call<List<String>>, response: Response<List<String>>){
                println("inside on response")
                if(response?.body() != null){
                    for(s in response?.body()!!){
                        movieText.append("\n$s")
                    }
                }
            }
            override fun onFailure(call: Call<List<String>>, t: Throwable) {
                println(t.message.toString())
            }
        })
    }

}