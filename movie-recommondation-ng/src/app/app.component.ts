import { Component } from '@angular/core';
import { MovieService } from './services/movieService';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'movie-recommondation-ng';
  searchTxt: any;
  movies:any

  constructor(private movieService: MovieService) {

  }

  sampleFns() {
    this.movieService.getMovieDetails(this.searchTxt).subscribe((data) => {
      this.movies = data;
    });

    //console.log(this.searchTxt)
  }
}
