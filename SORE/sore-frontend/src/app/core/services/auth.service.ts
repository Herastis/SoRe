import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url: string = 'http://127.0.0.1:5000';
  private loggedIn = new BehaviorSubject<boolean>(false); 
  redirectUrl = 'profile'

  constructor(private http: HttpClient) { }

  register(email: string, password: string) {
    return this.http.post(`${this.url}/register`, { email, password });
  }

  login(email: string, password: string) {
    return this.http.post(`${this.url}/login`, { email, password });
  }

  isLoggedIn() {
    return this.loggedIn.asObservable();
  }

  setLoggedIn(value: boolean) {
    this.loggedIn.next(value);
  }
}
