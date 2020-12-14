from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from ..db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), default = datetime.utcnow, nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), default = datetime.utcnow, nullable=False, server_default=func.now())
    # group_id = Column(Integer, ForeignKey("groups.id"))

    # group = relationship("Group", back_populates="users")
    items = relationship("Item", back_populates="owner")