from itertools import chain

from datetime import datetime
from uuid import uuid4


class Problem:
    def __init__(self, id, island, title, level, description, answers, updated_at):
        self.id = id
        self.island = island
        self.title = title
        self.level = level
        self.description = description
        self.answers = {answer.id: answer for answer in answers}
        self.updated_at = updated_at

    @classmethod
    def new(cls, island, title, level, description):
        id = str(uuid4())[:8]
        updated_at = datetime.now()
        return cls(id, island, title, level, description, [], updated_at)

    def add_answer(self, who, source_code, impression):
        max_num = str(max(int(i[9:]) for i in chain(self.answers, ['12345678_0'])))
        new_id = self.id + '_' + str(int(max_num)+1)
        self.answers[new_id] = Answer(str(new_id), who, source_code, impression)
        return self.answers[str(new_id)]

    def rm_answer(self, answer_id):
        self.answers.pop(answer_id)

    def to_dict(self):
        return {
            'id': self.id,
            'island': self.island,
            'title': self.title,
            'level': self.level,
            'description': self.description,
            'answers': {k: v.to_dict() for k, v in self.answers.items()},
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return 'Problem(id={self.id!r}, island={self.island!r},' \
               'title={self.title!r}, level={self.level},' \
               'description={self.description!r},' \
               'answers={answers!r}, updated_at={self.updated_at!r})'.\
            format(self=self, answers=self.answers.items())


class Answer:
    def __init__(self, id, who, source_code, impression):
        self.id = id
        self.who = who
        self.source_code = source_code
        self.impression = impression

    def to_dict(self):
        return {
            'id': self.id,
            'who': self.who,
            'source_code': self.source_code,
            'impression': self.impression,
        }

    def __repr__(self):
        return 'Answer(who={self.who!r}, source_code={self.source_code!r},' \
               'impression={self.impression!r})'.\
            format(self=self)
