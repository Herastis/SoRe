import { Component, OnInit } from '@angular/core';
import { HomepageService } from '../services/homepage.service';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {

  text: string = '';
  constructor(private readonly service: HomepageService) { }

  ngOnInit(): void {
    this.service.getHomepage().subscribe(value => {
      this.text = value;
    })
  }
}
