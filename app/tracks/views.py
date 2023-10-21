from flask import render_template, request, url_for, redirect
from app.tracks import track_blueprint
from app.models import  Track

def tracks_index():
    return "<h1 style='color:red; '>  Tracks Index</h1>"


# connect blueprint with the view function
@track_blueprint.route('hello', endpoint='tracks_hello')
def hellotrack():
    return "<h1 style='color:green'> Hello Track </h1>"



@track_blueprint.route('/index', endpoint='list')
def index():
    tracks  = Track.get_all_objects()
    return render_template('tracks/index.html', tracks= tracks)


@track_blueprint.route('/create', endpoint='create',methods = ['GET', 'POST'])
def create():
    if request.method=='POST':
        track = Track.save_track(request.form)
        return redirect(url_for('tracks.list'))

    return render_template('tracks/create.html')