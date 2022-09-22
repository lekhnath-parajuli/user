from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from sqlalchemy_utils import database_exists, create_database
from models.user import Base
from models.user import User
from config import config


DATABASE_URL = config.DATABASE_URL
if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


class UserController:
   async def register(self, firstname: str, lastname: str) -> int:
        user = User(firstname=firstname, lastname=lastname)
        with Session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user.uid


