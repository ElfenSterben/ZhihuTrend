from . import *

class User(Model):
    __tablename__ =  'user'

    def __init__(self, form):
        self.name = form.get('name')
        self.id = form.get('id')
        self.description = form.get('description')
        self.profession = form.get('profession')
        self.sex = form.get('sex')
        self.answer = int(form.get('answer'))
        self.share = int(form.get('share'))
        self.question = int(form.get('question'))
        self.collection = int(form.get('collection'))
        self.receive_up_prove = int(form.get('receive_up_prove'))
        self.receive_thank = int(form.get('receive_thank'))
        self.receive_collect = int(form.get('receive_collect'))
        self.follower = int(form.get('follower')) # 关注者
        self.following = int(form.get('following')) # 关注了
        self.sponsor_live = int(form.get('sponsor_live'))
        self.interest_topic = int(form.get('interest_topic'))
        self.interest_column = int(form.get('interest_column'))
        self.interest_question = int(form.get('interest_question'))
        self.interest_collection = int(form.get('interest_collection'))

    @classmethod
    def find_user_by_id(cls, id):
        filter_dict = {
            'id': id,
        }
        return cls.query.find_one(filter_dict)

    @classmethod
    def get_activity_user(cls):
        filter_dict = {
            'follower': {'$gt': 800},
            'receive_thank': {'$gt': 4000}
        }
        return cls.query.find(filter_dict)

    @classmethod
    def get_user_ids(cls):
        return cls.query.distinct('id')

    @classmethod
    def get_rank_by_answers(cls, answers):
        rank = 0
        for answer in answers:
            rank += cls.find_user_by_id(answer.get('id')).get('follower', 0)

        return rank

    @classmethod
    def all(cls):
        cls.query.find()