from database import db
import sqlalchemy as sa

class Thing(db.Model):
    __tablename__ = "thing"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=True)
    location = sa.Column(sa.String, nullable=True)

    def serialize(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            location = self.location
        )
