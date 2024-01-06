import { Spectator, createComponentFactory } from '@ngneat/spectator';
import { NavbarComponent } from './navbar.component';

describe('NavbarComponent', () => {
  let spectator: Spectator<NavbarComponent>;
  const createComponent = createComponentFactory(NavbarComponent);

  beforeEach(() => {
    spectator = createComponent();
  });

  it('should create', () => {
    expect(spectator.component).toBeTruthy();
  });
});
