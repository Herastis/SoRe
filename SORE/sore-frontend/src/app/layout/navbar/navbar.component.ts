import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { LoginComponent } from 'src/app/features/login/pages/login.component';
import { RegisterComponent } from 'src/app/features/register/register.component';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  isLoggedIn: boolean = false;
  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  login() {
    const dialogRef = this.dialog.open(LoginComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
    //this.isLoggedIn = true;
  }

  logout() {
    //this.isLoggedIn = false;
  }

}
