from src.models.interfaces.tarefa_interface import Interface_Tarefa
from src.models.tarefa_model import Tarefa
from src.settings.extensions import db

import datetime

class Repository_Tarefa(Interface_Tarefa):
    
    def create_tarefa(self, user_id:int, title:str, description:str) -> None:
        try:
            
            nova_tarefa = Tarefa(
                id_user =user_id,
                title=title,
                description=description
            )
            db.session.add(nova_tarefa)
            db.session.commit()
            
            return nova_tarefa
            
        except Exception as e:
            return str(e)
    
    def list_tarefas(self, id_user: int) -> list:
        try:
            lista_tarefas = db.session.query(Tarefa).filter(Tarefa.user_id == id_user).all()
            
            if not lista_tarefas:
                return None
            
            return lista_tarefas
        
        except Exception as e:
            return str(e)
            
    
    def one_registry_tarefa(self, id_user:int, id_tarefa:int) -> dict:
        try:
            dict_tarefa = db.session.query(Tarefa).filter(Tarefa.user_id == id_user and Tarefa.id == id_tarefa).first()
            
            if not dict_tarefa:
                return None
            
            return dict_tarefa
        
        except Exception as e:
            return str(e)
        
    
    def update_all_registry(self, id_tarefa:int, title:str, description:str, status: str) -> None:
        try:
            select_tarefa = db.session.query(Tarefa).filter(Tarefa.id == id_tarefa).first()
            
            if not select_tarefa:
                return None
            
            select_tarefa.title = title
            select_tarefa.description = description
            select_tarefa.status = status
            select_tarefa.updated_at = datetime.datetime.now()
            db.session.commit()
            print(title, description, status)
        
        except Exception as e:
            return str(e)
         
    
    def update_one_registry(self, id_tarefa: int, data: dict):

        select_tarefa = db.session.query(Tarefa).filter(
            Tarefa.id == id_tarefa
        ).first()

        if not select_tarefa:
            raise ValueError("Tarefa não encontrada")

        allowed_fields = {"title", "description", "status"}

        for key, value in data.items():
            if key in allowed_fields:
                setattr(select_tarefa, key, value)

        db.session.commit()

        return select_tarefa
            
    
    def delete_one_registry(self, id_tarefa:int) -> None:
        try:
            select_tarefa = db.session.query(Tarefa).filter(Tarefa.id == id_tarefa).first()
            if not select_tarefa:
                return ValueError("Tarefa não encontrada")
            
            db.session.delete(select_tarefa)
            db.session.commit()
            
            return select_tarefa
        
        except Exception as e:
            return str(e)