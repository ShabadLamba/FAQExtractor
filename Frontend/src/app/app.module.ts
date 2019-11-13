import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AngularFireModule } from '@angular/fire';
import { environment } from '../environments/environment';
import { AngularFireDatabaseModule } from '@angular/fire/database';
import { AngularFireStorageModule } from '@angular/fire/storage';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomePageComponent } from './home-page/home-page.component';
import { ExtractPageComponent } from './extract-page/extract-page.component';
import { ExplorePageComponent } from './explore-page/explore-page.component';
import { DataDisplayComponent } from './data-display/data-display.component';
import { DataTablesModule } from 'angular-datatables';
import { ButtonsModule } from 'ngx-bootstrap/buttons';
import { ExtractPageApiService } from './extract-page/extract-page-api.service';
import { AppService } from './app.service';

@NgModule({
  declarations: [AppComponent, HomePageComponent, ExtractPageComponent, ExplorePageComponent, DataDisplayComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot([
      { path: 'extract', component: ExtractPageComponent },
      { path: 'explore', component: ExplorePageComponent },
      { path: 'home', component: HomePageComponent },
      { path: '', redirectTo: 'home', pathMatch: 'full' },
      { path: '**', redirectTo: 'home', pathMatch: 'full' }
    ]),
    AngularFireModule.initializeApp(environment.firebase),
    AngularFireDatabaseModule,
    AngularFireStorageModule,
    DataTablesModule,
    ButtonsModule.forRoot()
  ],
  providers: [
    ExtractPageApiService,
    AppService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
