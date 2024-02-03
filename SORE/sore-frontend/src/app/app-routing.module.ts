import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TopicComponent } from './features/topic/page/topic.component';
import { UserProfileComponent } from './features/user-profile/page/user-profile.component';
import { AuthGuard } from './shared/guards/auth-guard';

const routes: Routes = [
  {
    path: 'homepage',
    component: TopicComponent
  },
  {
    path: 'profile',
    canActivate: [AuthGuard],
    component: UserProfileComponent
  },
  {
    path: ':type',
    canActivate: [AuthGuard],
    component: TopicComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
