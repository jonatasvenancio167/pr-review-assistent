# Code Review Inteligente com Python e RAG

Assistente de code review com arquitetura modular baseada em Service Objects. O objetivo é analisar alterações de código, recuperar conhecimento técnico e produzir apontamentos fundamentados. O fluxo de review será implementado incrementalmente; a base de infraestrutura e as primeiras estruturas de domínio já existem.

A [documentação da arquitetura](docs/arquitetura.md) descreve as camadas, os fluxos de review e ingestão, os contratos de domínio, as responsabilidades dos serviços, a estratégia de testes e as etapas de evolução. Ela distingue os componentes existentes dos planejados.

## Ambiente FastAPI + PostgreSQL + pgvector

Ambiente Docker com Python 3.12, FastAPI, SQLAlchemy 2 assíncrono, asyncpg e Alembic. PostgreSQL 17 usa a imagem do projeto pgvector. A API executa com usuário sem privilégios. O Compose aguarda o banco saudável, executa `alembic upgrade head` em um serviço separado e então inicia a API.

## Iniciar

Requisitos: Docker Engine e Docker Compose v2.

`requirements.in` declara as dependências diretas e `requirements.txt` fixa as versões resolvidas no Python 3.12 Linux para o build. Ao atualizar dependências, atualize também esse arquivo e repita a validação de integração.

```bash
cp .env.example .env
# Edite POSTGRES_PASSWORD em .env antes de iniciar.
docker compose up -d --build --wait
```

Se `.env` já existir, preserve seu conteúdo. Neste projeto, a configuração inicial inclui um `.env` local com senha aleatória; esse arquivo é ignorado pelo Git e pelo build.

Na máquina usada para validação, a porta 8000 já estava ocupada. O `.env` local foi configurado com `API_PORT=8001`; nesse caso, acesse http://localhost:8001/docs. Os exemplos abaixo usam a porta padrão do `.env.example`.

- Swagger: http://localhost:8000/docs
- OpenAPI: http://localhost:8000/openapi.json
- Liveness: http://localhost:8000/health/live
- Readiness (banco e extensão): http://localhost:8000/health/ready

```bash
docker compose ps -a
docker compose logs -f api migrate db
docker compose down
```

`down` preserva o volume `postgres_data`. `docker compose down -v` apaga definitivamente o banco. Credenciais de PostgreSQL são aplicadas na inicialização do volume: mudar a senha em `.env` não muda a senha de um banco existente; use `ALTER ROLE` antes de atualizar a configuração.

## Desenvolvimento

```bash
# Ajuste LOCAL_UID e LOCAL_GID em .env conforme id -u e id -g.
docker compose -f compose.yaml -f compose.dev.yaml up -d --build --wait
```

Esse modo monta `app/`, habilita `--reload` e publica PostgreSQL somente em `127.0.0.1:5432`. Configure `API_PORT` e `POSTGRES_EXTERNAL_PORT` em `.env` se houver conflito de portas. Na rede Docker a API sempre conecta em `db:5432`; ferramentas no host conectam em `localhost` usando a porta externa e as credenciais de `.env`.

## Modelos e migrações

`app/database.py` fornece `Base`, `SessionFactory` e a dependência `get_session`. Use `Depends(get_session)` nas rotas e faça `await session.commit()` explicitamente quando gravar dados. Registre novos modelos em `app/models.py` ou importe-os em `alembic/env.py` para que o Alembic encontre seu metadata.

A revisão `0001` habilita a extensão `vector` e cria `documents`, uma tabela de exemplo com `Vector(3)`. Troque as três dimensões pelas exigidas pelo seu modelo de embeddings mediante uma nova migração. O downgrade remove a tabela e preserva a extensão para não afetar outros consumidores.

Após alterar um modelo, gere uma revisão usando a configuração de desenvolvimento (o arquivo será escrito no host):

```bash
docker compose -f compose.yaml -f compose.dev.yaml run --rm migrate alembic revision --autogenerate -m "descreve a alteração"
# Revise o arquivo gerado antes de aplicá-lo.
docker compose -f compose.yaml -f compose.dev.yaml run --rm migrate alembic upgrade head
docker compose -f compose.yaml -f compose.dev.yaml run --rm migrate alembic current
docker compose -f compose.yaml -f compose.dev.yaml run --rm migrate alembic check
```

Para distribuir alterações, reconstrua a imagem com as revisões incluídas e execute `docker compose up -d --build --wait`. Não use `Base.metadata.create_all()` para substituir migrações. Mudanças em extensões precisam de operações explícitas no Alembic; autogenerate não cria `CREATE EXTENSION` automaticamente.

Exemplo de busca com SQLAlchemy:

```python
from sqlalchemy import select
from app.models import Document

statement = (
    select(Document)
    .where(Document.embedding.is_not(None))
    .order_by(Document.embedding.cosine_distance([1.0, 2.0, 3.0]))
    .limit(5)
)
documents = (await session.scalars(statement)).all()
```

## Validação

Com o ambiente ativo:

```bash
docker compose exec -T api python < tests/smoke.py
docker compose run --rm migrate alembic check
```

O teste verifica HTTP, migração aplicada e inserção/leitura/distância vetorial usando o ORM. Os dados de teste são revertidos ao final.

## Uso fora do desenvolvimento

A configuração base não monta código e não publica a porta do banco. A API fica em loopback; para acesso externo configure um proxy com HTTPS. Configure backups do volume e segredos conforme o ambiente. O usuário definido por `POSTGRES_USER` na imagem oficial tem privilégios administrativos; em produção, use uma credencial para migrações e outra com privilégios limitados para a API. As migrações devem rodar uma vez por implantação, antes da atualização das réplicas.

Referências: [FastAPI em Docker](https://fastapi.tiangolo.com/deployment/docker/), [SQLAlchemy assíncrono](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html), [Alembic assíncrono](https://alembic.sqlalchemy.org/en/latest/cookbook.html#using-asyncio-with-alembic), [pgvector](https://github.com/pgvector/pgvector) e [ordem de inicialização no Compose](https://docs.docker.com/compose/how-tos/startup-order/).
