# Escopo funcional

[Voltar ao índice](../../AGENTS.md)

Aqui precisamos separar o que o sistema deverá fazer do que ficará para versões futuras.

## Funcionalidades incluídas no MVP

| ID | Funcionalidade | Descrição |
| --- | --- | --- |
| RF-01 | Receber diff | Receber alterações de código por API |
| RF-02 | Processar diff | Identificar arquivos e linhas adicionadas |
| RF-03 | Análise estática | Executar verificações determinísticas |
| RF-04 | Ingestão de conhecimento | Importar documentos técnicos |
| RF-05 | Chunking | Dividir documentos em fragmentos |
| RF-06 | Embeddings | Gerar representações vetoriais |
| RF-07 | Retrieval | Recuperar conhecimento relevante |
| RF-08 | Revisão com IA | Enviar contexto ao LLM |
| RF-09 | Validar achados | Verificar estrutura e evidências |
| RF-10 | Gerar relatório | Retornar os resultados estruturados |

## Funcionalidades fora do MVP

- Integração direta com GitHub
- Revisão automática de Pull Requests.
- Comentários automáticos em repositórios
- Correção automática de código
- Criação de commits
- Suporte a Ruby, JavaScript, Java e outras linguagens.
- Execução de agentes autônomos
- Treinamento de modelos próprios
- Interface web administrativa

Essas funcionalidades poderão ser consideradas em versões futuras, depois que o pipeline principal estiver validado.
