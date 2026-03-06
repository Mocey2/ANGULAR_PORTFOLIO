import { Component, signal, OnInit } from '@angular/core';

@Component({
  selector: 'app-preloader',
  standalone: true,
  imports: [],
  templateUrl: './preloader.html',
  styleUrl: './preloader.scss',
})
export class Preloader implements OnInit {
  readonly visible = signal(true);

  ngOnInit(): void {
    window.addEventListener('load', () => {
      this.visible.set(false);
    });
    setTimeout(() => this.visible.set(false), 1500);
  }
}
