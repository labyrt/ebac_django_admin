# Meu Blog — Django e pytest

Projeto desenvolvido para o exercício de Python Avançado da EBAC. A aplicação
contém o aplicativo `blog`, o modelo `Post` e um teste automatizado com pytest.

## Tecnologias

- Python 3.12
- Django 5.2 LTS
- pytest
- pytest-django
- SQLite

## Preparação do ambiente

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python manage.py migrate
```

No Windows, ative o ambiente com `.venv\\Scripts\\activate`.

## Executar o projeto

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` no navegador.

## Executar os testes

```bash
pytest
```

O teste em `blog/tests/test_post_model.py` cria um usuário e um post, consulta o
registro salvo e valida seus campos, valores padrão, datas e representação em texto.
