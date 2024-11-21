from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import Session, declarative_base
import random


engine=create_engine('postgresql+psycopg2://postgres:12345@localhost/postgres')

meta=MetaData()


Base=declarative_base()


class YaProject(Base):
    __tablename__='ya_projects'
    id=Column(Integer, primary_key=True)
    col1=Column(Integer, primary_key=False)
    col2=Column(Integer, primary_key=False)
    col3=Column(Integer, primary_key=False)
    col4=Column(Integer, primary_key=False)
    col5=Column(Integer, primary_key=False)

def fill_ya_projects(engine):
    session=Session(bind=engine)

    for i in range(100):
        values=random.sample(range(0, 99999), 5)
        session.add_all(
            [
                YaProject(
                    col1=values[0],
                    col2=values[1],
                    col3=values[2],
                    col4=values[3],
                    col5=values[4],
                )
                for i in range(5)
            ]
        )
        session.flush()
    session.commit()


def init_db():
    with engine.connect() as conn:
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        fill_ya_projects(engine)

if __name__=='__main__':
    init_db()