from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config.settings import settings


DATABASE_URL = (
    f"mysql+pymysql://{quote_plus(settings.MYSQL_USER)}:"
    f"{quote_plus(settings.MYSQL_PASSWORD)}@"
    f"{settings.MYSQL_HOST}:"
    f"{settings.MYSQL_PORT}/"
    f"{settings.MYSQL_DATABASE}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()