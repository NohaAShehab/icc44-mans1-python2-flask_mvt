
from flask_sqlalchemy import SQLAlchemy
from flask import  url_for

db = SQLAlchemy()



class Track(db.Model):
    __tablename__='tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime,server_onupdate=db.func.now(), server_default=db.func.now())
    students= db.relationship('Student', backref='track_name', lazy=True)


    def __str__(self):
        return f"{self.name}"
    @classmethod
    def get_all_objects(cls):
        return  cls.query.all()

    @classmethod
    def save_track(cls, request_data):
        track  =cls(**request_data)
        db.session.add(track)
        db.session.commit()
        return track

# here where I will create the models

class Student(db.Model):
    __tablename__='students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    track = db.Column(db.String)
    dept_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=True)

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

    @classmethod
    def get_specific_student(cls, id):
        return  cls.query.get_or_404(id)

    @property
    def get_image_url(self):
        return url_for('static', filename=f'students/images/{self.image}')

    @property
    def get_show_url(self):
        return  url_for('students.show', id=self.id)

    # @property
    # def get_delete_url(self):
    #     return  url_for('students.delete', id= self.id)


