
# connect blueprint with views
from app.students import student_blueprint
@student_blueprint.route('hello')
def helloworld():
    return '<h1> Hello world'

