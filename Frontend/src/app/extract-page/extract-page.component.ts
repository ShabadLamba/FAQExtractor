import { Component, OnInit, OnChanges, SimpleChanges, Input } from '@angular/core';
import * as _ from 'lodash';
import { ExtractPageApiService } from './extract-page-api.service';
import { FAQ } from './extract-page.model';
import { Router } from '@angular/router';
import { isBoolean } from 'util';

export enum websiteType {
  samePageQnALoadedWithWebsite = 0,
  samePageQnALoadedAfterWebsiteIsLoaded,
  QuestionsAreLinksToAnswers
}

@Component({
  templateUrl: './extract-page.component.html',
  styleUrls: ['./extract-page.component.css']
})
export class ExtractPageComponent implements OnInit, OnChanges {
  // static url_: any;
  constructor(private extractFAQApi: ExtractPageApiService, private router: Router) { }

  extractPageTitle = 'Extract Questions And Answers';
  @Input() url = '';
  @Input() fileName = '';
  @Input() typeOfWebsite: number = websiteType.QuestionsAreLinksToAnswers;

  public isDataFetched = false;
  outputLink = 'https://experience.imiconnect.io/faqs/';

  items: any;
  filteredItems: any;
  filters = {};

  // tslint:disable-next-line: variable-name
  fetchData(url_: string, fileName_: string, typeOfWebsite_: number) {
    const body: FAQ = {
      url: url_,
      fileName: fileName_,
      typeOfWebsite: typeOfWebsite_
    };
    console.log(body);
    this.extractFAQApi.fetchQnAFromFirebase(body).subscribe(
      // tslint:disable-next-line: triple-equals
      (value) => {
        if (!value[0]) {
          console.log(!value[0]);
          this.extractFAQApi.fetchQnA(body).subscribe(
            (value) => {
              console.log("Inside Value")
              this.items = value;
              this.isDataFetched = true;
            },
            (error) => {
              alert(error.message);
              console.log("Inside Fetch Error")
              this.isDataFetched = false;
            })
        }
        else {
          console.log("Inside Get Value")
          this.items = value;
          this.isDataFetched = true;
        }
      },
      (error) => {
        alert(error.message);
        console.log("Inside Get Error")
        this.isDataFetched = false;
      });
  }

  ngOnInit() { }

  ngOnChanges(changes: SimpleChanges): void {
    this.isDataFetched = false;
  }
}
