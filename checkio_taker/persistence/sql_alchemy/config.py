from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
ENGINE = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=ENGINE)


def load_engine(file_path):
    global ENGINE
    global Session
    ENGINE = create_engine('sqlite:///{}'.format(file_path),
                           connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=ENGINE)
    Base.metadata.create_all(bind=ENGINE)



class Problem(Base):
    __tablename__ = 'problem'

    id = Column(String, primary_key=True)
    island = Column(String)
    title = Column(String)
    level = Column(Integer)
    description = Column(String)
    answers = relationship('Answer',
                           cascade="save-update, merge, delete, delete-orphan")
    updated_at = Column(DateTime)


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(String, primary_key=True)
    who = Column(String)
    source_code = Column(String)
    impression = Column(String)
    problem_id = Column(String, ForeignKey('problem.id'))


if __name__ == '__main__':
    Base.metadata.create_all(bind=ENGINE)
    session = create_session()
    print(session.query(Problem).all())
