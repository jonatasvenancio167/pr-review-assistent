# Visão do produto

[Voltar ao índice](../../AGENTS.md)

O Python AI Code Review será uma ferramenta de apoio à revisão de código.

O desenvolvedor fornecerá um Git Diff contendo as alterações realizadas em um projeto Python. O sistema processará essas alterações, consultará sua base de conhecimento e utilizará um modelo de IA para identificar possíveis problemas.

Ao final, o sistema apresentará um relatório contendo:

- Problema identificada
- Arquivo e linha afetados, quando determináveis
- Classificação de severidade
- Categoria do problema.
- Evidência encontrada no código
- Explicação técnica
- Sugestão de melhoria
- Referência à regra ou documentação recuperada, quando aplicável.

<strong>Principio fundamental:</strong> a IA deve atuar como assistente de revisão, não como autoridade absoluta sobre a qualidade do código.
