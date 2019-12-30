import { Component, OnInit } from '@angular/core';
import * as Auth0 from 'auth0-web';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent implements OnInit {
  pageTitle = 'Questions And Answers Scrapper';
  authenticated = false;

  constructor() { }

  signIn = Auth0.signIn;
  signOut = Auth0.signOut;
  getProfile = Auth0.getProfile;

  ngOnInit() {
    const self = this;
    console.log(this.authenticated);
    Auth0.subscribe((authenticated) => (self.authenticated = authenticated));
  }
}
