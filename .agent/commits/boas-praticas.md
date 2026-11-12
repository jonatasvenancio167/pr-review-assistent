# Boas Práticas

## Commits

* Cada commit deve conter uma **alteração lógica única**.
    * Não faça diversas alterações lógicas em um único commit como corrigir um bug e implementar uma nova funcionalidade, por exemplo. Neste caso, prefira criar commits separados.
* Não separe uma **alteração lógica única** em vários commits.
    * A implementação de uma funcionalidade e os seus testes devem estar em um mesmo commit, por exemplo.
* Realize o commit **o quanto antes** e **frequentemente**.
    * Esta prática traz vantagens como:
        1. manter os commits pequenos
        2. manter os commits de coisas relacionadas
        3. permitir que seu código seja compartilhado com frequência (em desenvolvimento colaborativo ou times)
        4. facilitar a integração e evitar conflitos de merge (em desenvolvimento colaborativo ou times)
        5. commits grandes dificulta entender o que foi feito e a resolução de possíveis conflitos de merge
        6. pequenos commits são mais fáceis de entender e o rollback pode ser feito com mais facilidade
* Os commits devem ser **ordenados logicamente**.
    * Se o commit A depende de alterações do commit B, então o commit B deve vir antes do commit A no *histórico de commits*.
* Não realize o commit de **trabalhos pela metade**.
    * Porém, não faça o commit de uma funcionalidade inteira em apenas um commit.
    * Quebre a implementação de uma funcionalidade em *pedaços menores* e lembre-se de realizar um commit *o quanto antes* e *frequentemente*.
    * Não realize o commit apenas para *limpar* a sua área de trabalho (use `git stash` para isso) ou para *ter algo* no repositório após um dia de trabalho.
* Faça **testes** antes de realizar o commit.
    * Resista a tentação de realizar um commit de algo que "ache" que está concluído.
    * Realize os testes para se certificar de que tudo está *funcionando corretamente*, principalmente se o código for compartilhado.
* O controle de versão não é uma **ferramenta de backup**.
    * Ter o *backup do código* é um benefício de se ter um sistema de controle de versão.
    * Preste atenção ao criar seus commits, faça isso de maneira *semântica* e que cada commit seja de *coisas relacionadas*.
* Escreva **ótimas mensagens** de commit.
    * Use o *editor* para escrever as mensagens de commit. Ao utilizar o *terminal* para isso, o resultado será uma *mensagem curta*, *não informativa* e *ambígua*.
    * A mensagem deverá conter um *título* *descritivo* porém *sucinto*. Recomenda-se não ultrapassar *50 caracteres*. Deve começar com *maiúscula*, estar no *modo imperativo* e não deve terminar com *ponto final*.
    * Uma *linha em branco* separa o *título* da *descrição*.
    * A *descrição* deve ter no máximo *72 caracteres* por linha, explicar o *porquê* a alteração é necessária, *como* foi realizada e os *efeitos colaterais* resultantes da alteração.
    * Ao escrever uma *mensagem de commit* pense no que você *precisará saber* meses depois.
    * Se a solução de um commit A depende de um commit B a *dependência* deve-se sinalizada na mensagem do commit A.
    * Se um *problema resolvido* no commit A corrige um erro introduzido no commit B deve-se sinalizar na mensagem do commit A.
```
Pequeno resumo das alterações (até 50 caracteres)

Texto mais detalhado sobre explicando as alterações em até
72 caracteres e no modo imperativo. Deve-se explicar as motivações
da alteração, como a alteração foi realizada e os efeitos colaterais
resultantes da alteração.

Outros parágrafos vem após linhas em branco.

- Itens são permitidos

- Eles devem ser separados por uma linha em branco

- E devem utilizar asteriscos ou traços para identificá-los
```