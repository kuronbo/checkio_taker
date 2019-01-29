from checkio_taker.model import Problem, Answer
from checkio_taker.persistence.sql_alchemy import config
from checkio_taker.persistence.interface import ProblemRepository


class AlcProblemRepository(ProblemRepository):
    def __init__(self):
        self.session = config.Session()

    def get(self, id):
        session = self.session
        response = session.query(config.Problem).\
            filter(config.Problem.id==id).\
            first()
        if response:
            return Problem(response.id, response.island, response.title,
                           response.level, response.description,
                           [Answer(a.id, a.who, a.source_code, a.impression)
                            for a in response.answers], response.updated_at)

    def save(self, problem, update=False):
        session = self.session
        if not update:
            p_db = config.Problem(id=problem.id,
                                  island=problem.island,
                                  title=problem.title,
                                  level=problem.level,
                                  description=problem.description,
                                  updated_at=problem.updated_at)
            a_dbs = [config.Answer(id=a.id, who=a.who, source_code=a.source_code,
                                   impression=a.impression)
                     for a in problem.answers.values()]
            p_db.answers = a_dbs
            session.add(p_db)
            session.flush()
        else:
            p_db = session.query(config.Problem).filter_by(id=problem.id).first()
            for para in ['island', 'title', 'level', 'description', 'updated_at']:
                setattr(p_db, para, getattr(problem, para))
            p_db.answers = []
            p_db.answers = [config.Answer(id=a.id, who=a.who, source_code=a.source_code,
                                          impression=a.impression)
                            for a in problem.answers.values()]
            session.flush()

    def commit(self):
        self.session.commit()


if __name__ == '__main__':
    config.load_engine(':memory:')
    alc = AlcProblemRepository()
    p = Problem.new('island', 'title', 0, 'aaa')
    p.add_answer('watashi', 'from im import *', 'impression')
    alc.save(p)
    p.add_answer('peenuts', 'from im import *', 'impression')
    alc.save(p, update=True)
    print(alc.get(p.id))
