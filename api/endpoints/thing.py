from flask_restful import Resource
from flask import request, jsonify
from database import db
from model.thing import Thing

class ThingsEndpoint(Resource):
    def get(self):
        thing_list = db.session.execute(db.select(Thing)).scalars()
        return [t.serialize() for t in thing_list], 200

    
    def post(self):
        data = request.json

        name = data["name"]

        description = None
        if "description" in data.keys():
            description = data["description"]

        location = None
        if "location" in data.keys():
            location = data["location"]

        thing = Thing(
            name=name,
            description=description,
            location=location
        )
        db.session.add(thing)
        db.session.commit()
        return thing.serialize(), 201


class ThingEndpoint(Resource):
    def get(self, id):
        thing = db.session.execute(db.select(Thing).where(Thing.id == id)).scalar()
        
        if thing == None:
            return f"Thing with id:{id} does not exist.", 404
        
        return thing.serialize(), 200

    
    def delete(self, id):
        thing = db.session.execute(db.select(Thing).where(Thing.id == id)).scalar()

        if thing == None:
            return f"Thing with id:{id} does not exist.", 404

        db.session.delete(thing)
        db.session.commit()
        return thing.serialize(), 200

    


    
