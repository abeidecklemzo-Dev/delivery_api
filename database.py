from sqlmodel import SQLModel , Session ,create_engine
DATABASE_URL="sqlite:///./database.db"
engine=create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)
def get_db():
    with Session(engine) as session :
        yield session

