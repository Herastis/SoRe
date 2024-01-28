import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  mouseoverLogin!: any;

  constructor(private authService: AuthService,
    private router: Router) { }

  ngOnInit(): void {
  }

  loginForm = new FormGroup({
    email: new FormControl("", [Validators.required, Validators.email]),
    password: new FormControl("", Validators.required),
  })

  login() {
    // this.authService.isLoggedin = true;
    // this.authService.email = this.loginForm.controls['email'].value;
    // this.authService.firstName = this.authService.email.split(/[@.]/)[0];
    // this.authService.lastName = this.authService.email.split(/[@.]/)[1];
    
    // if (this.loginForm.valid) {
    //   if(this.authService.redirectUrl){
    //     this.router.navigateByUrl(this.authService.redirectUrl);
    //   } else {
    //     this.router.navigate(['population']);
    //   }
    // }
  }
}
