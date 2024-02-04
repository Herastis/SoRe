import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserProfileService {
  url: string = 'http://127.0.0.1:5000';
  constructor(private http: HttpClient) { }

  saveProfile(profileData: any) {
    return this.http.post(`${this.url}/profile`, profileData);
  }
}
