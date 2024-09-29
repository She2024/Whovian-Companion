from init import db, ma
from marshmallow import fields

from models.library_episodes import library_episode_association
#

# Create a Model of a table
class Episode(db.Model):
     # Define the name of the table
    __tablename__ = "episodes"
   # Define the Primary key
    id = db.Column(db.Integer, primary_key=True)
     # Define other attributes
    title = db.Column(db.String, nullable=False)
    episode_number = db.Column(db.Integer)
    date = db.Column(db.Date) #date created

    libraries = db.relationship('Library', 
        secondary=library_episode_association, back_populates='episodes')

class EpisodeSchema(ma.Schema):
    library = fields.List(fields.Nested('LibrarySchema', only=["id","user_id"]))
    class Meta:
        fields = ("id", "title", "episode_number", "date", "library")

episode_schema = EpisodeSchema()
episodes_schema = EpisodeSchema(many=True) 
   


    