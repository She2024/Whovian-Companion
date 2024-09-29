
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.my_library import MyLibrary, my_library_schema, my_libraries_schema

my_library_bp = Blueprint("my_library", __name__, url_prefix="/my_library")


# /library - GET - fetch all libary
@my_library_bp.route("/")
def get_all_my_libraries():
    stmt = db.select(MyLibrary)
    my_library = db.session.scalars(stmt)
    return my_libraries_schema.dump(my_library)

# /library/<id> - GET - fetch a specific library

# /library - POST - create a new library
# /library/<id> - DELETE - delete a library
# /library/<id> - PUT, PATCH - edit a library entry
