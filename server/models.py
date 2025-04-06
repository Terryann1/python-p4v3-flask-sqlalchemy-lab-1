from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model,SerializerMixin):
    __tablename__="earthquakes"
    id=db.Column(db.Integer,primary_key=True)
    location=db.Column(db.String(),nullable=False)
    magnitude=db.Column(db.Float,nullable=False)
    year=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"<Earthquake {self.id} {self.magnitude} {self.location} {self.year}>"

    def to_dict(self):
        return {
            "id": self.id,  
            "magnitude": self.magnitude,
            "location": self.location,
            "year": self.year
        }