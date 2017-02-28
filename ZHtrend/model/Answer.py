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

    def get_today_answers(self):
        return list(self.query.find({'post_time': datetime.now().strftime('%Y-%m-%d')}))