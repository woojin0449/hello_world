from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(): #애플리케이션 팩토리 정해진 이름이므로 바꾸면 작동X
    app=Flask(__name__)
    app.config.from_object(config)

    #ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models

    # @app.route("/")
    # def hello_pybo(): #라우팅 함수 @app랑 연결해줌
    #     return "Hello, Pybo!!"

    #블루프린트
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app