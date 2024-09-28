from sqlalchemy import Column
from init import db, ma
from marshmallow import fields, validates
from src.models import my_library

# Create a Model of a table
class MyLibrary(db.Model):
     # Define the name of the table
    __tablename__ = "my_library"
   # Define the Primary key
    id = db.Column(db.Integer, primary_key=True)
     # Define other attributes
    title = db.Column(db.String, nullable=False)
    episode_number = db,Column(db.Integer)
    date = db.Column(db.Date) #date created

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

class MyLibrarySchema(ma.Schema):
    user = fields.List(fields.Nested('UserSchema', only=["id", "name", "email"]))
    class Meta:
        fields = ("id", "title", "episode_number", "date", "user_id")

my_library_schema = MyLibrarySchema()
my_library_schema = MyLibrarySchema(many=True)    
   

my_library = db.relationship('User', back_populates='MyLibrary') 
comments = db.relationship('Comment', back_populates='card', cascade="all, delete")
    