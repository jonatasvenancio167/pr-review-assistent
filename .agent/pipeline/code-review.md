# Pipeline de Code Review

[Voltar ao índice](../../AGENTS.md)

Essa é uma das partes mais importantes da especificação.

O pipeline deve seguir uma sequência previsível de processamento

## Etapa 1 - recebimento

O desenvolvedor envia uma requisição contendo:

- Identificação do repositório.
- Commit associado, opcional.
- Git Diff.

## Etapa 2 — Análise do diff

O CodeAnalysisService deverá:

- Interpretar o formato unificado do Git Diff.
- Identificar arquivos modificados.
- Identificar linhas adicionadas.
- Preservar a numeração original das linhas.
- Identificar a linguagem do arquivo.
- Preparar o contexto para as próximas etapas.

Uma observação importante: não devemos trabalhar apenas com uma lista de linhas adicionadas. Precisamos preservar o caminho do arquivo, os hunk headers (@@) e os números reais das linhas de destino. Isso será fundamental para apontamentos precisos.

## Etapa 3 — Recuperação de conhecimento

O RetrievalService receberá o contexto da alteração e consultará a base de conhecimento.

Exemplo:

Se o código apresentar uma consulta SQL dinâmica, o sistema deverá recuperar documentos relacionados a:

- SQL Injection.
- Consultas parametrizadas.
- Segurança em acesso a banco de dados.
- Boas práticas de acesso a dados em Python.

## Etapa 4 - Análise com LLM

O LLMReviewService receberá:

1. O diff original.
2. O contexto das alterações.
3. Os documentos recuperados.
4. As instruções de revisão.
5. O formato esperado da resposta.

O modelo deverá retornar achados estruturados, evitando recomendações genéricas ou problemas sem evidência.

## Etapa 5 — Validação

O FindingValidationService deverá verificar:

- Existência da evidência.
- Correspondência com as linhas analisadas.
- Validade da severidade.
- Presença dos campos obrigatórios.
- Duplicidade dos apontamentos.

## Etapa 6 — Relatório

O ReportService organizará os resultados e devolverá uma resposta padronizada.
