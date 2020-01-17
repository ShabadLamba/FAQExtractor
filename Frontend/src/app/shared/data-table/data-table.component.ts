import {
  Component,
  OnInit,
  SimpleChanges,
  forwardRef,
  ViewChild,
  Input
} from '@angular/core';
import { AngularFireDatabase, listChanges } from '@angular/fire/database';
import * as _ from 'lodash';
import { NgForm } from '@angular/forms';
import { ExtractApiService } from '../../services/faq/fetch/extract-api.service';

@Component({
  selector: 'app-data-table',
  templateUrl: './data-table.component.html',
  styleUrls: ['./data-table.component.scss']
})
export class DataTableComponent implements OnInit {

  constructor(
    private db: AngularFireDatabase,
    private extractFAQApi: ExtractApiService,
  ) { }

  /*
    Variables
   */

  // tslint:disable: member-ordering
  items: any;
  filteredItems: any;
  filters = {};
  @Input() listOfItems: Array<any> = [];
  @Input() filename = '';
  listOfQnA: Array<any> = [];
  listOfSelectedQnA: Array<any> = [];
  // tslint:disable-next-line: ban-types
  @Input() showData: Boolean = false;
  disabled = true;
  // tslint:disable-next-line: member-ordering
  editField: string;
  /* Class Functions */

  getData() {
    for (const item in this.listOfItems) {
      // tslint:disable-next-line: forin
      this.listOfQnA.push(this.listOfItems[item]);
    }
  }

  toggleShowData() {
    if (!this.showData) {
      // console.log(this.listOfQnA);
      this.getData();
    } else {
      this.listOfQnA = [];
    }
    this.showData = !this.showData;
  }

  applyFilters() {
    this.filteredItems = _.filter(this.items, _.conforms(this.filters));
  }

  onSubmit(form: NgForm) {
    console.log('In Submit: ', form.valid);
  }

  updateList(id: number, property: string, event: any) {
    const editField = event.target.textContent;
    this.listOfQnA[id][property] = editField;
  }

  changeValue(id: number, property: string, event: any) {
    this.editField = event.target.textContent;
  }

  onSelected(id: any) {
    const selectedElement = this.listOfQnA[id];
    if (
      this.listOfSelectedQnA.some(
        item => item.question === selectedElement.question
      )
    ) {
      // tslint:disable-next-line: only-arrow-functions
      this.listOfSelectedQnA = this.listOfSelectedQnA.filter(function (value) {
        return value !== selectedElement;
      });
    } else {
      this.listOfSelectedQnA.push(selectedElement);
    }
    console.log(this.listOfSelectedQnA);
  }

  selectAll() {
    this.disabled = !this.disabled;
    console.log('CheckBoxes Disabled ', this.disabled);
    if (this.disabled) {
      this.listOfSelectedQnA.splice(0, this.listOfSelectedQnA.length);
    } else {
      this.listOfSelectedQnA = [...this.listOfQnA];
    }
    // console.log("List Of Questions ", this.listOfQnA);
    // console.log("List Of Selected Questions ", this.listOfSelectedQnA);
  }
  /* Angular Functions */

  ngOnInit() {
    this.toggleShowData();
  }

}
