import { Component, OnInit } from '@angular/core';
import * as Auth0 from 'auth0-web';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  pageTitle = 'Questions And Answers Scrapper';
  authenticated = true;

  focus: any;
  focus1: any;

  constructor() { }

  ngOnInit() {
    const self = this;
    console.log(this.authenticated);
    Auth0.subscribe((authenticated) => (self.authenticated = authenticated));
  }

}
