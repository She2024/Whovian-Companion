from init import db, ma
from marshmallow import fields


class User (db.Model):
    #table name
    __tablename__= "users"

    # attributes of table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(25))
    email = db.Column(db.VARCHAR(100), nullable=False, unique=True)
    password = db.Column(db.VARCHAR, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    library = db.relationship("Library", back_populates="user")

class UserSchema(ma.Schema):
    class Meta:
        library = fields.Nested('LibrarySchema', exclude=["user"])

        fields = ("id", "name", "email", "password", "is_admin", "library")
        

# to handle a single user object, excludes password for privacy/security
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects, excludes password for privacy/security
users_schema = UserSchema(many=True, exclude=["password"])