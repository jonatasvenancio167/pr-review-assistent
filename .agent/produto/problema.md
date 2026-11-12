# Problema e abordagem

[Voltar ao índice](../../AGENTS.md)

O processo tradicional de Code Review depende significativamente da experiência dos desenvolvedores responsáveis pela revisão.

Em equipes de desenvolvimento, alguns problemas são recorrentes:

- Identificação inconsistente de problemas de qualidade de código.
- Falta de padronização nas revisões
- Dificuldade em compartilhar e aplicar boas práticas de engenharia.
- Revisões manuais demoradas.
- Problemas de segurança e performance que podem passar despercebidos.
- Recomendações sem justificativa técnica ou contexto suficiente.

Além disso, ferramentas tradicionais de análise estática possuem limitações para interpretar determinadas situações que dependem de contexto de negócio, decisões arquiteturais ou relações entre diferentes trechos de código.

O projeto pretende explorar a combinação de três abordagens:

1. <strong>Análise estática:</strong> identificação de problemas por regras determinísticas.
2. <strong>RAG:</strong> recuperação de conhecimento técnico relevante para a alteração analisada.
3. <strong>LLM:</strong> interpretação contextual do código e geração de recomendações.

O diferencial pretendido é produzir revisões contextualizadas, rastreáveis e fundamentadas, em vez de simplesmente solicitar ao modelo que avalie um trecho de código.
