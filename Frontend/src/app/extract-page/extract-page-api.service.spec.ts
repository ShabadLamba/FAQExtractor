import { TestBed } from '@angular/core/testing';

import { ExtractPageApiService } from './extract-page-api.service';

describe('ExtractPageApiService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ExtractPageApiService = TestBed.get(ExtractPageApiService);
    expect(service).toBeTruthy();
  });
});
