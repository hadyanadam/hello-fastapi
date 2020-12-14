import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path('.').resolve()
load_dotenv(BASE_DIR / 'app' / '.env')
print(BASE_DIR)
DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
print(DATABASE_URI)