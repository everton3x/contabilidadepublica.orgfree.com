Title: Conversor PAD : um conversor de leiaute para os arquivos do SIAPC/PAD do TCE/RS
Date: 2016-04-18 13:56
Status: published
Category: Material
Tags: PAD, ferramentas, TCE/RS
Summary:A ferramenta Conversor PAD é um conversor de leiaute para os arquivos de dados gerados para o Programa Autenticador de Dados (PAD) do sistema SIAPC do TCE/RS.

A ferramenta Conversor PAD é um conversor de leiaute para os arquivos de dados gerados para o Programa Autenticador de Dados (PAD) do sistema SIAPC do TCE/RS.

Ele converte os “txt do PAD” em arquivos CSV que são compatíveis com softwares de planilhas eletrônicas, como o Excel, por exemplo.


Além de converter os dados do leiaute de colunas com largura fixa para colunas separadas por ponto-e-vírgula, ele também faz conversões para os campos de data, moeda e outros, tais como códigos de receita, despesa e contábil.

O Conversor PAD é gratuito e distribuído sob a licença [Creative Commons Atribuição 3.0 Brasil](https://creativecommons.org/licenses/by/3.0/br/).

# Instalação

A instalação do Conversor PAD é simples, bastando executar o instalador que irá descompactar a pasta ConversorPAD no local de instalação.

O Conversor PAD foi desenvolvido no Windows 10 e testado nele, porém, virtualmente é possível executar em qualquer outra versão do Windows desde que acima do Windows Vista, ou seja, no Windows Vista, no Windows 7, no Windows 8 e 8.1 e no Windows 10.

Também é virtualmente possível o conversor funcionar no Linux, já que ele é desenvolvido inteiramente com PHP 7.

É recomendável que o local de instalação seja a pasta raiz de alguma partição, como C:, ou D:. Embora a ferramenta possa funcionar em outros caminhos de instalação, ela é desenvolvida no caminho C:ConversorPAD, por isso, instalar em outros locais pode ocasionar, mesmo que eventualmente, falhas na conversão.

# Utilizando o Conversor PAD

## Escolhendo os arquivos txt do PAD para converter

Coloque os txt do PAD na pasta “input”. A ferramenta apenas irá converter os arquivos que estiverem dentro da pasta “input”.

Por exemplo: se quiser converter apenas o bal_desp.txt, é esse arquivo que você vai colocar dentro de “input”.
Coloque ali os arquivos, e não o atalho para eles.

## Inicie a conversão

Execute o arquivo convert2csv.bat (note que a extensão .bat pode não aparecer para você, dependendo das configurações de opções de pasta do Windows).

Para executar convert2csv.bat, basta dar dois cliques no arquivo ou selecionar ele e pressionar ENTER.

A partir daí, aparecerá uma tela do prompt de comando do Windows. Nessa tela você irá acompanhar a conversão. Também aparecerão os erros, se ocorrerem.

## Verificando o resultado da conversão

Ao final da conversão, se tudo ocorreu bem, na pasta “output” estarão os arquivos convertidos.

A conversão irá criar um arquivo CSV, para cada arquivo txt do PAD que existe dentro da pasta “input”. Se algum arquivo não for convertido, não será criado um arquivo CSV.

Lembre-se que, dependendo das configurações do Windows, a extensão .csv poderá não aparecer.

Ao abrir o arquivo convertido, você terá na primeira linha da planilha o cabeçalho das colunas. Nas demais linhas, os dados do txt convertidos.

Para aprender mais sobre o formato de arquivo CSV, consulte a [Wikipédia](https://pt.wikipedia.org/wiki/Comma-separated_values).

Lembre-se de mover ou copiar os arquivos convertidos para outra pasta, já que a cada nova conversão, os arquivos convertidos anteriores são apagados.

## Como obter suporte

Por se tratar de um trabalho voluntário, não há, evidentemente garantia de suporte.

O conversor foi desenvolvido para uso pessoal do desenvolvedor, que é contador público de um município do Rio Grande do Sul. Desta forma, eventuais erros e problemas serão resolvidos pela utilização pessoal dele. Problemas enfrentados pelos demais usuários poderão ser relatadas nos comentários desta página.

Maiores detalhes sobre instalação e utilização, consulte o arquivo Ajuda.doc dentro da pasta "ConversorPADdoc".

## Baixando o instalador

[Instalador para Windows (PHP 7 incluso)]({filename}/files/ConversorPAD_v16.04.18.0.exe)
[Arquivos compactados para Linux (PHP 7 não incluso)]({filename}/files/ConversorPAD_v16.04.18.0.7z)
