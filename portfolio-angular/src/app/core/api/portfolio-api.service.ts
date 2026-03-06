import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, catchError, of } from 'rxjs';
import { API_BASE_URL } from './api-config';

export interface Profile {
  id: number;
  full_name: string;
  first_name: string;
  last_name: string;
  headline: string;
  bio_lead: string;
  bio_paragraph: string;
  personality?: string;
  email: string;
  phone: string;
  photo: string | null;
  photo_url: string | null;
  cv_url: string | null;
  linkedin_url: string;
  github_url: string;
}

export interface Education {
  id: number;
  period: string;
  title: string;
  place: string;
}

export interface Experience {
  id: number;
  title: string;
  description: string;
}

export interface Skill {
  id: number;
  name: string;
}

export interface Interest {
  id: number;
  title: string;
  subtitle: string;
  icon: string;
}

export interface Project {
  id: number;
  title: string;
  short_desc: string;
  full_desc: string;
  tech: string;
  image: string | null;
  image_url: string | null;
  type: 'academique' | 'personnel';
}

export interface Fact {
  id: number;
  number: number;
  suffix: string;
  label: string;
  icon: string;
}

export interface ContactForm {
  name: string;
  email: string;
  subject: string;
  message: string;
}

@Injectable({ providedIn: 'root' })
export class PortfolioApiService {
  private readonly http = inject(HttpClient);
  private readonly base = API_BASE_URL;

  getProfile(): Observable<Profile | null> {
    return this.http.get<Profile>(`${this.base}/profile/`).pipe(
      catchError(() => of(null))
    );
  }

  private extractList<T>(r: unknown): T[] {
    if (Array.isArray(r)) return r;
    if (r && typeof r === 'object' && 'results' in r && Array.isArray((r as { results: T[] }).results)) {
      return (r as { results: T[] }).results;
    }
    return [];
  }

  getEducation(): Observable<Education[]> {
    return this.http.get<unknown>(`${this.base}/education/`).pipe(
      map((r) => this.extractList<Education>(r)),
      catchError(() => of([]))
    );
  }

  getExperience(): Observable<Experience[]> {
    return this.http.get<unknown>(`${this.base}/experience/`).pipe(
      map((r) => this.extractList<Experience>(r)),
      catchError(() => of([]))
    );
  }

  getSkills(): Observable<Skill[]> {
    return this.http.get<unknown>(`${this.base}/skills/`).pipe(
      map((r) => this.extractList<Skill>(r)),
      catchError(() => of([]))
    );
  }

  getInterests(): Observable<Interest[]> {
    return this.http.get<unknown>(`${this.base}/interests/`).pipe(
      map((r) => this.extractList<Interest>(r)),
      catchError(() => of([]))
    );
  }

  getProjects(type?: 'academique' | 'personnel'): Observable<Project[]> {
    let url = `${this.base}/projects/`;
    if (type) {
      url += `?type=${type}`;
    }
    return this.http.get<unknown>(url).pipe(
      map((r) => this.extractList<Project>(r)),
      catchError(() => of([]))
    );
  }

  getFacts(): Observable<Fact[]> {
    return this.http.get<unknown>(`${this.base}/facts/`).pipe(
      map((r) => this.extractList<Fact>(r)),
      catchError(() => of([]))
    );
  }

  sendContact(form: ContactForm): Observable<{ message: string }> {
    return this.http.post<{ message: string }>(`${this.base}/contact/`, form);
  }
}
