import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserProfile } from '../types/user-profile.type';

@Injectable({
  providedIn: 'root'
})
export class UserProfileService {
  url: string = 'http://127.0.0.1:5000';
  constructor(private http: HttpClient) { }

  saveProfile(profileData: UserProfile) {
    return this.http.post(`${this.url}/profile`, profileData);
  }
}
