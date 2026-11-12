# Estratégia de testes e avaliação

[Voltar ao índice](../../AGENTS.md)

Não podemos avaliar o projeto apenas pela quantidade de testes automatizados.

Precisamos avaliar também a qualidade das revisões geradas pela IA.

Testes unitários

- Parsing do Git Diff.
- Extração de linhas adicionadas.
- Geração de embeddings.
- Recuperação de documentos.
- Validação dos achados.
- Comportamento do orquestrador.

Testes de integração

- PostgreSQL e pgvector.
- Repositórios.
- API do LLM.
- API de embeddings.
- Fluxo completo de revisão.

Testes de avaliação de IA
Vamos construir um conjunto de diffs com problemas conhecidos e resultados esperados.

Algumas métricas importantes:

| Métrica | Objetivo |
| --- | --- |
| Precision | Medir quantos achados reportados são relevantes |
| Recall | Medir quantos problemas conhecidos foram identificados |
| False Positive Rate | Identificar apontamentos incorretos |
| Retrieval Relevance | Medir a qualidade dos documentos recuperados |
| Latency | Medir o tempo de execução |
| Cost per Review | Medir o custo médio por revisão |

Essa etapa será importante para comparar diferentes modelos, prompts e estratégias de retrieval.
