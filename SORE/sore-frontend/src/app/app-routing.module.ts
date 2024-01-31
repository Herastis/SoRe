import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TopicComponent } from './features/topic/page/topic.component';
import { UserProfileComponent } from './features/user-profile/page/user-profile.component';

const routes: Routes = [
  { path: 'profile', component: UserProfileComponent },
  { path: ':type', component: TopicComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
