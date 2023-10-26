

from flask_restful import  reqparse

student_parser = reqparse.RequestParser()

student_parser.add_argument('name', type=str,required=True,
                            help='Student is required')

student_parser.add_argument('image', type=str)
student_parser.add_argument('dept_id', type=int)