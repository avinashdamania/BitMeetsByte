import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Tab2Page } from './tab2.page';
import {HttpClient} from '@angular/common/http'
import { HttpHeaders } from '@angular/common/http';
import {User} from './User';
@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    RouterModule.forChild([{ path: '', component: Tab2Page }])
  ],
  declarations: [Tab2Page]
})
export class Tab2PageModule {
  link = 'https://bit-meets-byte.appspot.com/'
  id_num = 20;
  userList:Array<User> = []
  constructor(private http: HttpClient)
  {

  }
  async ionViewWillEnter() {
    console.log('hi')
    await this.getInfo();
  }
  getInfo()
  {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
        'Authorization': 'my-auth-token'
      })};
    return this.http.post(this.link + '/deets', {id:1}).subscribe(data =>{
      console.log(data)
      this.userList.push(new User(data['first_name'],data['last_name'],data['bio'],data['memo'],data['age'],data['skill']));
    },
    err => console.log(err),);
  }
}
