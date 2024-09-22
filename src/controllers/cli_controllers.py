from flask import Blueprint
from init import db, bcrypt
from models.user import User

db_commands = Blueprint("db", __name__)

#create new tables in the database
@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("seed")
def seed_tables():
    # Create a list of User instances
    users = [
        User(
            email = "admin@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin = True
        ), 
        User(
            name = "User A",
            email = "usera@email.com",
            password = bcrypt.generate_password_hash("123456").decode("utf-8")
        )
    ]

    db.session.add_all(users)

    db.session.commit()

    print("Tabels seeded!")