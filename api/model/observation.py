from database import db
import sqlalchemy as sa

class Observation(db.Model):
    __tablename__ = "observation"
    sensor_id = sa.Column(sa.Integer, db.ForeignKey("sensor.id", ondelete="CASCADE"), primary_key=True)
    feature_id = sa.Column(sa.Integer, db.ForeignKey("feature.id", ondelete="CASCADE"), primary_key=True)
    timestamp = sa.Column(sa.String, primary_key=True)
    value = sa.Column(sa.Float, nullable=False)

    def serialize(self):
        return dict(
            sensor_id = self.sensor_id,
            feature_id = self.feature_id,
            timestamp = self.timestamp,
            value = self.value
        )
