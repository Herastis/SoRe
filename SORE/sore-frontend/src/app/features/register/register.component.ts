import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { LoginComponent } from '../login/pages/login.component';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  mouseoverLogin!: any;

  constructor(
    public dialog: MatDialog
  ) { }

  ngOnInit() {
  }

  registerForm = new FormGroup({
    firstName: new FormControl("", Validators.required), 
    lastName: new FormControl("", Validators.required),  
    email: new FormControl("", [Validators.required, Validators.email]),
    password: new FormControl("", Validators.required),
  })

  register() {

  }

  openLoginDialog(): void {
    const dialogRef = this.dialog.open(LoginComponent, {
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The register dialog was closed');
    });
  }

}
