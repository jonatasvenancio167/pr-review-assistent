# Estrutura de diretórios

[Voltar ao índice](../../AGENTS.md)

```text
python-ai-code-review/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── schemas/
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── exceptions.py
│   │
│   ├── domain/
│   │   ├── entities/
│   │   └── enums/
│   │
│   ├── services/
│   │   ├── review_orchestrator.py
│   │   ├── code_analysis_service.py
│   │   ├── llm_review_service.py
│   │   ├── finding_validation_service.py
│   │   ├── report_service.py
│   │   │
│   │   └── rag/
│   │       ├── document_ingestion_service.py
│   │       ├── chunking_service.py
│   │       ├── embedding_service.py
│   │       └── retrieval_service.py
│   │
│   ├── repositories/
│   │   ├── knowledge_repository.py
│   │   └── review_repository.py
│   │
│   ├── integrations/
│   │   ├── llm/
│   │   ├── embeddings/
│   │   └── git/
│   │
│   ├── dependencies.py
│   └── main.py
│
├── knowledge/
│   └── coding_standards/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── evaluation/
│
├── migrations/
├── Dockerfile
├── compose.yaml
├── pyproject.toml
└── README.md
```

Essa estrutura é a arquitetura-alvo. O projeto atual já possui parte dessa organização; não precisamos criar todos os módulos imediatos
