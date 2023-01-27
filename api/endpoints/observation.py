from flask_restful import Resource
from flask import request
from model.observation import Observation
from database import db
import datetime


class ObservationsEndpoint(Resource):
    def get(self):
        DEFAULT_START = str(datetime.datetime.min)  # format: YYYY-MM-DD hh:mm:ss.mmmmmm
        DEFAULT_END = str(datetime.datetime.max)    # format: YYYY-MM-DD hh:mm:ss.mmmmmm

        start = request.args.get("start", default=DEFAULT_START, type=str)
        end = request.args.get("end", default=DEFAULT_END, type=str)
        sensor_id = request.args.get("sensor_id", default=None, type=int)
        feature_id = request.args.get("feature_id", default=None, type=int)

        query = db.select(Observation)
        query = query.filter(Observation.timestamp >= start)
        query = query.filter(Observation.timestamp <= end)

        if sensor_id is not None:
            query = query.filter(Observation.sensor_id == sensor_id)

        if feature_id is not None:
            query = query.filter(Observation.feature_id == feature_id)

        observations_list = db.session.execute(query).scalars()
        return [o.serialize() for o in observations_list], 200

    def post(self):
        data = request.json
        observation = Observation(
            sensor_id=data["sensor_id"],
            feature_id=data["feature_id"],
            timestamp=data["timestamp"],
            value=data["value"]
        )
        db.session.add(observation)
        db.session.commit()
        return observation.serialize(), 201
