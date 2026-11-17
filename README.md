# AI Travel Planner

An AI-powered travel planner that generates personalized trip itineraries.
Users describe their destination, dates, and preferences; the app uses
Google Gemini to build a day-by-day plan, enriches it with real places from
Geoapify, and displays everything on an interactive MapLibre map.

> **Status:** Early setup. The application code has not been scaffolded yet.

## Tech Stack

| Layer          | Technology                     |
| -------------- | ------------------------------ |
| Frontend       | Next.js, TypeScript            |
| Backend        | Python, FastAPI                |
| AI             | Google Gemini API              |
| Database       | Supabase (PostgreSQL)          |
| Maps & Places  | Geoapify (places), MapLibre GL |

## Repository Structure

```
ai-travel-planner/
├── apps/
│   ├── web/          # Next.js + TypeScript frontend
│   └── api/          # Python + FastAPI backend
├── .gitignore
└── README.md
```

## Getting Started

Setup instructions will be added once the frontend and backend are scaffolded.
