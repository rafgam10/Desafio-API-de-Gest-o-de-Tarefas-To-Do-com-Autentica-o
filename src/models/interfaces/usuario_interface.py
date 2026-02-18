from abc import ABC, abstractmethod
from typing import Optional
from src.models.usuario_model import User

class Interface_Usuario(ABC):

    @abstractmethod
    def cadastra_usuario(self, name: str, email: str, password_hash: str) -> User:
        pass

    @abstractmethod
    def busca_por_email(self, email: str) -> Optional[User]:
        pass
