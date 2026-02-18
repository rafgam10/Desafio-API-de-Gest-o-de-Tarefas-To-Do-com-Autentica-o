from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from email_validator import validate_email, EmailNotValidError

from src.models.repositories.usuario_repository import Repository_Usuario
from src.utils.util_hash import create_password_hash, verify_password

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# =========================
# REGISTER
# =========================
@auth_bp.route("/register", methods=["POST"])
def register_user():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"msg": "É necessário enviar os dados do usuário."}), 400

        # validação de campos obrigatórios
        required_fields = ["name", "email", "password"]
        for field in required_fields:
            if field not in data:
                return jsonify({"msg": f"Campo obrigatório ausente: {field}"}), 400

        # valida email
        try:
            validate_email(data["email"])
        except EmailNotValidError as e:
            return jsonify({"msg": str(e)}), 400

        repo = Repository_Usuario()

        # verifica se já existe usuário
        existing_user = repo.busca_por_email(data["email"])
        if existing_user:
            return jsonify({"msg": "Email já cadastrado."}), 409

        # cria usuário
        user = repo.cadastra_usuario(
            name=data["name"],
            email=data["email"],
            password_hash=create_password_hash(data["password"])
        )

        return jsonify({
            "msg": "Usuário registrado com sucesso!",
            "user_id": user.id
        }), 201

    except Exception as e:
        return jsonify({"msg": str(e)}), 500


# =========================
# LOGIN
# =========================
@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"msg": "É necessário enviar email e password."}), 400

        required_fields = ["email", "password"]
        for field in required_fields:
            if field not in data:
                return jsonify({"msg": f"Campo obrigatório ausente: {field}"}), 400

        repo = Repository_Usuario()
        user = repo.busca_por_email(data["email"])

        if not user:
            return jsonify({"msg": "Credenciais inválidas."}), 401

        if not verify_password(data["password"], user.password_hash):
            return jsonify({"msg": "Credenciais inválidas."}), 401

        access_token = create_access_token(identity=user.email)

        return jsonify({
            "access_token": access_token
        }), 200

    except Exception as e:
        return jsonify({"msg": str(e)}), 500
