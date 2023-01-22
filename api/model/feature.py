from database import db
import sqlalchemy as sa

class Feature(db.Model):
    __tablename__ = "feature"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    unit = sa.Column(sa.String, nullable=False)

    def serialize(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            unit = self.unit
        )
