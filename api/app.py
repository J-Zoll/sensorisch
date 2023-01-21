from flask import Flask
from flask_restful import Api
import json
from database import db
import database

from endpoints.sensor import SensorsEndpoint, SensorEndpoint

app = Flask(__name__)
api = Api(app)

app.config.from_file("config.json", load=json.load)
db.init_app(app)

database.setup(app=app)


# add endpoints
api.add_resource(SensorsEndpoint, "/sensor")
api.add_resource(SensorEndpoint, "/sensor/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)