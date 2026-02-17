from src.settings.extensions import db
import datetime
import enum

class StatusTarefa(enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Tarefa(db.Model):
    
    __tablename__ = "tarefas"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    status = db.Column(db.String, default=StatusTarefa.PENDING.value, nullable=False)
    due_date = db.Column(db.Datetime, nullable=True)
    created_at = db.Column(db.Datetime, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.Datetine, server_default=db.func.now())
    
    user = db.relationship("User", back_populates="tarefas")
    
    def __repr__(self):
        return f"Tarefa: {self.user_id} - {self.title} - {self.status}"