from src.settings.extensions import db
import datetime

class User(db.Model):
    
    __tablename__ = "usuario"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Datetime, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.Datetine, server_default=db.func.now())
    
    tarefas = db.relationship("Tarefa", back_populates="usuario")
    
    def __repr__(self):
        return f"User: {self.name} - {self.email} - {self.password_hash} - {self.created_at} - {self.updated_at}"