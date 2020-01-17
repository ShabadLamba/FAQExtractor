import { NgModule } from '@angular/core';
import { CommonModule, } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule } from '@angular/router';

import { SignupComponent } from './examples/signup/signup.component';
import { NucleoiconsComponent } from './components/nucleoicons/nucleoicons.component';
import { HomeComponent } from './components/home/home.component';
import { ExtractComponent } from './components/extract/extract.component';
import { CallbackComponent } from './components/callback/callback.component';
import { ExploreComponent } from './components/explore/explore.component';

const routes: Routes = [
  // { path: 'components', component: ComponentsComponent },

  { path: '', redirectTo: 'faq/home', pathMatch: 'full' },
  { path: 'faq/callback', component: CallbackComponent },
  { path: 'faq/extract', component: ExtractComponent },
  { path: 'faq/explore', component: ExploreComponent },
  // { path: 'faq/signup', component: SignupComponent },
  { path: 'faq/home', component: HomeComponent },
  { path: 'faq/nucleoicons', component: NucleoiconsComponent }
];

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
  ],
})
export class AppRoutingModule { }
