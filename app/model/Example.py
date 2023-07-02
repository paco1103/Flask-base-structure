from . import db


class Example(db.Model):

    __tablename__ = 'example'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    field1 = db.Column(db.VARCHAR(255))


    def __init__(self, field1=None):
        super().__init__()
        self.field1 = field1

    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_by_id(self, id):
        return Example.query.filter(Example.id == id).first()

    def delete_by_id(self, id):
        # 0 = not found, 1 = deleted
        result = Example.query.filter(Example.id == id).delete()
        db.session.commit()
        return result
