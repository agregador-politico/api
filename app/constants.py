import os

# Database
DATABASE_URL = os.getenv("DATABASE_URL") or "mongodb://mongodb:27017"
DATABASE_NAME = os.getenv("DATABASE_NAME") or "agregador-database"
DATABASE_USER = os.getenv("DATABASE_USER") or "root"
DATABASE_PASS = os.getenv("DATABASE_PASS ") or "agregador"
## Collections
FORMS = "forms"
QUESTIONS = "questions"
ACCESS = "ACCESS"
