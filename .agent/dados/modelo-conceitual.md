# Modelo de dados conceitual

[Voltar ao índice](../../AGENTS.md)

A princípio, teremos quatro entidades principais:

<table>
  <tr>
    <td>
      <strong>CodeReview</strong>
      <p>Representa uma revisão realizada.</p>
      <p>ID, repository, commit_sha, status, diff_hash, created_at</p>
    </td>
  </tr>
  <tr>
    <td>
      <strong>ReviewFinding</strong>
      <p>Representa um problema identificado.</p>
      <p>ID, review_id, title, severity, category, evidence, recommendation, line_number</p>
    </td>
  </tr>
  <tr>
    <td>
      <strong>KnowledgeDocument</strong>
      <p>Representa um documento técnico ingerido.</p>
      <p>ID, title, source, language, category, version, content_hash</p>
    </td>
  </tr>
  <tr>
    <td>
      <strong>KnowledgeChunk</strong>
      <p>Representa um fragmento de documento com seu embedding.</p>
      <p>ID, document_id, content, chunk_index, embedding, metadata</p>
    </td>
  </tr>
</table>

Relacionamentos principais:

![Relacionamento Principais](../../assets/relacionamentos-principais.png)

Uma decisão importante: para o MVP educacional, podemos persistir inicialmente apenas a base de conhecimento e os fragmentos. O histórico completo das revisões pode ser implementado depois, caso o objetivo de aprendizagem exija essa persistência.
