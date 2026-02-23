from flask import (
    Blueprint,
    jsonify,
    request
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from src.models.repositories.tarefa_repository import Repository_Tarefa
from src.models.repositories.usuario_repository import Repository_Usuario

tarefas_bp = Blueprint("tarefas", __name__, url_prefix="/tarefas")

@tarefas_bp.route("/tasks", methods=["POST"])
@jwt_required()
def creater_tasks():
    repo_tarefa = Repository_Tarefa()
    repo_user = Repository_Usuario()
    current_user_email = get_jwt_identity()
    
    try:
        
        data = request.get_json()
        
        user = repo_user.busca_por_email(current_user_email)
        
        if not user:
            return jsonify({"found": "Usuário não localizado."}), 404
        
        if not data:
            return jsonify({"error": "É necessário body com JSON."}), 400

        repo_tarefa.create_tarefa(**data)
        
        return jsonify({"msg": "Tarefa criada com sucesso."}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)})
    
    
@tarefas_bp.route("/tasks", methods=["GET"])
@jwt_required()
def list_tasks():
    repo_tarefa = Repository_Tarefa()
    repo_user = Repository_Usuario()
    current_user_email = get_jwt_identity()
    
    try:
        
        user = repo_user.busca_por_email(current_user_email)
        
        if not user:
            return jsonify({"found": "Usuário não localizado."}), 404
        
        lista_tarefas = repo_tarefa.list_tarefas(user.id)
        
        return jsonify([tarefa.to_dict() for tarefa in lista_tarefas])
        
    except Exception as e:
        return jsonify({"error": str(e)})
    

@tarefas_bp.route("/tasks/<int:id>", methods=["GET"])
@jwt_required()
def one_registry_tasks(id):
    repo_tarefa = Repository_Tarefa()
    repo_user = Repository_Usuario()
    current_user_email = get_jwt_identity()
    
    try:
        
        user = repo_user.busca_por_email(current_user_email)
        
        if not user:
            return jsonify({"found": "Usuário não localizado."}), 404
        
        tarefa_obj = repo_tarefa.one_registry_tarefa(user.id, id)
        
        return jsonify(tarefa_obj.to_dict())
        
    except Exception as e:
        return jsonify({"error": str(e)})


@tarefas_bp.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update_all_tasks(id):

    repo_tarefa = Repository_Tarefa()
    repo_user = Repository_Usuario()
    current_user_email = get_jwt_identity()

    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Não possui atributos para atualização completa."}), 400

        user = repo_user.busca_por_email(current_user_email)

        if not user:
            return jsonify({"error": "Usuário não localizado."}), 404

        repo_tarefa.update_all_registry(id, **data)

        return jsonify({"msg": f"Tarefa {id} foi atualizada com sucesso"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@tarefas_bp.route("/tasks/<int:id>", methods=["PATCH"])
@jwt_required()
def update_one_tasks(id):
    repo_tarefa = Repository_Tarefa()
    repo_user = Repository_Usuario()
    current_user_email = get_jwt_identity()
    
    try:
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "Não possuir os atributos para atualização completa."}), 400
        
        user = repo_user.busca_por_email(current_user_email)
        
        if not user:
            return jsonify({"found": "Usuário não localizado."}), 404
        
        repo_tarefa.update_one_registry(id, data)
        
        return jsonify({"msg": f"Tarefa {id}, foi atualizado pacialmente."}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)})
    

@tarefas_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_tasks(id):
    repo_tarefa = Repository_Tarefa()
    repo_user = Repository_Usuario()
    current_user_email = get_jwt_identity()
    
    try:
        user = repo_user.busca_por_email(current_user_email)
        
        if not user:
            return jsonify({"found": "Usuário não localizado."}), 404
        
        repo_tarefa.delete_one_registry(id)
        
        return jsonify({"msg": f"Tarefa {id}, foi deletado com sucesso"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)})