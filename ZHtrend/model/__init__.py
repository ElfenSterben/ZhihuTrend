import pymongo

conn = pymongo.MongoClient('127.0.0.1', 18888)
db_zhtrend = conn.zhtrend
conn.authenticate('test', 'test')

class Model(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    @property
    def query(self):
        return self.get_collection()

    @classmethod
    def get_collection(cls):
        cn = cls.__tablename__
        col = db_zhtrend[cn]
        return col

    def save(self):
        col = self.get_collection()
        col.insert(self.__dict__)

    @classmethod
    def delete(cls, forms):
        col = cls.get_collection()
        col.remove(forms)

    @classmethod
    def _update(cls, old, new):
        col = cls.get_collection()
        col.update(old, {'$set': new})




if __name__ == '__main__':
    pass
