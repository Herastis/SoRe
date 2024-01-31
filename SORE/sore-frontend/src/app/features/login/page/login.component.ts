import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';
import { RegisterComponent } from '../../register/register.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  mouseoverLogin!: any;
  loginForm!: FormGroup;

  constructor(private authService: AuthService,
    private router: Router,
    public dialog: MatDialog) { }

  ngOnInit(): void {
    this.loginForm = new FormGroup({
      email: new FormControl("", [Validators.required, Validators.email]),
      password: new FormControl("", Validators.required),
    })
  }

  login() {
    if (this.loginForm.valid) {
      const email = this.loginForm.get('email')?.value;
      const password = this.loginForm.get('password')?.value;
      this.authService.login(email, password).subscribe(
        (resp: any) => {
          localStorage.setItem('access_token', resp.access_token);
          this.authService.setLoggedIn(true);
          this.router.navigate([this.authService.redirectUrl]); 
        },
        err => {
          console.error(err);
        }
      );
    }
  }

  openRegisterDialog(): void {
    const dialogRef = this.dialog.open(RegisterComponent, {
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The login dialog was closed');
    });
  }
}
