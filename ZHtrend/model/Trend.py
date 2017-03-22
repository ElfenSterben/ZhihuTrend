from . import *
from datetime import datetime

class Trend(Model):
    __tablename__ = 'trend_temp'

    def __init__(self, form):
        self.question_id = form.get('question_id')
        self.rank = form.get('rank')

    @classmethod
    def drop_table(cls):
        cls.query.drop()

    @classmethod
    def create_today_trend(cls, all_rank):
        today = datetime.now().strftime('%Y-%m-%d')
        cls.drop_table()
        cls.save_all(all_rank)
        cls.__tablename__ = 'trend_' + today
        cls.query.rename('trend_old')
        cls.__tablename__ = 'trend_temp'
        cls.query.rename('trend_' + today)
        cls.__tablename__ = 'trend_old'
        cls.drop_table()
