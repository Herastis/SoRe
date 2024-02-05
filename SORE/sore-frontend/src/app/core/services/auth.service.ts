import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable, map } from 'rxjs';
import { LoginResponseType } from '../types/loginResponse.type';
import { RegisterFormType } from '../types/registerForm.type';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url: string = 'http://127.0.0.1:5000';
  redirectUrl = 'profile'
  public isLoggedInStatus = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient, private router: Router) {
    this.isLoggedInStatus.next(this.checkIsLoggedInStatus());
  }

  register(form: RegisterFormType) {
    return this.http.post(`${this.url}/register`, form);
  }

  login(email: string, password: string): Observable<boolean> {
    return this.http.post<LoginResponseType>(`${this.url}/login`, { email, password })
      .pipe(map(response => {
        if (response.access_token) {
          localStorage.setItem('access_token', response.access_token);
          localStorage.setItem('firstName', response.firstName);
          localStorage.setItem('lastName', response.lastName);
          localStorage.setItem('email', response.email);
          this.isLoggedInStatus.next(true);
          return true;
        } else {
          return false;
        }
      }
      ));
  }

  logout() {
    this.isLoggedInStatus.next(false);
    localStorage.removeItem('access_token');
    localStorage.removeItem('firstName');
    localStorage.removeItem('lastName');
    localStorage.removeItem('email');
    this.router.navigate(['/homepage']);
  }

  setIsLoggedInStatus(value: boolean) {
    this.isLoggedInStatus.next(value);
  }

  isLoggedIn(): boolean {
    return this.isLoggedInStatus.value;
  }

  private checkIsLoggedInStatus(): boolean {
    return !!localStorage.getItem('access_token');
  }

  getAvatarUrl(firstName: string, lastName: string): string {
    return `https://ui-avatars.com/api/?name=${encodeURIComponent(firstName)}+${encodeURIComponent(lastName)}&rounded=true`;
  }
}
