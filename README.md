# Facebook Page Manager & Multimodal AI Agent

This repository is a professional starter for a high-end Facebook Page management system with an advanced multimodal AI layer. It is designed as a production-oriented foundation for:

- Facebook / Meta Page publishing and automation
- AI-assisted conversation and content generation
- File and image extraction (text OCR, docs, PDFs)
- Dashboard for page operations and automation
- Multi-page and multi-channel management

Important notes:
- This repository is a strong engineering foundation and operational MVP, not a literal AGI.
- To use Meta APIs you still need valid page access tokens and developer app configuration from Meta.
- The AI features are designed to be extensible for LLM providers, OCR, embeddings, and workflow orchestration.

## Architecture

- Backend: FastAPI (Python)
- Frontend: lightweight static dashboard served by FastAPI
- Data layer: SQLite starter (easy local development)
- AI services: pluggable LLM and OCR adapters
- Meta client: Graph API wrapper for page publish/read operations

## Quick start

1. Create a Python virtual environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set environment variables
   ```bash
   cp ../.env.example ../.env
   ```

4. Run the app
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

5. Open the dashboard
   ```text
   http://localhost:8000
   ```

## Included capabilities

- AI agent chat endpoint
- File upload endpoint for docs/images
- OCR text extraction pipeline for images and PDFs
- Facebook page content publish scaffold
- Dashboard UI for campaign operations
- API contracts for future enterprise features

## Folder structure

```text
.
├── .env.example
├── .gitignore
├── README.md
├── docker-compose.yml
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── health.py
│   │   │   ├── agent.py
│   │   │   └── pages.py
│   │   └── services/
│   │       ├── ai_agent.py
│   │       ├── file_extractor.py
│   │       └── meta_client.py
│   └── requirements.txt
├── frontend/
│   ├── app.js
│   ├── index.html
│   └── styles.css
└── docs/
    └── architecture.md
```

## Next phases to expand

- Add persistent SQLAlchemy models
- Add user auth and role-based access control
- Integrate OpenAI / Azure OpenAI / Claude / Groq / local LLM
- Add vector search and memory storage
- Add automation rules and triggers
- Add scheduled content planner
- Add robust OCR pipeline with Tesseract and EasyOCR
- Add background jobs for publishing and analytics

## Meta requirements

To enable publishing through Meta:
- Create a Meta app in Meta for Developers
- Generate a Page Access Token
- Add your page ID and token to `.env`
- Ensure permissions like `pages_manage_posts`, `pages_read_engagement`, `pages_manage_engagement`, or relevant scopes are granted

## License

This project is set up as a starter foundation for enterprise automation and internal tooling.
