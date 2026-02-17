from src.settings.extensions import db
import datetime

class User(db.Model):
    
    __tablename__ = "usuario"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, server_default=db.func.now())
    
    tarefas = db.relationship("Tarefa", back_populates="usuario")
    
    def __init__(self, name, email, password_hash, created_at, updated_at):
        self.name = name
        self.email = email,
        self.password_hash = password_hash,
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return f"User: {self.name} - {self.email} - {self.password_hash} - {self.created_at} - {self.updated_at}"