from . import *

class User(Model):
    __tablename__ =  'user'

    def __init__(self, form):
        self.name = form.get('name')
        self.id = form.get('id')
        self.description = form.get('description')
        self.profession = form.get('profession')
        self.sex = form.get('sex')
        self.answer = form.get('answer')
        self.share = form.get('share')
        self.question = form.get('question')
        self.collection = form.get('collection')
        self.receive_up_prove = form.get('receive_up_prove')
        self.receive_thank = form.get('receive_thank')
        self.receive_collect = form.get('receive_collect')
        self.follower = form.get('follower')
        self.following = form.get('following')
        self.sponsor_live = form.get('spsons_or_live')
        self.interest_topic = form.get('interest_topic')
        self.interest_column = form.get('interest_column')
        self.interest_question = form.get('interest_question')
        self.interest_collection = form.get('interest_collection')
