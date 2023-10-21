def tracks_index():
    return "<h1 style='color:red; '>  Tracks Index</h1>"


from app.tracks import track_blueprint


# connect blueprint with the view function
@track_blueprint.route('hello', endpoint='tracks_hello')
def hellotrack():
    return "<h1 style='color:green'> Hello Track </h1>"
