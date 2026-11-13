# Desenvolvimento da aplicação para auxiliar code review

Sistema de apoio ao Code Review de alterações Python, com entrada em Git Diff, arquitetura baseada em Service Objects, análise estática, RAG e LLM. O objetivo é aprendizado técnico.

## Instruções de leitura

A especificação foi dividida por tópicos em [`.agent/`](.agent/). Os documentos vinculados abaixo complementam as instruções deste arquivo.

Antes de implementar uma funcionalidade, leia as [diretrizes de desenvolvimento com IA](.agent/desenvolvimento/diretrizes-ia.md), as [regras de negócio](.agent/regras/regras-de-negocio.md), as [orientações de segurança](.agent/seguranca/riscos.md) e o [escopo funcional](.agent/produto/escopo-funcional.md). Consulte também os tópicos relacionados à alteração.

Analise a arquitetura existente, preserve a separação de responsabilidades e atualize a documentação quando houver mudanças arquiteturais. A IA atua como assistente de revisão. Nunca execute o código submetido para análise.

## Atualização obrigatória da documentação

A cada desenvolvimento ou alteração de uma feature, revise e atualize este `AGENTS.md` e os documentos relacionados em `.agent/`, mantendo as instruções, o índice e a especificação alinhados ao estado atual do projeto. Registre nos tópicos correspondentes as mudanças de comportamento, contratos, regras de negócio, arquitetura, decisões técnicas e testes, conforme aplicável.

A atualização da documentação faz parte da entrega da feature e deve ser concluída junto com a implementação. Remova ou corrija informações desatualizadas e mantenha os links válidos.

## Estado atual do desenvolvimento

A API disponibiliza healthchecks e documentação HTTP. A rota
`POST /reviews` está temporariamente desativada (HTTP 404 e ausente do
OpenAPI), pois seus serviços ainda não estão implementados. Seus arquivos
estão preservados para evolução posterior. O teste de inicialização executa
Uvicorn sem exigir PostgreSQL; readiness continua dependendo de PostgreSQL
com pgvector.

O parser interpreta um único bloco de diff, com adições, remoções e
validação das contagens do cabeçalho. Consulte o [pipeline de Code
Review](.agent/pipeline/code-review.md) para os limites atuais e o fluxo
previsto para o MVP.

## Índice por tópico

| Documento | Conteúdo |
| --- | --- |
| [Boas práticas de commits](.agent/commits/boas-praticas.md) | Agrupamento lógico, validação e mensagens de commits. |
| [Contexto e escopo](.agent/produto/contexto.md) | Tecnologias, entrada e objetivo educacional. |
| [Problema e abordagem](.agent/produto/problema.md) | Problemas das revisões e combinação de análise estática, RAG e LLM. |
| [Visão do produto](.agent/produto/visao.md) | Fluxo de uso e conteúdo do relatório. |
| [Objetivos do projeto](.agent/produto/objetivos.md) | Objetivo geral e objetivos específicos. |
| [Escopo funcional](.agent/produto/escopo-funcional.md) | Funcionalidades incluídas e excluídas do MVP. |
| [Arquitetura e responsabilidades](.agent/arquitetura/camadas.md) | Service Objects e responsabilidades de cada camada. |
| [Estrutura de diretórios](.agent/arquitetura/diretorios.md) | Organização de diretórios prevista para a aplicação. |
| [Pipeline de Code Review](.agent/pipeline/code-review.md) | Recebimento, análise, recuperação, LLM, validação e relatório. |
| [Regras de negócio](.agent/regras/regras-de-negocio.md) | Regras RN-01 a RN-14. |
| [Classificação dos achados](.agent/regras/severidades.md) | Severidades controladas e critérios de classificação. |
| [Categorias de revisão](.agent/regras/categorias.md) | Categorias dos achados e relação com severidade. |
| [Base de conhecimento e fontes](.agent/rag/fontes.md) | Fontes técnicas, organização e versões de referência. |
| [Pipeline de ingestão](.agent/rag/ingestao.md) | Diagrama de ingestão e metadados dos fragmentos. |
| [Estratégia de recuperação](.agent/rag/recuperacao.md) | Critérios de retrieval e evolução para busca híbrida. |
| [Modelo de dados conceitual](.agent/dados/modelo-conceitual.md) | Entidades, campos, relacionamentos e persistência inicial. |
| [Requisitos não funcionais](.agent/qualidade/requisitos-nao-funcionais.md) | Requisitos RNF-01 a RNF-10. |
| [Estratégia de testes e avaliação](.agent/qualidade/testes-e-avaliacao.md) | Testes unitários, integração, avaliação de IA e métricas. |
| [Segurança e tratamento de riscos](.agent/seguranca/riscos.md) | Proteção de código, credenciais, limites e prompt injection. |
| [Roadmap de desenvolvimento](.agent/planejamento/roadmap.md) | Seis fases de implementação e evolução. |
| [Critérios de aceite do MVP](.agent/planejamento/criterios-de-aceite.md) | Checklist para validação do MVP. |
| [Decisões técnicas](.agent/planejamento/decisoes-tecnicas.md) | Escolhas definidas e decisões ainda pendentes. |
| [Diretrizes para o desenvolvimento com IA](.agent/desenvolvimento/diretrizes-ia.md) | Regras operacionais para agentes e evolução da documentação. |
| [Princípios arquiteturais](.agent/arquitetura/principios.md) | Limites de cada componente e prioridade ao fluxo completo inicial. |
