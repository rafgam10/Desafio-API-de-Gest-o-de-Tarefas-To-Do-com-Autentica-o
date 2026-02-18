from abc import ABC, abstractmethod

class Interface_Tarefa(ABC):
    
    @abstractmethod
    def create_tarefa():
        pass
    
    @abstractmethod
    def list_tarefas():
        pass
    
    @abstractmethod
    def one_registry_tarefa():
        pass
    
    @abstractmethod
    def update_all_registry():
        pass
    
    @abstractmethod
    def update_one_registry():
        pass
    
    @abstractmethod
    def delete_one_registry():
        pass