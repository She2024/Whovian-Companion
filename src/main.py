from flask import Flask

from init import db, ma, bcrypt, jwt

# Application factories

def creeate_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] ="postgressql+psycopg2://whovian_dev:123456@localllhoost:554432/whovian_db"
    app.config["Jwt_SECRET_KEY"] = "secret"

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)   
    jwt.init_app(app)

    return app