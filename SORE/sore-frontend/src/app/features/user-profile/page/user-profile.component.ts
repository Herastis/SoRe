import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

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

  constructor() {
    this.profileForm = this.createprofileForm();
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

  toggleEdit() {
    if (this.profileForm.enabled) {
      this.profileForm.disable();
    } else {
      this.profileForm.enable();
    }
  }

  loadProfile(): void {
    this.firstName = localStorage?.getItem('firstName');
    this.lastName = localStorage?.getItem('lastName');
  }
}
