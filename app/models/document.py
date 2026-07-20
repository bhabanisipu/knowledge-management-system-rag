from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255), nullable=False)

    filepath = Column(String(500), nullable=False)

    file_type = Column(String(20), nullable=False)

    file_size = Column(Integer, nullable=False)

    status = Column(String(50), default="Uploaded")

    uploaded_by = Column(Integer, ForeignKey("users.id"))

    upload_date = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship with User
    user = relationship("User", back_populates="documents")