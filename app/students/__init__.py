
from flask import  Blueprint
student_blueprint= Blueprint('students', __name__, url_prefix='/students')
from app.students import views