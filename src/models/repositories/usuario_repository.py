from src.models.interfaces.usuario_interface import Interface_Usuario
from src.models.usuario_model import User
from src.settings.extensions import db

class Repository_Usuario(Interface_Usuario):

    def cadastra_usuario(self, name: str, email: str, password_hash: str) -> User:
        user = User(
            name=name,
            email=email,
            password_hash=password_hash
        )

        db.session.add(user)
        db.session.commit()

        return user

    def busca_por_email(self, email: str):
        return db.session.query(User).filter(User.email == email).first()
