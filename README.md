# Offer Manager

Full-stack application for managing affiliate marketing offers with custom payout configurations for individual influencers.

**Live Demo:** https://offer-manager-frontend.onrender.com/

## Tech Stack

**Backend**

- FastAPI
- SQLModel
- SQLite
- Pydantic Settings

**Frontend**

- React 19
- TypeScript
- Vite
- Tailwind CSS v4
- Motion

`client.ts` is auto-generated using [Swagger TypeScript API](https://github.com/acacode/swagger-typescript-api)

## Running locally

**Backend**

```bash
git clone https://github.com/mikke555/offer-manager.git
cd backend

# create and activate virtual environment

# Windows
python -m venv .venv
.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

# install dependecies
pip install -r requirements.txt

# run the app
fastapi dev
```

**Frontend**

```bash
cd frontend
npm install
npm run dev
```

**Backend tests**

```bash
cd backend
pytest
```

## Configuration

Backend runs on `localhost:8000`, frontend on `localhost:5173`.

To adjust these ports, rename `.env.example` to `.env` in respective directories.

**backend/.env**

```
CORS_ORIGINS="http://localhost:5173"
```

**frontend/.env**

```
VITE_API_BASE_URL="http://localhost:8000"
```

## How to use

API documentation is available at `localhost:8000/docs`.

On the initial run, the database is populated with dummy data.

There is no authentication. To view offers with custom payouts, provide
influencer_id as a query parameter, for example:
`http://localhost:5173/?influencer_id=1`.

If no query parameter is provided, the public view is displayed.
