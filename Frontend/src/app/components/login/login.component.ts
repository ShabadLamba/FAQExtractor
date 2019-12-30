import { Component, OnDestroy, OnInit } from '@angular/core';
import * as Auth0 from 'auth0-web';
import { Subscription } from 'rxjs';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

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
