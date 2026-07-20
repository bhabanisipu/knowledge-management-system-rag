from app.database.database import Base, engine

# Import all models here
from app.models.user import User
from app.models.document import Document

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")