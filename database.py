from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
Host: sql10.freesqldatabase.com
Database name: sql10440052
Database user: sql10440052
Database password: ZuiKu3Q3Vp
Port number: 3306
'''

DATABASE_URL = "mysql+mysqlconnector://sql10440052:ZuiKu3Q3Vp@sql10.freesqldatabase.com:3306/sql10440052"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()