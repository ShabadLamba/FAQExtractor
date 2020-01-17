import { Component, OnInit, Input, ElementRef, ViewChild } from '@angular/core';
import { FilesService } from './../../services/download/files.service';
import { error } from 'util';

@Component({
  selector: 'app-download-file',
  templateUrl: './download-file.component.html',
  styleUrls: ['./download-file.component.scss']
})
export class DownloadFileComponent implements OnInit {

  @Input() listOfSelectedQnA: Array<any>;
  filename_out = '';
  @ViewChild('filename', { static: true }) filename: ElementRef;

  focus: any;
  focus1: any;

  constructor(private filesService: FilesService) { }

  ngOnInit() { }

  download() {
    if (this.listOfSelectedQnA.length !== 0) {
      this.filesService.downloadFile(this.listOfSelectedQnA, this.filename.nativeElement.value);
    } else {
      alert("No FAQ selected!!");
    }
  }
}
