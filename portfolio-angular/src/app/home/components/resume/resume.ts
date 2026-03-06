import { Component, inject, signal, OnInit } from '@angular/core';
import { PortfolioApiService } from '../../../core/api/portfolio-api.service';
import type { Education, Experience, Skill } from '../../../core/api/portfolio-api.service';

@Component({
  selector: 'app-resume',
  standalone: true,
  imports: [],
  templateUrl: './resume.html',
  styleUrl: './resume.scss',
})
export class Resume implements OnInit {
  private readonly api = inject(PortfolioApiService);
  readonly education = signal<Education[]>([]);
  readonly experience = signal<Experience[]>([]);
  readonly skills = signal<Skill[]>([]);

  ngOnInit(): void {
    this.api.getEducation().subscribe((e) => this.education.set(e));
    this.api.getExperience().subscribe((e) => this.experience.set(e));
    this.api.getSkills().subscribe((s) => this.skills.set(s));
  }
}
