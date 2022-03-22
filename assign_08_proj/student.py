from settings import *
import json

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # birthday: year - 4 digit
    birthday = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'birthday': self.birthday, 'sex': self.sex}

    def add_student(_name, _birthday, _sex):
        new_student = Student(name=_name, birthday=_birthday, sex=_sex)
        db.session.add(new_student)
        db.session.commit()

    def get_all_students():
        return [Student.json(student) for student in Student.query.all()]

    def get_student(_id):
        return [Student.json(Student.query.filter_by(id=_id).first())]

    def update_student(_id, _name, _birthday, _sex):
        student_to_update = Student.query.filter_by(id=_id).first()
        student_to_update.name = _name
        student_to_update.birthday = _birthday
        student_to_update.sex = _sex
        db.session.commit()

    def delete_student(_id):
        Student.query.filter_by(id=_id).delete()
        db.session.commit()