import { Component, ElementRef, OnInit, ViewChild, inject } from '@angular/core';
import { FormGroup, FormControl, FormArray, FormBuilder } from '@angular/forms';
import { UserProfileService } from '../services/user-profile.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit {
  firstName!: string | null;
  lastName!: string | null;
  profileForm!: FormGroup;
  nameForm!: FormGroup;
  topics = ['news', 'events', 'music', 'movies', 'healthAndWellness', 'technologyAndGadgets', 'lifestyleAndTravel', 'humorAndMemes', 'educationAndLearning'];
  preferencesForm: FormGroup;

  allCategoryJokes = ['Programming', 'Misc', 'Pun', 'Spooky', 'Christmas']
  allHealthInterests = ['treatment', 'health', 'covid']
  allNewsInterests = ["Art", "Technology", "Travel", "Coding", "Gaming"]

  constructor(private fb: FormBuilder, private service: UserProfileService,  private snackBar: MatSnackBar) {
    this.profileForm = this.createprofileForm();
    this.preferencesForm = new FormGroup({
      categoryJokes: new FormControl(['Programming']),
      healthInterests: new FormControl(['treatment']),
      newsInterests: new FormControl(['Art'])
    });
  }

  ngOnInit(): void {
    this.loadProfile();
  }

  createprofileForm() {
    const group: any = {};

    this.topics.forEach((topic) => {
      group[topic] = new FormControl({ value: '', disabled: true });
    });

    return new FormGroup(group);
  }

  loadProfile(): void {
    this.firstName = localStorage?.getItem('firstName');
    this.lastName = localStorage?.getItem('lastName');
  }

  onSubmit() {
    if (this.preferencesForm.valid) {
      this.service.saveProfile(this.preferencesForm.value).subscribe({
         next: () => {
          this.snackBar.open('Profile saved succesfully!', 'OK', {
            duration: 5000,
            horizontalPosition: 'center', 
            verticalPosition: 'top',
          });
        },
        error: () => {
          this.snackBar.open('An error has occured!', 'OK', {
            duration: 5000,
            horizontalPosition: 'center', 
            verticalPosition: 'top',
          });
        }
      });
    }
  }

  updateFruits(fruits: string[], formControl: string) {
    this.preferencesForm.get(formControl)?.setValue(fruits);
  }
}
