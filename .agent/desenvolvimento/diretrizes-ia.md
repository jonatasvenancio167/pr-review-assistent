# Diretrizes para o desenvolvimento com IA

[Voltar ao índice](../../AGENTS.md)

Quero destacar uma parte que considero especialmente importante para o projeto: como outras ferramentas de IA deverão trabalhar com esse código.

Como você pretende utilizar ferramentas de desenvolvimento assistido por IA, recomendo estabelecer algumas regras permanentes:

1. Antes de implementar qualquer funcionalidade, analisar a arquitetura existente.
2. Não criar serviços com responsabilidades duplicadas.
3. Não colocar regras de negócio nas rotas da API.
4. Não permitir acesso direto ao banco pelos Service Objects.
5. Utilizar injeção de dependência.
6. Criar testes para cada nova regra de negócio.
7. Não adicionar dependências sem justificativa técnica.
8. Não introduzir frameworks de agentes sem necessidade.
9. Não modificar contratos existentes sem avaliar os impactos.
10. A cada desenvolvimento ou alteração de uma feature, revisar e atualizar o `AGENTS.md` e os documentos relacionados em `.agent/`, conforme a regra de atualização obrigatória do arquivo principal. Concluir essa atualização junto com a implementação, mantendo a documentação alinhada ao estado atual do projeto.
11. Ao criar commits, seguir as [boas práticas de commits](../commits/boas-praticas.md), mantendo cada alteração lógica junto de seus testes e validando o trabalho antes de registrá-lo.

## Evolução futura da documentação

A documentação atual está organizada em `.agent/`, com índice no `AGENTS.md` da raiz. A estrutura abaixo é uma proposta futura para documentação complementar e registros de decisões arquiteturais (ADRs):

```text
docs/
├── PROJECT_SCOPE.md
├── ARCHITECTURE.md
├── BUSINESS_RULES.md
├── DATABASE.md
├── RAG_PIPELINE.md
├── TESTING_STRATEGY.md
└── ADR/
    ├── 001-service-objects.md
    ├── 002-postgresql-pgvector.md
    └── 003-llm-provider.md

AGENTS.md
README.md
```

O AGENTS.md servirá como instrução operacional para agentes de programação. Os documentos em `.agent/` são a referência detalhada atual do projeto; a proposta de `docs/` acima poderá ser avaliada futuramente.
