Title: Planilha para preenchimento do SIOPS
Date: 2016-03-16 08:18
Status: published
Category: Material
Tags: SIOPS, ferramentas
Summary: Nesta planilha do Excel você vai digitar os valores de receitas, despesas e saldos financeiros (na aba DADOS e vai imprimir as demais planilhas que são as "auxiliares" para preenchimento do SIOPS.

Se você que está lendo isto chegou até aqui, é porque sebe exatamente o que é o SIOPS, não é? (Se não sabe, [descubra aqui](http://siops.datasus.gov.br))

Por isso não vou "espichar a conversa" além do necessário, pois quero compartilhar com vocês uma planilha para facilitar o preenchimento do SIOPS, especificamente das pastas Despesas por Fonte e RP e a Execução Financeira por Blocos.

Nesta planilha do Excel você vai digitar os valores de receitas, despesas e saldos financeiros (na aba DADOS e vai imprimir as demais planilhas que são as "auxiliares" para preenchimento do SIOPS.

Na aba DADOS temos várias colunas que terão as informações a serem consolidadas:

- Coluna ESFERA: Recebe os valores 1FEDERAL, 2ESTADUAL ou 3MUNICIPAL, para identificar a origem das receitas da Execução por Blocos. Os números antes do texto são para ordenação nas abas seguintes.
- Coluna RV: É o "núcleo" da planilha. Nela você vai colocar os códigos das fontes de recursos (ou vínculos, ou recursos vinculados). Também colocará os códigos dos projetos/atividades (na planilha começam com P) para informação dos valores da fonte 0040 ASPS (mais explicações sobre isso no decorrer do texto).
- Coluna BLOCO: Especifica a qual bloco se refere a linha;
- Coluna COMPONENTE: Especifica o componente a qual a linha se refere.
- Coluna FONTE: Identifica se a linha se refere a Transferências do SUS, a Impostos ou a outra fonte conforme consta na Pasta Despesa por Fonte e RP do SIOPS.
- Demais colunas são autoexplicativas.

Como você vai observar na planilha com dados de exemplo, na coluna RV tem dois tipos de valores: os numéricos que correspondem a fontes de recursos (vínculos) e outros valores no formato P#### onde #### representa o código de projeto/atividade.

Nas linhas onde RV representa um vínculo, você vai preencher cada coluna com os valores daquele vínculo.

Já, nas linhas P####, você vai preencher com os valores referentes ao projeto ou atividade indicado pelo número ####, mas apenas naquilo que se refere à fonte 00040 ASPS.

Também há uma linha para a fonte 0040 ASPS. Nela você NÃO vai preencher os campos com cor de fundo preta.

Se você observar, na linha P2089, tem algumas células com fundo rpeto também. Isso ocorre porque no orçamento de meu município existia a atividade 2.089 realtiva a um contrato de rateio com consórcio público. Assim, eu não podia preencher os valores de empenhado, liquidado e pago para fechar o SIOPS.

Outra observação importante é a de que você deve vincular atentamente cada linha ao bloco, componete e fonte corretos para que tudo funcione. Os dados digitados na planilha são os de meu município e servem de exemplo. Você vai ter que adaptar de acordo com a sua realidade.

Bom, estas foram as orientações gerais para a utilização desta planilha, sempre lembrando que após digitar qualquer valor em DADOS, as demais abas devem ser atualizadas, pois se tratam de tabelas dinâmicas.

Clique no link para baixar a planilha:

[planilha-siops_v1.xlsx]({filename}/files/planilha-siops_v1.xlsx)
