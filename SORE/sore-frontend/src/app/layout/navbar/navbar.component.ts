import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { AuthService } from 'src/app/core/services/auth.service';
import { LoginComponent } from 'src/app/features/login/page/login.component';
import { RegisterComponent } from 'src/app/features/register/register.component';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit {
  isLoggedIn: boolean = false;
  subscription!: Subscription;
  avatarUrl!: string;
  firstName!: string | null;
  lastName!: string | null;

  constructor(public dialog: MatDialog,
    private authService: AuthService,
    private router: Router) { }

  ngOnInit(): void {
    this.subscription = this.authService.isLoggedInStatus.subscribe(
      (loggedInStatus: boolean) => {
        this.isLoggedIn = loggedInStatus;
        this.getAvatar();
      }
    );
  }

  register(): void {
    const dialogRef = this.dialog.open(RegisterComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  login(): void {
    const dialogRef = this.dialog.open(LoginComponent);

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        this.isLoggedIn = true;
        this.getAvatar();
      }
    });

  }

  logout(): void {
    this.authService.logout();
  }

  navigateToProfile() {
    this.router.navigate(['/profile']);
  }
  
  getAvatar(): void {
    this.firstName = localStorage.getItem('firstName');
        this.lastName = localStorage.getItem('lastName');
        if (this.firstName && this.lastName) {
          this.avatarUrl = this.authService.getAvatarUrl(this.firstName, this.lastName);
        }
  }
}
