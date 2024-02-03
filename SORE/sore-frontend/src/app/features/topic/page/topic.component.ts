import { Component, OnInit } from '@angular/core';
import { TopicService } from '../services/topic.service';
import { ActivatedRoute } from '@angular/router';
import { TopicType } from '../types/topic.type';


@Component({
  selector: 'app-topic',
  templateUrl: './topic.component.html',
  styleUrls: ['./topic.component.scss']
})
export class TopicComponent implements OnInit {

  //text: string = '';
  newsItems: TopicType[] = [];
  currentTab: string = '';
  constructor(private readonly service: TopicService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.url.subscribe(urlSegments => {
      this.currentTab = urlSegments[0].path;
      this.service.loadTopicData(this.currentTab).subscribe(value => {
        this.newsItems = value;
      });
    });
  }

  like(post: TopicType) {

  }

  connect(post: TopicType) {
    
  }
}
