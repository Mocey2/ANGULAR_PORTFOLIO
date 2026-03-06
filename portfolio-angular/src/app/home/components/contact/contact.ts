import { Component, inject, signal } from '@angular/core';
import { PortfolioApiService, type Profile } from '../../../core/api/portfolio-api.service';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [],
  templateUrl: './contact.html',
  styleUrl: './contact.scss',
})
export class Contact {
  private readonly api = inject(PortfolioApiService);
  readonly profile = signal<Profile | null>(null);
  readonly loading = signal(false);
  readonly success = signal(false);
  readonly error = signal<string | null>(null);

  constructor() {
    this.api.getProfile().subscribe((p) => this.profile.set(p));
  }

  onSubmit(form: HTMLFormElement): void {
    const formData = new FormData(form);
    const name = (formData.get('name') as string)?.trim();
    const email = (formData.get('email') as string)?.trim();
    const subject = (formData.get('subject') as string)?.trim();
    const message = (formData.get('message') as string)?.trim();
    if (!name || !email || !subject || !message) {
      this.error.set('Veuillez remplir tous les champs.');
      return;
    }
    this.loading.set(true);
    this.error.set(null);
    this.success.set(false);
    this.api.sendContact({ name, email, subject, message }).subscribe({
      next: () => {
        this.success.set(true);
        form.reset();
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set(err?.error?.message || 'Erreur lors de l\'envoi. Vérifiez que le backend est démarré.');
        this.loading.set(false);
      },
    });
  }
}
