from flask_restful import Resource
from flask import request
from model.observation import Observation
from database import db

class ObservationsEndpoint(Resource):
    def get(self):
        observations_list = db.session.execute(db.select(Observation)).scalars()
        return [o.serialize() for o in observations_list], 200

    def post(self):
        data = request.json
        obeservation = Observation(
            sensor_id=data["sensor_id"],
            feature_id=data["feature_id"],
            timestamp=data["timestamp"],
            value=data["value"]
        )
        db.session.add(obeservation)
        db.session.commit()
        return obeservation.serialize(), 201

