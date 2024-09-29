from init import db, ma
from marshmallow import fields
from models.library_episodes import library_episode_association

class Library(db.Model):
    __tablename__ = "libraries"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", back_populates="library")
    episodes = db.relationship("Episode", 
        secondary=library_episode_association, back_populates="libraries")


class LibrarySchema(ma.Schema):
    episodes = fields.List(fields.Nested('EpisodeSchema', only=["id","title","episode_number","date"]))
    user = fields.Nested('UserSchema', only=("id", "name", "email"))
    class Meta:
        fields = ("id", "user", "episodes")

library_schema = LibrarySchema()
libraries_schema = LibrarySchema(many=True)
