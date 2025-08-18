# Comunidade Impressionadora
Um sistema web em Flask para gerenciamento de usuários, autenticação, posts e perfis personalizados.  

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.1.1-black.svg)
![Postgres](https://img.shields.io/badge/PostgreSQL-15.0-blue.svg)

## 📌 Sobre o Projeto
O **Comunidade Impressionadora** é uma aplicação web construída em Flask que permite:
- Criar e gerenciar usuários com autenticação (login e logout).
- Editar perfis com upload de foto e cursos concluídos.
- Criar, visualizar, editar e excluir posts.
- Visualizar todos os usuários da comunidade.

A aplicação foi desenvolvida com foco em aprendizado e prática de **Flask, SQLAlchemy, autenticação com Flask-Login e PostgreSQL/SQLite**.

## ✅ Funcionalidades
- [x] Criar conta e login de usuários
- [x] Autenticação com Flask-Login
- [x] Upload e atualização de foto de perfil
- [x] Criar, editar e excluir posts
- [x] Listagem de usuários
- [ ] Área de administração (em breve)

## 🖼️ Demonstração
### Tela de Login
![Tela de Login](comunidadeimpressionadora/static/readme_images/tela_login.png)

### Perfil do Usuário
![Perfil](comunidadeimpressionadora/static/readme_images/meu_perfil.png)
![Editar Perfil](comunidadeimpressionadora/static/readme_images/editar_perfil.png)

### Feed de Posts
![Feed](comunidadeimpressionadora/static/readme_images/home.png)
![Editar post](comunidadeimpressionadora/static/readme_images/editar_post.png)

### Listagem de Usuários
![Feed](comunidadeimpressionadora/static/readme_images/usuarios.png)

## 🛠 Tecnologias
- [Python 3.12](https://www.python.org/)
- [Flask 3.1.1](https://flask.palletsprojects.com/)
- [Flask-Login](https://flask-login.readthedocs.io/)
- [Flask-WTF](https://flask-wtf.readthedocs.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/) (produção) / SQLite (desenvolvimento)
- [Gunicorn](https://gunicorn.org/) (deploy)

## 🌐 Deploy
A aplicação está disponível em produção no [Railway](https://railway.app/).



