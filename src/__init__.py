from flask import Flask
from .settings.config import Config
from .settings.extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    with app.app_context():
        from src.models import User, Tarefa
        db.create_all()

    try:
        from .routes import register_routes
        register_routes(app)
        
        from src.routes.auth_routes import auth_bp
        from src.routes.tarefas_routes import tarefas_bp
        
        app.register_blueprint(auth_bp)
        app.register_blueprint(tarefas_bp)
        
    except Exception:
        pass

    return app
