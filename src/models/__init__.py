from sqlalchemy import ForeignKey, Column, Integer, String, Float, Text, VARCHAR
from sqlalchemy.orm import relationship
from src.database import Base


class Players(Base):
    __tablename__ = "players"

    uid = Column(VARCHAR(255), primary_key=True, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    icon = Column(VARCHAR(255), nullable=False)
