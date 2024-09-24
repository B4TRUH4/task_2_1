from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base
from .config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)
Session = sessionmaker(bind=engine)


def get_session():
    return Session()


def prepare_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    prepare_database()
