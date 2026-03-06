import { Component, inject, HostListener, signal } from '@angular/core';
import { ThemeService } from '../../../core/services/theme.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './header.html',
  styleUrl: './header.scss',
})
export class Header {
  readonly themeService = inject(ThemeService);
  readonly menuOpen = signal(false);
  readonly scrolled = signal(false);

  @HostListener('window:scroll')
  onScroll(): void {
    this.scrolled.set(window.scrollY > 50);
  }

  toggleMenu(): void {
    this.menuOpen.update((v) => !v);
  }

  closeMenu(): void {
    this.menuOpen.set(false);
  }

  cycleTheme(): void {
    this.themeService.cycleTheme();
  }

  readonly navItems = [
    { href: '#home', label: 'Accueil' },
    { href: '#about', label: 'À propos' },
    { href: '#services', label: 'Compétences' },
    { href: '#resume', label: 'Parcours' },
    { href: '#portfolio', label: 'Projets' },
    { href: '#contact', label: 'Contact' },
  ];
}
