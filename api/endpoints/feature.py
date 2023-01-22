from flask_restful import Resource
from flask import request
from database import db
from model.feature import Feature

class FeaturesEndpoint(Resource):
    def get(self):
        feature_list = db.session.execute(
            db.select(Feature)
        ).scalars()
        return [f.serialize() for f in feature_list], 200

    def post(self):
        data = request.json

        name = data["name"]
        description = None
        if not "description" in data.keys():
            description = data["description"]
        unit = data["unit"]

        feature = Feature(name=name, description=description, unit=unit)
        db.session.add(feature)
        db.session.commit()
        return feature.serialize(), 201


class FeatureEndpoint(Resource):
    def get(self, id):
        feature = db.session.execute(
            db.select(Feature).where(Feature.id == id)
        ).scalar()

        if feature == None:
            return f"Feature with id:{id} does not exist.", 404
        return feature.serialize(), 200

    def delete(self, id):
        feature = db.session.execute(
            db.select(Feature).where(Feature.id == id)
        ).scalar()

        if feature == None:
            return f"Feature with id:{id} does not exist.", 404
        db.session.delete(feature)
        db.session.commit()
        return feature.serialize(), 200
        

    


    
