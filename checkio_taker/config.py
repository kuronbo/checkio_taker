from checkio_taker.persistence.sql_alchemy.repository import AlcProblemRepository
from checkio_taker.persistence.sql_alchemy.config import load_engine


PROBLEM_REPO = None


def configure(path):
    global PROBLEM_REPO
    load_engine(path)
    PROBLEM_REPO = AlcProblemRepository()
