from flask_restful import Resource, fields, marshal_with, abort
from flask import  make_response
from app.models import Student, Track, db
from app.students.parser import  student_parser

## api --> receive data from form


## seriliaze data

track_serlizer= {
    "id": fields.Integer,
    "name": fields.String
}
student_serializer= {
    "id": fields.Integer,
    'name':fields.String,
    "dept_id": fields.Integer,
    'track_name': fields.Nested(track_serlizer)
}


## crud operations

class StudentList(Resource):
    @marshal_with(student_serializer)
    def get(self):
        students = Student.get_all_objects()
        return students,200

    @marshal_with(student_serializer)
    def post(self):
        # pass
        # get data from form >
        # parsing form data --> x-application
        student_args = student_parser.parse_args()
        print(student_args) # dict ---> parsing
        student = Student.create_student(student_args)
        return student, 201



        ## saving , return with result



class StudentResource(Resource):
    @marshal_with(student_serializer)
    def get(self, std_id):
        student = Student.get_specific_student(std_id)
        return student, 200

    @marshal_with(student_serializer)
    def put(self, std_id):
        student = Student.get_specific_student(std_id)
        if student:
            std_args = student_parser.parse_args()
            student.name= std_args['name']
            student.image = std_args['image']
            student.dept_id=  std_args['dept_id']
            db.session.add(student)
            db.session.commit()

            return  student, 200

        abort(404, message='Student object not found')

    def delete(self, std_id):
        student = Student.get_specific_student(std_id)
        if student:
            db.session.delete(student)
            db.session.commit()
            response = make_response("deleted", 204)
            return  response

        abort(404)

