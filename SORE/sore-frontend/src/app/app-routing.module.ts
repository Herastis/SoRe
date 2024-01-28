import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from 'src/features/dashboard';
import { HomepageComponent } from 'src/features/homepage/page/homepage.component';
import { LoginComponent } from 'src/features/login/pages/login.component';

const routes: Routes = [
  { path: '', redirectTo: '/homepage', pathMatch: 'full' }, // Default route
  { path: 'login', component: LoginComponent },
  { path: 'homepage', component: HomepageComponent }, // Default route
  { path: 'dashboard', component: DashboardComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
