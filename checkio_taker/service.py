from checkio_taker import config
from checkio_taker.exception import ValueCheckIOError
from checkio_taker.model import Problem


def need_kwargs(kwargs, need_paras):
    for para in need_paras:
        if para not in kwargs:
            raise ValueCheckIOError


class CommandService:
    def flush(self):
        """commandが成功するかどうか確認"""
        raise NotImplementedError

    def commit(self):
        """commandを適用する"""
        raise NotImplementedError


class ProblemOperator(CommandService):
    def __init__(self):
        self.problem = None
        self.is_new = False
        self.repository = config.PROBLEM_REPO

    def is_loaded(self):
        """ロードされているかどうか"""
        return bool(self.problem)

    def load(self, id):
        """指定のidの`Problem`をロード"""
        self.problem = self.repository.get(id)
        self.is_new = False

    def property(self):
        return self.problem.to_dict()

    def new(self, **kwargs):
        """新しい`Problem`を作成する。

        Arguments:
            island (str): islandの名前
            title (str): `Problem`のタイトル
            level (int): `Problem`のレベル(0-3)
            description (str): `Problem`の説明文
        """
        need_paras = ['island', 'title', 'level', 'description']
        need_kwargs(kwargs, need_paras)
        self.problem = Problem.new(**{name:kwargs[name] for name in need_paras})
        self.is_new = True

    def answer(self, answer_id):
        """該当の`Answer`を返す

        Arguments:
            answer_id (str): answerのid

        Returns:
            Answer or None: `Answer`インスタンス or None
        """
        return self.problem.answers.get(answer_id)

    def add_answer(self, **kwargs):
        """新しい`Answer`を追加する

        Arguments:
            who (str): 解答者
            source_code (str): ソースコード
            impression (str): 思うこと
        """
        need_paras = ['who', 'source_code', 'impression']
        need_kwargs(kwargs, need_paras)
        return self.problem.add_answer(*[kwargs[name] for name in need_paras])

    def flush(self):
        self.repository.save(self.problem, update=not self.is_new)

    def commit(self):
        self.repository.commit()


class Request:
    def by_id(self, id):
        r = config.PROBLEM_REPO.get(id)
        return r.to_dict() if r else {}
