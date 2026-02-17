from src.settings.extensions import db
from sqlalchemy import func
import datetime

class User(db.Model):
    
    __tablename__ = "usuario"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now)
    
    tarefas = db.relationship("Tarefa", back_populates="usuario")
    
    def __init__(self, name, email, password_hash):
        self.name = name
        self.email = email,
        self.password_hash = password_hash,
    
    def __repr__(self):
        return f"User: {self.name} - {self.email} - {self.password_hash} - {self.created_at} - {self.updated_at}"