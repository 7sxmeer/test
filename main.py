from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# Database configuration
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "mydb"
DB_HOST = "104.198.132.85"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on GCP!"}

@app.get("/test-db")
def test_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 'Hello from PostgreSQL';")).fetchone()
        return {"db_response": result[0]}
