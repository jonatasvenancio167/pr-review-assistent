# Roadmap de desenvolvimento

[Voltar ao índice](../../AGENTS.md)

Organizaria a implementação em seis fases.

Fase 1 — Fundação
Estrutura inicial criada

- FastAPI e Pydantic.
- Service Objects.
- Orquestrador.
- Contratos de entrada e saída.
- Testes iniciais.

Fase 2 — Persistência

- PostgreSQL.
- Docker Compose.
- SQLAlchemy.
- Alembic.
- pgvector.

Fase 3 — RAG

- Ingestão.
- Chunking.
- Embeddings.
- Retrieval.
- Testes de recuperação.

Fase 4 — Integração com LLM

- Adaptador de API.
- Prompt estruturado.
- Geração de achados.
- Validação das respostas.

Fase 5 — Qualidade

- Dataset de avaliação.
- Métricas.
- Segurança.
- Observabilidade.
- Otimizações.

Fase 6 — Evolução

- Integração GitHub.
- Pull Requests.
- Comentários automáticos.
- Suporte a outras linguagens.
