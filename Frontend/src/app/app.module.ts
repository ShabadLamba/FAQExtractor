import { BrowserModule } from "@angular/platform-browser";
import { NgModule } from "@angular/core";
import { RouterModule } from "@angular/router";
import { FormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
import { AngularFireModule } from "@angular/fire";
import { environment } from "../environments/environment";
import { AngularFireDatabaseModule } from "@angular/fire/database";
import { AngularFireStorageModule } from "@angular/fire/storage";
import { AppRoutingModule } from "./app-routing.module";
import { AppComponent } from "./app.component";
import { HomePageComponent } from "./home-page/home-page.component";
import { ExtractPageComponent } from "./extract-page/extract-page.component";
import { ExplorePageComponent } from "./explore-page/explore-page.component";
import { DataDisplayComponent } from "./data-display/data-display.component";
import { DataTablesModule } from "angular-datatables";
import { ButtonsModule } from "ngx-bootstrap/buttons";
import { ExtractPageApiService } from "./extract-page/extract-page-api.service";
import { AppService } from "./app.service";
import { ExtractComponent } from "./components/extract/extract.component";
import { LoginComponent } from './components/login/login.component';
import { CallbackComponent } from './components/login/callback.component';
import * as Auth0 from 'auth0-web';


@NgModule({
  declarations: [
    AppComponent,
    HomePageComponent,
    ExtractPageComponent,
    ExplorePageComponent,
    DataDisplayComponent,
    ExtractComponent,
    LoginComponent,
    CallbackComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: 'callback', component: CallbackComponent },
      { path: "faq/login", component: LoginComponent },
      { path: "faq/extract", component: ExtractPageComponent },
      { path: "faq/explore", component: ExplorePageComponent },
      { path: "faq/extractNew", component: ExtractComponent },
      { path: "faq/home", component: HomePageComponent },
      { path: "", redirectTo: "faq/home", pathMatch: "full" },
      { path: "**", redirectTo: "faq/home", pathMatch: "full" }
    ]),
    AngularFireModule.initializeApp(environment.firebase),
    AngularFireDatabaseModule,
    AngularFireStorageModule,
    DataTablesModule,
    ButtonsModule.forRoot()
  ],
  providers: [ExtractPageApiService, AppService],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor() {
    Auth0.configure({
      domain: 'dev-g-e5tghp.auth0.com',
      audience: 'https://faq-extractor/',
      clientID: 'whRkHg3bb07JVZwADShOqvT5MkBuQuAO',
      redirectUri: 'http://localhost:4200/callback',
      scope: 'openid profile extract:Hierarchy extract:NLP extract:Firebase'
    });
  }
}
