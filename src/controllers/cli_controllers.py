from datetime import date

from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.library import Library 
from models.episode import Episode


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

    libraries = [
        Library(
            user = users[0]
        ), 
        Library(
            user = users[1]
        )
    ]       

    db.session.add_all(libraries)


    episodes = [
        Episode(
            title = "Episode 1",
            episode_number = 1,
            date = date.today(),
            libraries = libraries[0]
        ),
        Episode(
            title = "Episode 2",
            episode_number = 2,
            date = date.today(),
            libraries = libraries[0]
        ),
        Episode(
            title = "Episode 3",
            episode_number = 3,
            date = date.today(),
            libraries = libraries[1]
        )
    ]

    db.session.add_all(episodes)

    db.session.commit()

    print("Tabels seeded!")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables droppped.")
