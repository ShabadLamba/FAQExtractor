import { TestBed } from '@angular/core/testing';

import { ExtractApiService } from './extract-api.service';

describe('ExtractApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ExtractApiService = TestBed.get(ExtractApiService);
    expect(service).toBeTruthy();
  });
});
