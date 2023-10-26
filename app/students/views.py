from flask import  request,render_template, redirect, url_for
from app.models import Student, db
# connect blueprint with views
from app.students import student_blueprint
from app.models import Track
from app.students.forms import StudentForm
@student_blueprint.route('hello')
def helloworld():
    return '<h1> Hello world'

@student_blueprint.route('', endpoint='students_index')
def index():
    students = Student.get_all_objects()
    return render_template('students/index.html', students=students)


@student_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'] )
def create():
    if request.method=='POST':
        print("request received", request.form)
        # student = Student(name=request.form['name'], track=request.form['track'],
        #                   image=request.form['image'])
        # # db.session.add(student)
        # # db.session.commit()
        # student.save_student()
        # return request.form
        # # return request.form
        student = Student.create_student(request.form)
        return redirect(url_for('students.students_index'))

    tracks = Track.get_all_objects()
    return render_template('students/create.html', tracks=tracks)


@student_blueprint.route('<int:id>', endpoint='show')
def show(id):
    student = Student.get_specific_student(id)
    return  render_template('students/show.html', student=student)



## check errors
def validate_inputs(request):
    errors = {}
    if 'csrf_token' not in request.keys():
        return  419
    if not request['name']:
        errors['name']= 'Name is required'

    return  errors

# @student_blueprint.route('forms/create', endpoint='forms_create', methods = ['GET', "POST"])
# def create_form():
#     form = StudentForm()
#     if request.method=='GET':
#         return render_template('students/create_form.html', form=form)
#     elif  request.method=='POST':
#         # get data from form .
#         data= dict(request.form)
#         errors = validate_inputs(data)
#         if errors:
#             return render_template('students/create_form.html', form=form, errors=errors)
#         del data['csrf_token']
#         student = Student.create_student(data)
#         return redirect(url_for('students.students_index'))



# @student_blueprint.route('forms/create', endpoint='forms_create', methods = ['GET', "POST"])
# def create_form():
#     form = StudentForm(request.form)
#
#     if  request.method=='POST' and form.validate():
#         # get data from form .
#         data= dict(request.form)
#         del data['csrf_token']
#         student = Student.create_student(data)
#         return redirect(url_for('students.students_index'))
#
#     return  render_template('students/create_form.html', form=form)


from app.students.forms import  StudentModelForm
@student_blueprint.route('forms/create', endpoint='forms_create', methods = ['GET', "POST"])
def create_form():
    form = StudentForm(request.form)

    if  request.method=='POST' and form.validate():
        # get data from form .
        data= dict(request.form)
        del data['csrf_token']
        student = Student.create_student(data)
        return redirect(url_for('students.students_index'))

    return  render_template('students/create_form.html', form=form)


# generate apis