# Princípios arquiteturais

[Voltar ao índice](../../AGENTS.md)

Existe uma decisão que considero importante para a qualidade final desse projeto:

Não transforme o LLM no responsável por tudo.

Uma arquitetura mais confiável será aquela em que cada componente tenha uma função bem delimitada:

- O parser entende o diff.
- A análise estática encontra problemas determinísticos.
- O RAG recupera conhecimento.
- O LLM interpreta o contexto e propõe achados.
- O validador verifica a consistência.
- O avaliador mede a qualidade do sistema.

Essa separação permitirá evoluir cada componente sem precisar reescrever toda a aplicação.

Também recomendo que o primeiro objetivo técnico seja demonstrar um fluxo completo, ainda que simples, antes de investir em funcionalidades sofisticadas.
