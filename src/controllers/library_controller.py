
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.library import Library, library_schema, libraries_schema

library_bp = Blueprint("library", __name__, url_prefix="/library")


# /library - GET - fetch all libary
@library_bp.route("/")
def get_all_libraries():
    libraries = Library.query.all()
    return libraries_schema.dump(libraries)

# /library/<id> - GET - fetch a specific library

# /library - POST - create a new library
# /library/<id> - DELETE - delete a library
# /library/<id> - PUT, PATCH - edit a library entry
