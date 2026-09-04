# Insurance Quote API

A small Flask-based API that simulates insurance quote calculations, built to practice a full DevOps workflow: containerization, automated testing, CI/CD, and audit logging.

## Features
- REST API endpoint to calculate mock insurance quotes based on age and coverage type
- Audit logging of every quote request (timestamp, inputs, result)
- Automated unit tests covering pricing logic
- Dockerized for consistent deployment
- CI/CD pipeline (GitHub Actions): runs tests → builds Docker image → verifies the container responds correctly

## Tech Stack
- Python / Flask
- Pytest
- Docker
- GitHub Actions

## Endpoints
- `GET /quote?age=<int>&coverage=<basic|standard|premium>` — returns a calculated quote
- `GET /health` — health check endpoint

## Running locally
\`\`\`bash
pip install -r requirements.txt
python app.py
\`\`\`

## Running with Docker
\`\`\`bash
docker build -t insurance-quote-api .
docker run -d -p 5000:5000 insurance-quote-api
\`\`\`

## Running tests
\`\`\`bash
pytest
\`\`\`

## Why this project
Built to demonstrate a realistic, compliance-aware DevOps workflow — including audit trails, which matter in regulated industries like insurance and finance.
