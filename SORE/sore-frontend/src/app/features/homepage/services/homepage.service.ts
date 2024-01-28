import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HomepageType } from '../types';

@Injectable({
  providedIn: 'root'
})
export class HomepageService {

  constructor(private httpClient: HttpClient) { }

  url: string = 'http://127.0.0.1:5000//homepage';

  getHomepage(): Observable<string> {
    return this.httpClient.get<string>(this.url);
  }
}

