from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.config import Config
from sqlalchemy import URL

# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False}
# )

# load env values
config = Config(".env")
_user = config("DB_USER", cast=str)
_password = config("DB_PASSWORD", cast=str)
_host = config("DB_HOST", cast=str)
_database = config("DB_NAME", cast=str)
_port = config("DB_PORT", cast=int, default=3306)

url_object = URL.create(
    "mysql",
    username=_user,
    password=_password,
    host=_host,
    database=_database,
    port=_port
)
engine = create_engine(url_object)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
