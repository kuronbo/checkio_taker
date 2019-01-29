from checkio_taker.persistence.memory import config


class MemoryProblemGetter:
    def by_id(self, id):
        storage = config.MEMORY_STORAGE
        return storage.get(id)
