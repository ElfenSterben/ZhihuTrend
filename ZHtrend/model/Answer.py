from . import *
from datetime import datetime

class Answer(Model):
    __tablename__ = 'answer'

    def __init__(self, form):
        self.question_id = form.get('question_id')
        self.answer_id = form.get('answer_id')
        self.title = form.get('title')
        self.total = form.get('total')
        self.approve = form.get('approve')
        self.content = form.get('content')
        self.post_time = form.get('post_time')
        self.edit_time = form.get('edit_time')
        self.comment = form.get('comment')
        self.user_id = form.get('user_id')

    @classmethod
    def get_today_question_ids(cls):
        return cls.query.find({'post_time': datetime.now().strftime('%Y-%m-%d')}).distinct('question_id')

    @classmethod
    def get_answers_by_question_id(cls, question_id):
        filter_dict = {
            'post_time': datetime.now().strftime('%Y-%m-%d'),
            'question_id': question_id,
        }
        return cls.query.find(filter_dict)