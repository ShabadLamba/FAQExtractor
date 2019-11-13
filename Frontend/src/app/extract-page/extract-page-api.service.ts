import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { API_URL } from '../env';
import { FAQ } from './extract-page.model';

@Injectable({
  providedIn: 'root'
})
export class ExtractPageApiService {
  constructor(private http: HttpClient) { }

  // GET list of public, future events
  fetchQnA(body: FAQ): Observable<FAQ[]> {
    // tslint:disable-next-line: max-line-length
    const output: Observable<any> = this.http.post(`${API_URL}/faq/extractByUrl/Hierarchy`, body)
      // .catch(this.handleError);
      .pipe(catchError((err) => {
        console.log('Error: Unable to complete request...', err.message);
        return throwError(err);
      }));
    return output;
  }

  fetchQnAFromFirebase(body: FAQ): Observable<FAQ[]> {
    // tslint:disable-next-line: max-line-length
    const output: Observable<any> = this.http.post(`${API_URL}/faq/extractByUrl/GetData/Firebase`, body)
      // .catch(this.handleError);
      .pipe(catchError((err) => {
        console.log('Error: Unable to complete request...', err.message);
        return throwError(err);
      }));
    return output;
  }
}
