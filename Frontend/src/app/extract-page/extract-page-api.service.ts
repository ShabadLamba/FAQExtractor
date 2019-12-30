import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../env';
import { FAQ } from './extract-page.model';
import * as Auth0 from 'auth0-web';


@Injectable({
  providedIn: 'root'
})
export class ExtractPageApiService {
  constructor(private http: HttpClient) { }

  // GET list of public, future events
  fetchQnA(body: FAQ): Observable<FAQ[]> {
    // tslint:disable-next-line: max-line-length
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${Auth0.getAccessToken()}`
      })
    };
    const output: Observable<any> = this.http.post(`https://dev.imibot.ai/faq/v2/extractByUrl/Hierarchy`, body, httpOptions)
      // .catch(this.handleError);
      .pipe(catchError((err) => {
        console.log('Error: Unable to complete request...', err.message);
        return throwError(err);
      }));
    return output;
  }

  fetchQnAFromFirebase(body: FAQ): Observable<FAQ[]> {
    // tslint:disable-next-line: max-line-length
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${Auth0.getAccessToken()}`
      })
    };
    const output: Observable<any> = this.http.post(`https://dev.imibot.ai/faq/v2/extractByUrl/GetData/Firebase`, body, httpOptions)
      // .catch(this.handleError);
      .pipe(catchError((err) => {
        console.log('Error: Unable to complete request...', err.message);
        return throwError(err);
      }));
    return output;
  }

  fetchQnANLP(body: FAQ): Observable<FAQ[]> {
    // tslint:disable-next-line: max-line-length
    const httpOptions = {
      headers: new HttpHeaders({
        'Authorization': `Bearer ${Auth0.getAccessToken()}`
      })
    };
    const output: Observable<any> = this.http.post(`https://dev.imibot.ai/faq/v2/extractByUrl/NLP`, body, httpOptions)
      // .catch(this.handleError);
      .pipe(catchError((err) => {
        console.log('Error: Unable to complete request...', err.message);
        return throwError(err);
      }));
    return output;
  }
}
