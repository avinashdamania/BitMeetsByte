import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { TabsPageRoutingModule } from './tabs.router.module';
import {LoginPageModule} from '../login/login.module';
import { TabsPage } from './tabs.page';
@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    TabsPageRoutingModule,
    LoginPageModule
  ],
  declarations: [TabsPage]
})
export class TabsPageModule {}
