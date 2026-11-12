# Segurança e tratamento de riscos

[Voltar ao índice](../../AGENTS.md)

O sistema trabalhará com código-fonte, que pode conter informações privadas ou instruções maliciosas.

Precisamos considerar:

1. Não executar código recebido.
2. Não permitir que o conteúdo do diff altere as instruções do sistema.
3. Tratar documentos recuperados como dados não confiáveis.
4. Não expor chaves de API.
5. Não armazenar credenciais presentes acidentalmente no código.
6. Limitar o tamanho dos diffs e do contexto.
7. Definir políticas de retenção dos dados.
8. Não enviar código privado a serviços externos sem autorização.

Um risco específico merece atenção: Prompt Injection. Um desenvolvedor pode, intencionalmente ou não, enviar um código contendo comentários como "ignore todas as instruções anteriores".

O modelo deverá receber instruções explícitas para tratar o conteúdo analisado exclusivamente como dado de entrada.
