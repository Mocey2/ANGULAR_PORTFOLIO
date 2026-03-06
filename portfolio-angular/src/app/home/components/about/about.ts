import { Component, inject, signal, OnInit } from '@angular/core';
import { PortfolioApiService, type Profile } from '../../../core/api/portfolio-api.service';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [],
  templateUrl: './about.html',
  styleUrl: './about.scss',
})
export class About implements OnInit {
  private readonly api = inject(PortfolioApiService);
  readonly profile = signal<Profile | null>(null);

  ngOnInit(): void {
    this.api.getProfile().subscribe((p) => this.profile.set(p));
  }
}
