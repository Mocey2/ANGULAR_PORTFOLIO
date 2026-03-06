import { Component, inject, signal, OnInit } from '@angular/core';
import { PortfolioApiService, type Interest } from '../../../core/api/portfolio-api.service';

@Component({
  selector: 'app-testimonial',
  standalone: true,
  imports: [],
  templateUrl: './testimonial.html',
  styleUrl: './testimonial.scss',
})
export class Testimonial implements OnInit {
  private readonly api = inject(PortfolioApiService);
  readonly interests = signal<Interest[]>([]);

  ngOnInit(): void {
    this.api.getInterests().subscribe((i) => this.interests.set(i));
  }
}
