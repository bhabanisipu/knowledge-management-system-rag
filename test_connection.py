import traceback
from sqlalchemy import text

from app.database.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ MySQL Connected Successfully!")
        print(result.scalar())
except Exception as e:
    print("❌ Connection Failed")
    print(type(e).__name__, e)
    traceback.print_exc()