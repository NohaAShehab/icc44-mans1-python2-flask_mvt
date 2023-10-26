

from flask_restful import reqparse

track_parser =reqparse.RequestParser()
track_parser.add_argument('name', 'str', help='This field is required', required=True)

