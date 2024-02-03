import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TopicType } from '../types';
@Injectable({
  providedIn: 'root'
})
export class TopicService {

  constructor(private httpClient: HttpClient) { }

  url: string = 'http://127.0.0.1:5000';

  loadTopicData(topic: string): Observable<TopicType[]> {
    return this.httpClient.get<TopicType[]>(`${this.url}/${topic}`);
  }
}

