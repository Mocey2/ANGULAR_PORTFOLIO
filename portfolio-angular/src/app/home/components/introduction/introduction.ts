import { Component, inject, signal, OnInit, OnDestroy } from '@angular/core';
import { PortfolioApiService, type Profile } from '../../../core/api/portfolio-api.service';

@Component({
  selector: 'app-introduction',
  standalone: true,
  imports: [],
  templateUrl: './introduction.html',
  styleUrl: './introduction.scss',
})
export class Introduction implements OnInit, OnDestroy {
  private readonly api = inject(PortfolioApiService);
  readonly profile = signal<Profile | null>(null);
  readonly words = ['Python', 'Flutter', 'Django'];
  readonly currentWord = signal('Python');
  private interval: ReturnType<typeof setInterval> | null = null;

  ngOnInit(): void {
    this.api.getProfile().subscribe((p) => this.profile.set(p));
    let idx = 0;
    this.interval = setInterval(() => {
      idx = (idx + 1) % this.words.length;
      this.currentWord.set(this.words[idx]);
    }, 2500);
  }

  ngOnDestroy(): void {
    if (this.interval) clearInterval(this.interval);
  }

  get firstName(): string {
    return this.profile()?.first_name || 'Océane';
  }

  get lastName(): string {
    return this.profile()?.last_name || 'Konan';
  }

  get headline(): string {
    return this.profile()?.headline || 'Génie Logiciel';
  }

  get photoUrl(): string | null {
    return this.profile()?.photo_url || null;
  }
}
