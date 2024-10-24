import { Injectable } from '@angular/core';
import { User } from '../user';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environment/environment';

@Injectable({
  providedIn: 'root'
})
export class MsaService {

  constructor(private http: HttpClient) { 
    
  }
  create(user: User) {
    this.http.post(`${environment.baseUrl}signUp`, user);
  }
}
