import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TopicComponent } from './features/topic/page/topic.component';
import { LoginComponent } from './features/login/pages/login.component';

const routes: Routes = [
  { path: ':type', component: TopicComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
