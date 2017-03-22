from . import *

class Frequency(Model):
    __tablename__ = 'frequency'

    @classmethod
    def save_tags(cls, tags):
        forms = []
        for tag in tags:
            data = {}
            data['frequency'] = tag[0]
            data['world'] = tag[1]
            forms.append(data)
        cls.save_all(forms)