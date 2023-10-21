
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class Track(db.Model):
    __tablename__='tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime,server_onupdate=db.func.now(), server_default=db.func.now())

# here where I will create the models

class Student(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    track = db.Column(db.String)

    @classmethod
    def get_all_objects(cls):
        return cls.query.all()

    def save_student(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def create_student(cls, request_form):
        std = cls(**request_form)
        db.session.add(std)
        db.session.commit()
        return std

    # @property
    # def get_image_url(self):
    #     return url_for('static', filename=f'students/images/{self.image}')
    #
    # @property
    # def get_show_url(self):
    #     return  url_for('students.show', id=self.id)
    #
    # @property
    # def get_delete_url(self):
    #     return  url_for('students.delete', id= self.id)


