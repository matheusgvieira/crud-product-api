# API FastAPI de Produtos

Bem-vindo à API FastAPI de Produtos! Esta API permite gerenciar informações sobre produtos.

## Pré-requisitos

Antes de executar os comandos, certifique-se de ter as seguintes dependências instaladas:

- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação de Dependências

Para instalar as dependências do projeto, execute o seguinte comando:

```sh
make install
```

## Banco de Dados

Para executar apenas o banco de dados usando o Docker Compose em ambiente de desenvolvimento, utilize o seguinte comando:

```sh
docker-compose -f docker-compose-dev.yml up -d db
```

## Migrações do Banco de Dados

Para executar as migrações do banco de dados usando Alembic, utilize o seguinte comando:

```sh
alembic upgrade head
```

## Seeds do Banco de Dados

Para executar as seeds do banco de dados, utilize o seguinte comando:

```sh
python seeds/run.py
```

## Executando a API

Para executar a API FastAPI, utilize o seguinte comando:

```sh
python -m products_api run --port 8000
```

ou

```sh
uvicorn products_api:app--reload
```

## Executando com Docker

Para executar a aplicação usando Docker Compose, utilize o seguinte comando:

```sh
docker-compose up
```

## Executando com Dockerfile

Para construir e executar a aplicação usando o Dockerfile, utilize os seguintes comandos:

```sh
docker build -t api-produtos .
docker run -p 8000:8000 api-produtos
```

## Contato

Se você encontrar algum problema ou tiver perguntas, não hesite em nos contatar em matheusmaxi9.0@gmail.com.

Divirta-se explorando a API!

```

Este README inclui todas as etapas necessárias para instalar as dependências, executar o banco de dados, realizar migrações e seeds, bem como executar a API FastAPI de Produtos. Certifique-se de substituir `matheusmaxi9.0@gmail.com` pelo contato de suporte real e adaptar os comandos e detalhes conforme necessário para o seu projeto.
```
