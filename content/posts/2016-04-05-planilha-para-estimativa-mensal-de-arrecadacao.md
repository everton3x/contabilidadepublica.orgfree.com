Title: Planilha para estimativa mensal de arrecadação
Date: 2016-04-05 19:00
Status: published
Category: Material
Tags: orçamento, ferramentas, estimativa de arrecadação
Summary: Quem trabalha com a elaboração do orçamento e a sua avaliação sabe que são necessárias estimativas mensais de arrecadação para a definição e avaliação da programação financeira.

Quem trabalha com a elaboração do orçamento e a sua avaliação sabe que são necessárias estimativas mensais de arrecadação para a definição e avaliação da programação financeira.

Eu costumo fazer a previsão da receita orçamentária de forma manual, já que isso me dá total controle do cálculo e não me faz esperar por ajustes de sistema quando algo está errado.

Alguns sistemas informatizados tem funcionalidades mais elaboradas para o rateio mensal da previsão da receita, enquanto que outros trabalham simplesmente com um valor médio mensal.

Grande parte das receitas tem uma característica de sazonalidade na distribuição mensal da arrecadação, inclusive as receitas mais relevantes no âmbito municipal, tais como o FPM e o ICMS. Pensando nisso (e atendendo a uma necessidade minha), desenvolvi uma planilha no Excel para distribuição mensal da previsão da receita, de forma automática de acordo com a sazonalidade média.

Na planilha existem várias guias,c ada uma com uma função, porém três delas são de importância para o usuário, a saber:

- Guia Receitas: nela são cadastrados os códigos e nomes das receitas, a fonte de recursos e os valores previstos para o ano;
- Guia Arrecadação: onde se registra a arrecadação mensal dos anos que serão base para o cálculo da sazonalidade;
- Guia Previsão Mensal: mostra os valores previstos mensais de acordo com a sazonalidade média ajustada.

## Instruções de uso e descrição do funcionamento

Primeiramente, o usuário deve preencher a guia Receitas, colocando o código da receita, a sua descrição, o código da fonte de recursos e o valor previsto para o ano que se deseja a meta mensal de arrecadação.

Os campos Código, Receita e Fonte são indicativos, ou seja, em Código, pode-se colocar o código da natureza da receita, ou um código de acesso ou outro qualquer, desde que seja único e identifique a receita desejada.

O campo Receita serve para colocar o nome da receita, não necessariamente a descrição constante no elenco de contas.

O mesmo se observa para Fonte, que se destina apenas para se fazer algum tipo de filtro ou agrupamento. Se quiser, pode deixar em branco que não haverá influência no resultado.

Uma observação importante para o campo Código: ele é referência nas demais guias: isso quer dizer que no campo Código das outras quias, deve-se incluir os mesmos valores dos informados na guia Receitas.

Depois de preencher a guia Receitas, o usuário deve preencher a guia Arrecadação, informando no campo Código o código da receita, em Ano, o ano da arrecadação e nos campos relativos aos meses, o valor arrecadado em cada mês.

Deve-se preencher tantos anos quanto se queira trabalhar, por exemplo, três anos, cinco anos, etc.

Caso seja necessário, deve-se preencher as demais colunas com as fórmulas, como se faria numa planilha normal.

Feito isso, agora todo o trabalho é por conta do sistema.

Na quia Sazonalidade, é feito o cálculo do percentual arrecadado em cada mês em relação ao total arrecadado, por ano e por receita.

Na guia Sazonalidade Média, o Excel calculará a sazonalidade mensal média para cada mês em cada receita.

Um dos efeitos da média com percentuais é que às vezes a soma dos percentuais médios corresponde a um valor diferente de 100%. Esse efeito é corrigido na guia Sazonalidade Corrigida.

Por fim, o Excel calculará com base na sazonalidade corrigida e no valor anual previsto o quanto cabe a cada mês, por receita. Isso é feito na guia Previsão Mensal.

O usuário deve ter o cuidado de preencher as linhas e colunas das guias com as fórmulas, caso o número de linhas com receitas informadas seja superior ao número de linhas contempladas nas guias. Isso é feito apenas copiando a linha superior de cada guia para a linha seguinte.

Além disso, na planilha, as colunas em que se deve digitar algo tem o cabeçalho sombreado em cinza, para facilitar a localização das informações digitadas. O resto são fórmulas.

[Baixe a planilha de rateio mensal de previsão de receitas]({filename}/files/previsao-mensal-receitas.xlsx)
