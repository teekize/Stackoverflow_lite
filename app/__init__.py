from flask import Flask


def create_app():
    app=Flask(__name__)


    from app.api.v1.users.views import users
    app.register_blueprint(users)
    return app