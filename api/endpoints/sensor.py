from flask_restful import Resource
from flask import request, jsonify
from database import db
from model.sensor import Sensor

class SensorsEndpoint(Resource):
    def get(self):
        sensor_list = db.session.execute(db.select(Sensor)).scalars()
        return [s.serialize() for s in sensor_list], 200

    
    def post(self):
        data = request.json

        name = data["name"]

        description = None
        if "description" in data.keys():
            description = data["description"]

        location = None
        if "location" in data.keys():
            location = data["location"]

        sensor = Sensor(
            name=name,
            description=description,
            location=location
        )
        db.session.add(sensor)
        db.session.commit()
        return sensor.serialize(), 201


class SensorEndpoint(Resource):
    def get(self, id):
        sensor = db.session.execute(db.select(Sensor).where(Sensor.id == id)).scalar()
        
        if sensor == None:
            return f"Sensor with id:{id} does not exist.", 404
        
        return sensor.serialize(), 200

    
    def delete(self, id):
        sensor = db.session.execute(db.select(Sensor).where(Sensor.id == id)).scalar()

        if sensor == None:
            return f"Sensor with id:{id} does not exist.", 404

        db.session.delete(sensor)
        db.session.commit()
        return sensor.serialize(), 200

    


    
