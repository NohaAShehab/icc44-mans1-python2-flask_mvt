
from flask_restful import  Resource, marshal_with
from app.models import  Track

from app.tracks.serializers import track_serailizer
from app.tracks.parsers import  track_parser
# need to serialize the object ?


class TrackListResource(Resource):
    @marshal_with(track_serailizer)
    def get(self):
        tracks = Track.get_all_objects()
        return tracks, 200

    @marshal_with(track_serailizer)
    def post(self):
        track_data= track_parser.parse_args()
        track = Track.save_track(track_data)
        return track, 201


