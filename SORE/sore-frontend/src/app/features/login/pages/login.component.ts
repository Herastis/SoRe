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

  constructor(private authService: AuthService,
    private router: Router,
    public dialog: MatDialog) { }

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

  openRegisterDialog(): void {
    const dialogRef = this.dialog.open(RegisterComponent, {
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The login dialog was closed');
    });
  }
}
