import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';
import { NouisliderModule } from 'ng2-nouislider';
import { JwBootstrapSwitchNg2Module } from 'jw-bootstrap-switch-ng2';
import { RouterModule } from '@angular/router';
import { DataTablesModule } from 'angular-datatables';
import { ButtonsModule } from 'ngx-bootstrap/buttons';

import { NucleoiconsComponent } from './nucleoicons/nucleoicons.component';
import { ComponentsComponent } from './components.component';
import { ExtractComponent } from './extract/extract.component';
import { HomeComponent } from './home/home.component';
import { ExploreComponent } from './explore/explore.component';
import { CallbackComponent } from './callback/callback.component';
import { DataTableComponent } from 'app/shared/data-table/data-table.component';

import { AngularFireDatabaseModule } from '@angular/fire/database';
import { AngularFireStorageModule } from '@angular/fire/storage';
import { AngularFireModule } from '@angular/fire';
import { environment } from '../../environments/environment';
import { DownloadFileComponent } from 'app/shared/download-file/download-file.component';

@NgModule({
    imports: [
        CommonModule,
        FormsModule,
        NgbModule,
        NouisliderModule,
        RouterModule,
        JwBootstrapSwitchNg2Module,
        AngularFireModule.initializeApp(environment.firebase),
        AngularFireDatabaseModule,
        AngularFireStorageModule,
        ButtonsModule.forRoot(),
        DataTablesModule
    ],
    declarations: [
        ComponentsComponent,
        NucleoiconsComponent,
        ExtractComponent,
        HomeComponent,
        ExploreComponent,
        CallbackComponent,
        DataTableComponent,
        DownloadFileComponent,
    ],
    // entryComponents: [NgbdModalContent],
    exports: [ComponentsComponent]
})
export class ComponentsModule { }
