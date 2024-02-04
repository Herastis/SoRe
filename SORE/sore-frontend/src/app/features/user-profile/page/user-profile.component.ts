import { Component, ElementRef, OnInit, ViewChild, inject } from '@angular/core';
import { FormGroup, FormControl, FormArray, FormBuilder } from '@angular/forms';
import { UserProfileService } from '../services/user-profile.service';

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
  preferencesForm!: FormGroup;

  travel = ['Adventure', 'Luxury', 'Backpacking', 'Cultural', 'Nature'];
  food = ['Cooking', 'Baking', 'Healthy', 'Reviews', 'Experiments'];
  fitness =  ['Gym', 'Yoga', 'Running', 'CrossFit', 'Bodybuilding'];
  fashion =  ['Streetwear', 'Vintage', 'HighFashion', 'Sustainable', 'DIY'];
  technology = ['Gadgets', 'Programming', 'AI', 'Cybersecurity', 'Development'];
  entertainment = ['Movies', 'TVShows', 'Celebrities', 'Concerts', 'Gaming'];
  books = ['Fiction', 'NonFiction', 'Fantasy', 'Mystery', 'ScienceFiction'];
  gaming = ['VideoGames', 'BoardGames', 'Esports', 'GameReviews', 'GameDevelopment'];
  photography = ['Landscape', 'Portrait', 'Mobile', 'Street', 'Wildlife'];
  parenting = ['NewbornCare', 'ParentingTips', 'Educational', 'FamilyTravel', 'ParentingHumor'];
  crafts = ['DIYCrafts', 'Knitting', 'Painting', 'Pottery', 'Scrapbooking'];
  politics = ['PoliticalNews', 'Activism', 'PolicyAnalysis', 'GlobalAffairs', 'LocalPolitics'];
  music = ['Genres', 'Concerts', 'MusicReviews', 'MusicProduction', 'VinylCollecting'];
  pets = ['Dogs', 'Cats', 'ExoticPets', 'PetCareTips', 'PetAdoption'];
  selfImprovement = ['Productivity', 'Mindfulness', 'MotivationalQuotes', 'GoalSetting', 'PersonalDevelopment'];
  art = ['FineArts', 'StreetArt', 'DigitalArt', 'Sculpture', 'ArtExhibitions'];
  movies = ['Genres', 'MovieReviews', 'FilmFestivals', 'ClassicFilms', 'IndieMovies'];
  sports = ['Football', 'Basketball', 'Tennis', 'Running', 'ExtremeSports'];
  health = ['MentalHealth', 'Nutrition', 'HolisticWellness', 'FitnessChallenges', 'HealthyRecipes'];
  education = ['OnlineLearning', 'EducationalTechnology', 'LearningResources', 'AcademicTips', 'CareerDevelopment'];



  constructor(private fb: FormBuilder, private service: UserProfileService) {
    this.profileForm = this.createprofileForm();
    this.preferencesForm = this.fb.group({
      travel: this.buildPreferencesArray(),
      food: this.buildPreferencesArray(),
      fitness: this.buildPreferencesArray(),
      fashion: this.buildPreferencesArray(),
      technology: this.buildPreferencesArray(),
      entertainment: this.buildPreferencesArray(),
      books: this.buildPreferencesArray(),
      gaming: this.buildPreferencesArray(),
      photography: this.buildPreferencesArray(),
      parenting: this.buildPreferencesArray(),
      crafts: this.buildPreferencesArray(),
      politics: this.buildPreferencesArray(),
      music: this.buildPreferencesArray(),
      pets: this.buildPreferencesArray(),
      selfImprovement: this.buildPreferencesArray(),
      art: this.buildPreferencesArray(),
      movies: this.buildPreferencesArray(),
      sports: this.buildPreferencesArray(),
      health: this.buildPreferencesArray(),
      education: this.buildPreferencesArray()
      // Continuați cu restul categoriilor
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

  private buildPreferencesArray(): FormControl {
    return this.fb.control([]);
  }

  onSubmit() {
    if (this.preferencesForm.valid) {
      this.service.saveProfile(this.preferencesForm.value).subscribe({
        next: (response) => {
          console.log('Profil salvat cu succes', response);
          // Aici poți adăuga logica pentru succes, de exemplu redirecționarea
        },
        error: (error) => {
          console.error('A apărut o eroare la salvarea profilului', error);
        }
      });
    }
  }
}
