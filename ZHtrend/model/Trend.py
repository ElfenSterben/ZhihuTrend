from . import *

class Trend(Model):
    __tablename__ = 'trend'

    def __init__(self, form):
        self.question_id = form.get('question_id')
        self.rank = form.get('rank')