import {
  Component,
  OnInit,
  OnChanges,
  SimpleChanges,
  Input
} from '@angular/core';
import * as _ from 'lodash';
import { ExtractApiService } from '../../services/faq/fetch/extract-api.service';
import { FAQ } from './extract.model';
import { Router, ActivatedRoute } from '@angular/router';
import { isBoolean } from 'util';

export enum websiteType {
  samePageQnALoadedWithWebsite = 0,
  samePageQnALoadedAfterWebsiteIsLoaded,
  QuestionsAreLinksToAnswers
}

@Component({
  selector: 'app-extract',
  templateUrl: './extract.component.html',
  styleUrls: ['./extract.component.scss']
})
export class ExtractComponent implements OnInit, OnChanges {
  // static url_: any;
  constructor(
    private extractFAQApi: ExtractApiService,
    private router: Router,
    private route: ActivatedRoute
  ) { }

  // tslint:disable: member-ordering

  extractPageTitle = 'Extract Questions And Answers';
  @Input() url = '';
  @Input() fileName = '';
  @Input() typeOfWebsite: number = websiteType.QuestionsAreLinksToAnswers;
  @Input() showData = false;
  @Input() methodOfExtraction: number = null;
  authenticated = false;
  startloading = false;


  public isDataFetched = false;
  outputLink = 'https://experience.imiconnect.io/faqs/';

  items: any;
  filteredItems: any;
  filters = {};

  // tslint:disable-next-line: variable-name
  fetchData(url_: string, fileName_: string, typeOfWebsite_: number, methodOfExtraction_: number) {
    const body: FAQ = {
      // tslint:disable-next-line: max-line-length
      access_token: 'gAAAAABd54JjdQJuW4NCIQopW_uPmVi5Yl8hiF-et3CEflvABusLeHa9KsmONFa7XlVrFKcsPoB726W0_Q6Dur7Md4LR47UQF5XZhol64TpkW9WYpdiIBTA=',
      url: url_,
      fileName: fileName_,
      typeOfWebsite: typeOfWebsite_,
      methodOfExtraction: methodOfExtraction_
    };
    this.route.params.subscribe(params => {
      if (this.route.snapshot.paramMap.get('ifAuthenticated') === 'true') {
        this.authenticated = true;
      }
    });
    this.isDataFetched = false;
    this.showData = false;
    console.log(body)
    if (this.authenticated) {
      if (body.methodOfExtraction === 0) {
        this.extractFAQApi.fetchQnAFromFirebase(body).subscribe(
          // tslint:disable-next-line: triple-equals
          value => {
            if (!value[0]) {
              // console.log(!value[0]);
              this.extractFAQApi.fetchQnA(body).subscribe(
                // tslint:disable: no-shadowed-variable
                value => {
                  console.log('Inside Value');
                  this.items = value;
                  this.isDataFetched = true;
                },
                error => {
                  alert(error.message);
                  console.log('Inside Fetch Error');
                  this.isDataFetched = false;
                }
              );
            } else {
              console.log('Inside Get Value');
              this.items = value;
              this.isDataFetched = true;
            }
          },
          error => {
            alert(error.message);
            console.log('Inside Get Error');
            this.isDataFetched = false;
          }
        );
      }
      // tslint:disable: one-line
      else if (body.methodOfExtraction === 1) {
        this.extractFAQApi.fetchQnANLP(body).subscribe(
          value => {
            console.log('Inside Value');
            this.items = value;
            this.isDataFetched = true;
          },
          error => {
            alert(error.message);
            console.log('Inside Fetch Error');
            this.isDataFetched = false;
          }
        );
      }
      else {
        alert('Not a Valid method of extraction choosen');
        console.log('Inside Get Error');
        this.isDataFetched = false;
      }
    }
    else {
      alert('Sign In To Continue...');
      this.router.navigate(['/faq/home']);
    }
  }

  ngOnInit() { }

  ngOnChanges(changes: SimpleChanges): void {
    this.isDataFetched = false;
  }
}
