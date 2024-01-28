/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { HomepageService } from './homepage.service';

describe('Service: Homepage', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HomepageService]
    });
  });

  it('should ...', inject([HomepageService], (service: HomepageService) => {
    expect(service).toBeTruthy();
  }));
});
