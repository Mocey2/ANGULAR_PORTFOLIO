import { Injectable, signal, computed, effect } from '@angular/core';

export type ThemeMode = 'dark' | 'light' | 'colorful';

@Injectable({ providedIn: 'root' })
export class ThemeService {
  private readonly storageKey = 'portfolio-theme';

  readonly theme = signal<ThemeMode>(
    (localStorage.getItem(this.storageKey) as ThemeMode) || 'dark'
  );

  readonly isDark = computed(() => this.theme() === 'dark');
  readonly isLight = computed(() => this.theme() === 'light');
  readonly isColorful = computed(() => this.theme() === 'colorful');

  constructor() {
    effect(() => {
      const mode = this.theme();
      localStorage.setItem(this.storageKey, mode);
      this.applyTheme(mode);
    });
  }

  setTheme(mode: ThemeMode): void {
    this.theme.set(mode);
  }

  cycleTheme(): void {
    const order: ThemeMode[] = ['dark', 'light', 'colorful'];
    const idx = order.indexOf(this.theme());
    this.theme.set(order[(idx + 1) % 3]);
  }

  private applyTheme(mode: ThemeMode): void {
    const root = document.documentElement;

    switch (mode) {
      case 'dark':
        root.style.setProperty('--bg-primary', '#0a0a0f');
        root.style.setProperty('--bg-secondary', '#12121a');
        root.style.setProperty('--bg-tertiary', '#1a1a25');
        root.style.setProperty('--text-primary', '#e8e8f0');
        root.style.setProperty('--text-secondary', '#a0a0b8');
        root.style.setProperty('--accent-primary', '#00f5ff');
        root.style.setProperty('--accent-secondary', '#ff00aa');
        root.style.setProperty('--accent-tertiary', '#8b5cf6');
        root.style.setProperty('--neon-glow', 'rgba(0, 245, 255, 0.4)');
        root.style.setProperty('--border-subtle', 'rgba(255, 255, 255, 0.06)');
        root.style.setProperty('--card-bg', 'rgba(18, 18, 26, 0.8)');
        break;
      case 'light':
        root.style.setProperty('--bg-primary', '#f8fafc');
        root.style.setProperty('--bg-secondary', '#ffffff');
        root.style.setProperty('--bg-tertiary', '#f1f5f9');
        root.style.setProperty('--text-primary', '#0f172a');
        root.style.setProperty('--text-secondary', '#475569');
        root.style.setProperty('--accent-primary', '#0891b2');
        root.style.setProperty('--accent-secondary', '#db2777');
        root.style.setProperty('--accent-tertiary', '#7c3aed');
        root.style.setProperty('--neon-glow', 'rgba(8, 145, 178, 0.3)');
        root.style.setProperty('--border-subtle', 'rgba(0, 0, 0, 0.08)');
        root.style.setProperty('--card-bg', 'rgba(255, 255, 255, 0.9)');
        break;
      case 'colorful':
        root.style.setProperty('--bg-primary', '#0d0d14');
        root.style.setProperty('--bg-secondary', '#14141f');
        root.style.setProperty('--bg-tertiary', '#1e1e2e');
        root.style.setProperty('--text-primary', '#f0f0ff');
        root.style.setProperty('--text-secondary', '#b8b8d0');
        root.style.setProperty('--accent-primary', '#ff00aa');
        root.style.setProperty('--accent-secondary', '#00f5ff');
        root.style.setProperty('--accent-tertiary', '#a855f7');
        root.style.setProperty('--neon-glow', 'rgba(255, 0, 170, 0.5)');
        root.style.setProperty('--border-subtle', 'rgba(168, 85, 247, 0.2)');
        root.style.setProperty('--card-bg', 'rgba(20, 20, 31, 0.85)');
        break;
    }

    root.setAttribute('data-theme', mode);
  }
}
