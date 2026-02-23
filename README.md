# Desafio API de Gestão de Tarefas (To-Do) com Autenticação

Segue um modelo simples e direto de `README.md` para o seu projeto:

---

# API de Gestão de Tarefas (To-Do) com Autenticação

API REST desenvolvida com Flask para gerenciamento de tarefas com autenticação via JWT.

## Tecnologias Utilizadas

* Python 3.13+
* Flask
* Flask-JWT-Extended
* Flask-SQLAlchemy
* SQLite
* Pytest
* Bcrypt

---

## Funcionalidades

* Registro de usuário
* Login com geração de token JWT
* Criação de tarefas
* Listagem de tarefas do usuário autenticado
* Consulta de tarefa específica
* Atualização completa (PUT)
* Atualização parcial (PATCH)
* Remoção de tarefa

Todas as rotas de tarefas são protegidas por autenticação JWT.

---

## Estrutura do Projeto

```
src/
 ├── models/
 │    ├── usuario_model.py
 │    ├── tarefa_model.py
 │    └── repositories/
 ├── routes/
 ├── settings/
 ├── utils/
 └── tests/
```

---

## Como Executar o Projeto

### 1. Clonar o repositório

```
git clone <url-do-repositorio>
cd nome-do-projeto
```

### 2. Criar ambiente virtual

```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente (se necessário)

Exemplo:

```
export FLASK_ENV=development
export SECRET_KEY=sua_chave_secreta
```

Ou criar um arquivo `.env` se estiver utilizando python-dotenv.

---

### 5. Executar a aplicação

```
flask run
```

Ou, se houver arquivo principal:

```
python run.py
```

A aplicação estará disponível em:

```
http://127.0.0.1:5000
```

---

## Autenticação

### Registrar usuário

```
POST /auth/register
```

Body JSON:

```
{
  "name": "Nome",
  "email": "email@email.com",
  "password": "senha"
}
```

---

### Login

```
POST /auth/login
```

Body JSON:

```
{
  "email": "email@email.com",
  "password": "senha"
}
```

Resposta:

```
{
  "access_token": "..."
}
```

---

## Uso do Token

Para acessar rotas protegidas, envie no header:

```
Authorization: Bearer <seu_token>
```

---

## Rotas de Tarefas

Criar tarefa:

```
POST /tarefas/tasks
```

Listar tarefas:

```
GET /tarefas/tasks
```

Buscar tarefa específica:

```
GET /tarefas/tasks/<id>
```

Atualização completa:

```
PUT /tarefas/tasks/<id>
```

Atualização parcial:

```
PATCH /tarefas/tasks/<id>
```

Remover tarefa:

```
DELETE /tarefas/tasks/<id>
```

---

## Executar Testes

```
pytest -s -v
```

Ou para um arquivo específico:

```
pytest src/tests/tarefa_repository_test.py
```

---

## Observações

* O banco utilizado é SQLite.
* As senhas são armazenadas com hash utilizando Bcrypt.
* As rotas de tarefas exigem autenticação JWT.
* O projeto utiliza padrão Repository para acesso ao banco.


