import { Component, inject, signal, OnInit } from '@angular/core';
import { PortfolioApiService, type Fact } from '../../../core/api/portfolio-api.service';

@Component({
  selector: 'app-facts',
  standalone: true,
  imports: [],
  templateUrl: './facts.html',
  styleUrl: './facts.scss',
})
export class Facts implements OnInit {
  private readonly api = inject(PortfolioApiService);
  readonly facts = signal<Fact[]>([]);

  ngOnInit(): void {
    this.api.getFacts().subscribe((f) => this.facts.set(f));
  }
}
