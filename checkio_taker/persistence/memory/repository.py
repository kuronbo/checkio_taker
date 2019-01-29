from checkio_taker.persistence.interface import ProblemRepository
from checkio_taker.persistence.memory import config


class MemoryProblemRepository(ProblemRepository):
    def __init__(self):
        self.storage = config.MEMORY_STORAGE
        self.cache = None

    def get(self, id):
        return self.storage.get(id)

    def save(self, problem, update=False):
        if not update and problem.id in self.storage:
            raise ValueError('既に`problem`が存在します。id={}'.format(problem.id))
        if update and problem.id not in self.storage:
            raise ValueError('`problem`が存在しません。id={}'.format(problem.id))
        self.cache = problem

    def commit(self):
        problem = self.cache
        self.storage[problem.id] = problem
        self.cache = None
