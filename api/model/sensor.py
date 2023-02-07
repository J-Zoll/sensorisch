from database import db
import sqlalchemy as sa

class Sensor(db.Model):
    __tablename__ = "sensor"
    id = sa.Column(sa.Integer, primary_key=True)
    thing_id = sa.Column(sa.Integer, nullable=False)
    feature_id = sa.Column(sa.Integer, nullable=False)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)

    def serialize(self):
        return dict(
            id = self.id,
            thing_id = self.thing_id,
            feature_id = self.feature_id,
            name = self.name,
            description = self.description
        )
