import {Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn:'root',
})
export class MovieService{

    constructor(private http:HttpClient){

    }

    getMovieDetails(title:any){
        return this.http.post("http://localhost:5000/title",{"title":title});
    }
}