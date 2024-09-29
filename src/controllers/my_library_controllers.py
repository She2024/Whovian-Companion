from datetime import date
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.my_library import MyLibrary, my_library_schema, my_libraries_schema
from utils import auth_as_admin_decorator

my_library_bp = Blueprint("my_library", __name__, url_prefix="/my_library")


# /library - GET - fetch all libary
@my_library_bp.route("/")
def get_all_my_libraries():
    stmt = db.select(MyLibrary)
    my_library = db.session.scalars(stmt)
    return my_libraries_schema.dump(my_library)

# /library/<id> - GET - fetch a specific library
@my_library_bp.route("/<int:card_id>")
def get_a_my_library(my_library_id):
    stmt = db.select(MyLibrary).filter_by(id=my_library_id)
    # stmt = db.select(Card).where(Card.id==card_id)
    my_library = db.session.scalar(stmt)
    if my_library:
        return my_library_schema.dump(my_library)
    else:
        return {"error": f"Library with id '{my_library_id}' not found"}, 404
    
# /library - POST - create a new library
@my_library_bp.route("/", methods=["POST"])
@jwt_required()
def create_my_library():
    # get the data from the body of the request
    body_data = my_library_schema.load(request.get_json())
    # create a new card model instance
    my_library = MyLibrary(
        title = body_data.get("title"),
        episode = body_data.get("description"),
        date = date.today(),        
        user_id = get_jwt_identity()
    )
    # add and commit to the DB
    db.session.add(my_library)
    db.session.commit()
    # response message
    return my_library_schema.dump(my_library)

# /library/<id> - DELETE - delete a library
@my_library_bp.route("/<int:my_library_id>", methods=["DELETE"])
@jwt_required()
@auth_as_admin_decorator
def delete_card(my_library_id):
    # check whether the user is admin or not
    # is_admin = authorise_as_admin()
    # if not admin
    # if not is_admin:
    #     # return error message
    #     return {"error": "User is not authorized to perform this action."}

    # fetch the card from the database
    stmt = db.select(MyLibrary).filter_by(id=my_library_id)
    card = db.session.scalar(stmt)
    # if card exists
    if card:
        # delete the card
        db.session.delete(my_library_id)
        db.session.commit()
        return {"message": f"Library {my_library_id.title} deleted successfully!"}
    # else
    else:
        # return error message
        return {"error": f"Card with id {my_library_id} not found"}, 404

# /library/<id> - PUT, PATCH - edit a library entry
@my_library_bp.route("/<int:my_library_id>", methods=["PUT", "PATCH"])
@jwt_required()
@auth_as_admin_decorator
def update_my_library(my_library_id):
    # get the info from the body of the request
    body_data = my_library_schema.load(request.get_json(), partial=True)
    # get the card from the database
    stmt = db.select(MyLibrary).filter_by(id=my_library_id)
    my_library = db.session.scalar(stmt)
    # check whether the user is admin or not
    # is_admin = authorise_as_admin()
    # if the card exists
    if my_library:
    #     # if the user is not the owner of the card
    #     if not is_admin and str(card.user_id) != get_jwt_identity():
    #         # return error message
    #         return {"error": "Cannot perform this operation. Only owners are allowed to execute this operation."}

        # update the fields as required
        my_library.title = body_data.get("title") or my_library.title
        my_library.description = body_data.get("description") or my_library.description
        my_library.status = body_data.get("status") or my_library.status
        my_library.priority = body_data.get("priority") or my_library.priority
        # commit to the DB
        db.session.commit()
        # return acknowledgement
        return my_library_schema.dump(my_library)
    # else
    else:
        # return error message
        return {"error": f"Library with id {my_library_id} not found."}, 404