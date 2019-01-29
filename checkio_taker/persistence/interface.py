class ProblemRepository:
    def get(self, id):
        raise NotImplementedError

    def save(self, problem, update=False):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError
