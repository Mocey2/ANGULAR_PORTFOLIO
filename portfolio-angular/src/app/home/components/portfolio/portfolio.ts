import { Component, inject, signal, OnInit } from '@angular/core';
import { PortfolioApiService, type Project } from '../../../core/api/portfolio-api.service';

@Component({
  selector: 'app-portfolio',
  standalone: true,
  imports: [],
  templateUrl: './portfolio.html',
  styleUrl: './portfolio.scss',
})
export class Portfolio implements OnInit {
  private readonly api = inject(PortfolioApiService);
  readonly selectedProject = signal<Project | null>(null);
  readonly projects = signal<Project[]>([]);
  readonly academiques = signal<Project[]>([]);
  readonly personnels = signal<Project[]>([]);

  ngOnInit(): void {
    this.api.getProjects().subscribe((p) => {
      this.projects.set(p);
      this.academiques.set(p.filter((x) => x.type === 'academique'));
      this.personnels.set(p.filter((x) => x.type === 'personnel'));
    });
  }

  openDetail(project: Project): void {
    this.selectedProject.set(project);
  }

  closeDetail(): void {
    this.selectedProject.set(null);
  }

  getProjectImageUrl(project: Project): string | null {
    return project.image_url || null;
  }
}
