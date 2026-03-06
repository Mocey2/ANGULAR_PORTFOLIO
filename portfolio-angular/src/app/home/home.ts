import { Component, inject, HostListener, signal } from '@angular/core';
import { Header } from '../shared/components/header/header';
import { Preloader } from '../shared/components/preloader/preloader';
import { Introduction } from './components/introduction/introduction';
import { About } from './components/about/about';
import { Facts } from './components/facts/facts';
import { Services } from './components/services/services';
import { Portfolio } from './components/portfolio/portfolio';
import { Projet } from './components/projet/projet';
import { Resume } from './components/resume/resume';
import { Testimonial } from './components/testimonial/testimonial';
import { Contact } from './components/contact/contact';
import { Footer } from '../shared/components/footer/footer';
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    Header,
    Preloader,
    Introduction,
    About,
    Facts,
    Services,
    Portfolio,
    Projet,
    Resume,
    Testimonial,
    Contact,
    Footer,
  ],
  templateUrl: './home.html',
  styleUrl: './home.scss',
})
export class Home {
  readonly showToTop = signal(false);

  @HostListener('window:scroll')
  onScroll(): void {
    this.showToTop.set(window.scrollY > 400);
  }

  scrollToTop(): void {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

}
