import { Injectable } from '@angular/core';
import { saveAs } from 'file-saver';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  // downloadFile(data, filename = 'data') {
  //   const csvData = this.ConvertToCSV(data, ['category', 'answer', 'question']);
  //   console.log(csvData);
  //   const blob = new Blob(['\ufeff' + csvData], { type: 'text/csv;charset=utf-8;' });
  //   const dwldLink = document.createElement('a');
  //   const url = URL.createObjectURL(blob);
  //   const isSafariBrowser = navigator.userAgent.indexOf('Safari') !== -1 && navigator.userAgent.indexOf('Chrome') === -1;
  //   if (isSafariBrowser) {  // if Safari open in new window to save file with random filename.
  //     dwldLink.setAttribute('target', '_blank');
  //   }
  //   dwldLink.setAttribute('href', url);
  //   dwldLink.setAttribute('download', filename + '.csv');
  //   dwldLink.style.visibility = 'hidden';
  //   document.body.appendChild(dwldLink);
  //   dwldLink.click();
  //   document.body.removeChild(dwldLink);
  // }

  ConvertToCSV(objArray, headerList) {
    const array = typeof objArray !== 'object' ? JSON.parse(objArray) : objArray;
    let str = '';
    let row = 'S.No,';
    console.log(Object.keys(array[0]));

    // tslint:disable-next-line: forin
    for (const index in headerList) {
      row += headerList[index] + ',';
    }

    row = row.slice(0, -1);
    str += row + '\r\n';

    for (let i = 0; i < array.length; i++) {
      let line = (i + 1) + '';
      // tslint:disable-next-line: forin
      for (const index in headerList) {
        const head = headerList[index];
        line += ',' + array[i][head];
      }
      str += line + '\r\n';
    }
    return str;
  }

  downloadFile(data: any, filename = 'data') {
    const replacer = (key, value) => value === null ? '' : value; // specify how you want to handle null values here
    const header = Object.keys(data[0]);
    const csv = data.map(row => header.map(fieldName => JSON.stringify(row[fieldName], replacer)).join(','));
    csv.unshift(header.join(','));
    const csvArray = csv.join('\r\n');

    const a = document.createElement('a');
    // tslint:disable-next-line: one-variable-per-declaration
    const blob = new Blob([csvArray], { type: 'text/csv' }),
      url = window.URL.createObjectURL(blob);

    a.href = url;
    a.download = filename + '.csv';
    a.click();
    window.URL.revokeObjectURL(url);
    a.remove();
  }

  downloadFileSaver(data: any) {
    const replacer = (key, value) => value === null ? '' : value; // specify how you want to handle null values here
    const header = Object.keys(data[0]);
    const csv = data.map(row => header.map(fieldName => JSON.stringify(row[fieldName], replacer)).join(','));
    csv.unshift(header.join(','));
    const csvArray = csv.join('\r\n');

    const blob = new Blob([csvArray], { type: 'text/csv' })
    saveAs(blob, 'myFile.csv');
  }
}
