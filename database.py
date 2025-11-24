from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE = "sqlite:///sqlite.db"
engine = create_engine(DATABASE, echo=True)


SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)