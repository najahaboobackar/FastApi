from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:najah123@localhost:3030/Person",echo=True)

Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)#binding