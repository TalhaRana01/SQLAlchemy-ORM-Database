from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from database import engine
from sqlalchemy import String

class Base(DeclarativeBase):
  pass


# User Model /User Table

class User(Base):
  __tablename__= "users"
  
  
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(100), nullable=False)
  email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
  
  
  def __repr__(self) -> str:
    return f"<User(id{self.id}, name={self.name}, email={self.email})>"
  
  
  # Create table
  

def create_tables():
    Base.metadata.create_all(engine)