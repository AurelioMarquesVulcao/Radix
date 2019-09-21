# Desafio Radix
<h3>.</h3>

![](Pics/ideasvtion.jpg)
![](headvdvder01.png)

## Regras Gerais

O candidato poderá escolher as seguintes tecnologias para resolução das questões:
1. JAVA
2. C#.NET
3. PYTHON
4. NODE

Em caso de sinalização do RH para que a prova seja feita para uma determinada tecnologia, espera-se que o candidato mantenha aderência ao requerido.


ANÁLISE DE SIMILARIDADE DE CÓDIGOS-FONTE:
Possuimos um banco de respostas em constante atualização para as questões abaixo. O código enviado passará por uma análise de similaridade onde conseguimos, facilamente, identificar se houve ou não cópia de código (sejam pedaços ou inteiros). Seja íntegro e honesto na elaboração de suas respostas.
  
## Questão 1 - Fibonacci Array (1,5 pontos)

Escreva um programa que leia um número inteiro e imprima o número de Fibonacci correspondente a esse número lido. Lembre-se que os primeiros elementos da série de Fibonacci são 0 e 1 e cada termo posterior é calculado a partir da soma dos dois precedentes. Todos os números de Fibonacci calculados neste programa devem caber em um número não assinado de 64 bits.

**********
EXEMPLO:
**********

Entrada: 
- 3
- 0
- 4
- 2

Saída:
- Fib(0) = 0
- Fib(4) = 3
- Fib(2) = 1

**********

ENTRADA: A primeira linha contém um número inteiro T, indicando a quantidade de cenários a serem testados. Cada cenário contém um inteiro N (0 <= N <= 60), correpondendo ao enésimo termo da série de Fibonacci.

SAÍDA: Para cada cenário de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o enésimo termo da série de Fibonacci.


## Questão 2 - Matrizes (1,5 pontos)

Faça um programa para criar uma matriz quadrada, onde todos seus elementos são iguais a 0 (zero) com exceção de sua diagonal principal que deve ser preenchido com o valor 1 (um).

**********
EXEMPLO:
**********

Entrada: 
- 3
- 0
- 4
- 2

Saída:
- Matrix(0x0)
  
- Matrix(4x4)  
  1 0 0 0  
  0 1 0 0  
  0 0 1 0  
  0 0 0 1

- Matrix(2x2)  
  1 0  
  0 1  

**********

ENTRADA: A primeira linha contém um número inteiro T, indicando a quantidade de cenários a serem testados. Cada cenário contém um inteiro N (0 <= N <= 20), correpondendo ao tamanho da matriz N x N.

SAÍDA: Para cada cenário de teste da entrada, imprima a mensagem "Matrix(NxN)" seguida da matriz.

## Questão 3 - Consulta SQL (2,0 pontos)

Faça um relatório sobre os funcionário da Radix que estão registrados no banco de dados a partir dos registros existentes no banco de dados com a seguinte estrutura:

Dados da Tabela 'funcionario':

1. id_funcionario (PK)	    numeric	
2. nome	                    varchar (255)	
3. uf                       char (2)
4. ano_nascimento           numeric

Dados da Tabela 'projeto':

1. id_projeto (PK)	        numeric	
2. nome	                    varchar (255)
3. data_inicio              datetime
4. data_fim                 datetime

Dados da Tabela 'funcionario_projeto':

1. id_funcionario (PK)	    numeric	
2. id_projeto (PK)          numeric	


Seu trabalho, agora é selecionar todos os funcionários que residem no Rio de Janeiro, possuem mais de 20 anos de idade e já trabalharam em mais de 3 projetos finalizados.

**********
EXEMPLO de Tabelas:
**********
<table >
    <thead>
        <tr>
            <th>funcionario</th>
            <th>projeto</th>
            <th>funcionario_projeto</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th>id_funcionario</th>
                            <th>nome</th>
                            <th>uf</th>
                            <th>ano_nascimento</th>
                        </tr>
                    </thead>
                    <tbody>
                            <tr><td>1  </td><td>Funcionário 1  </td><td>RJ</td><td>1991</td></tr>
                            <tr><td>2  </td><td>Funcionário 2  </td><td>RJ</td><td>1989</td></tr>
                            <tr><td>3  </td><td>Funcionário 3  </td><td>SP</td><td>1978</td></tr>
                            <tr><td>14 </td><td>Funcionário 4  </td><td>RJ</td><td>2000</td></tr>
                            <tr><td>15 </td><td>Funcionário 5  </td><td>RJ</td><td>1996</td></tr>
                            <tr><td>21 </td><td>Funcionário 6  </td><td>MG</td><td>1993</td></tr>
                            <tr><td>23 </td><td>Funcionário 9  </td><td>RJ</td><td>1999</td></tr>
                            <tr><td>25 </td><td>Funcionário 10 </td><td>RJ</td><td>1992</td></tr>
                            <tr><td>26 </td><td>Funcionário 13 </td><td>RJ</td><td>1988</td></tr>
                    </tbody>
                </table>
            </td>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th>id_projeto</th>
                            <th>nome</th>
                            <th>data_inicio</th>
                            <th>data_fim</th>
                        </tr>
                    </thead>
                    <tbody>
                            <tr><td>1  </td><td> Projeto 1  </td><td> 01/03/2010 </td><td> 01/09/2010</td></tr>
                            <tr><td>2  </td><td> Projeto 2  </td><td> 01/09/2011 </td><td> 01/09/2012</td></tr>
                            <tr><td>3  </td><td> Projeto 3  </td><td> 01/10/2012 </td><td> 01/02/2013</td></tr>
                            <tr><td>4  </td><td> Projeto 4  </td><td> 01/08/2012 </td><td> 01/03/2014</td></tr>
                            <tr><td>5  </td><td> Projeto 5  </td><td> 01/04/2013 </td><td> 01/12/2014</td></tr>
                            <tr><td>6  </td><td> Projeto 6  </td><td> 01/03/2015 </td><td> 01/09/2016</td></tr>
                            <tr><td>7  </td><td> Projeto 9  </td><td> 01/06/2015 </td><td> 01/09/2017</td></tr>
                            <tr><td>8  </td><td> Projeto 10 </td><td> 01/07/2016 </td><td>           </td></tr>
                            <tr><td>9  </td><td> Projeto 13 </td><td> 01/12/2017 </td><td>           </td></tr>
                    </tbody>
                </table>
            </td>
            <td>
                <table>
                    <thead>
                        <tr>
                            <th>id_funcionario</th>
                            <th>id_projeto</th>
                        </tr>
                    </thead>
                    <tbody>
                            <tr><td>1 </td><td> 2   </td> </tr>
                            <tr><td>1 </td><td> 1   </td> </tr>
                            <tr><td>1 </td><td> 3   </td> </tr>
                            <tr><td>1 </td><td> 4   </td> </tr>
                            <tr><td>2 </td><td> 1   </td> </tr>
                            <tr><td>3 </td><td> 1   </td> </tr>
                            <tr><td>4 </td><td> 1   </td> </tr>
                            <tr><td>3 </td><td> 4   </td> </tr>
                            <tr><td>2 </td><td> 3   </td> </tr>
                    </tbody>
                </table>
            </td>
        </tr>
    </tbody>
</table>

**********

## Questão 4 - Letters Count (2,0 pontos)

Dada uma string S, queremos imprimir a quantidade de ocorrências de cada letra presente na string e retornar a quantidade de ocorrências para um caractere C.

**********
EXEMPLO:
**********

Entrada: 
- 4
- ARARA A
- TORTA F
- URUGUAIANA UR
- PARALELEPIPEDO 1

Saída:
- A(3); R(2)  
  3

- T(2); O(1); R(1); A(1)  
  0

- U(3); R(1); G(1); A(3); I(1); N(1)  
  consulta inválida

- P(3); A(2); R(1); L(2); E(3); I(1); O(1)  
  consulta inválida

**********

ENTRADA: A primeira linha contém um número inteiro T, indicando a quantidade de cenários a serem testados. Cada uma das T subsequentes linhas contém uma string S, onde 0 < len(S) ≤ 100, seguida por um único caractere C que deve pertencer ao intervalo [a, z].

SAÍDA: Para cada cenário de teste da entrada, caso o tamanho desta string seja maior que 1 (um) caracter, imprima a cada letra L encontrada com sua respectiva quantidade de ocorrências N L(N) e em seguida retornar a quantidade de ocorrências para o caractere C. Caso o caractere C não atenda aos requisitos de entrada, deverá retornar "consulta inválida"

## Questão 5 - Palindrome (3,0 pontos)

Um palíndromo é uma string tal que sua reversão é igual à string original. Em outras palavras, é uma string que, quando lida de trás para frente, é igual à string original. Por exemplo, o BANANAB é um palíndromo, enquanto o BANANAS não. Neste problema estamos interessados em um assunto um pouco mais interessante.

Dada uma string S, queremos encontrar a MAIOR subsequência que seja um palíndromo (Strings de 1(um) caracter não serão considerados como palíndromo). Uma subsequência é uma string que pode ser obtida da remoção de zero ou mais caracteres da string original. Por exemplo, ANANA é a maior subsequência de BANANAS (retirando-se os caracteres nas posições 0 e 6).

**********
EXEMPLO:
**********

Entrada: 
- 4
- BANANAS
- PATA
- ANEL
- A1A

Saída:
- ANANA
- ATA
- sem resultados
- entrada inválida

**********

ENTRADA: A primeira linha contém um número inteiro T, indicando a quantidade de cenários a serem testados. Cada uma das T subsequentes linhas contém uma string S, onde 0 < len(S) ≤ 100 e S só poderá conter letras, ou seja, tem que pertencer ao intervalo [a, z].

SAÍDA: Para cada cenário de teste da entrada, caso o tamanho desta string seja maior que 1 (um) caracter, imprima a maior string encontrada. Caso contrário, imprima 'sem resultados'. No caso em que a entrada for inválida, imprima 'entrada inválida'.

## Questão 6 - Big Bang Theory - Bazinga (1,0 ponto EXTRA)

No oitavo episódio da segunda temporada de Big Bang Theory, chamado "The Lizard-Spock Expansion", Sheldon e Raj estão discutindo sobre o que é melhor: o filme Saturno 3 ou o programa de TV Deep Space 9. Raj, então, sugere que escolha seja baseada no vecendor de "pedra-papel-tesoura". No entanto, Sheldon diz que no jogo de pedra-papel-tesoura, jogadores familiarizados uns com os outros vão empatar de 75% a 80% das vezes devido  ao número limitado de opções e, então, sugire "pedra-papel-tesoura-lagarto-Spock".

As regras do jogo são:

1. tesoura corta papel;
2. papel cobre pedra;
3. pedra esmaga lagarto;
4. lagarto envenena Spock;
5. Spock esmaga tesouras;
6. tesoura decapita lagarto;
7. lagarto come o papel;
8. papel refuta Spock;
9. Spock vaporiza a pedra;
10. pedra esmaga tesoura;

 

Ambos escolheram Spock e o jogo empata! No entanto, não é difícil perceber o que aconteceria se o jogo tivesse continuado. No caso da vitória de Sheldon, ele teria dito: "Bazinga!"; se Raj tivesse vencido, Sheldon declararia: "Raj trapaceou!" ("Raj traiu" em portugues); no caso de empate, ele pedia uma nova rodada: "De novo!". Dadas as opções escolhidas por ambos, faça um programa que imprima a reação de Sheldon ao resultado.

**********
EXEMPLO:
**********

Entrada: 
- 3
- papel pedra
- lagarto tesoura
- Spock Spock

Saída:
- Caso #1: Bazinga!
- Caso #2: Raj trapaceou!
- Caso #3: De novo!

**********

ENTRADA: A primeira linha contém um número inteiro T (T ≤ 100), indicando a quantidade de cenários a serem testados. Cada uma das T subsequentes linhas contém as opções de Sheldon e Raj, separadas por um espaço em branco. As opções são: pedra, papel, tesoura, lagarto e spock.

SAÍDA: Para cada cenário de teste da entrada, imprima a mensagem  "Caso #t: R", onde t é o número do caso de teste e R é a reação de Sheldon ao resultado: "Bazinga!", "Raj trapaceou!" ou "De novo!"



## Finalização do Desenvolvimento

Ao finalizar, envie um email para o o recrutador responsável pelo seu processo seguindo o padrão de assunto: "Prova 1 - [Nome] - [Tecnologia]". Não esqueça de adicionar o usuário radix.recruit como reporter do seu repositório. Crie ou edite o README do seu repositório para realizar comentários e/observações, por exemplo, o que achou dos desafios ou maiores dificuldades encontradas.

## Avaliação - Critérios/Requisitos

Você será avaliado nos seguintes aspectos, em ordem de prioridade:
1. Correta execução: As respostas precisam estar coerentes com as premissas estabelecidas no questionário
2. Legibilidade de código e organização
3. Breve análise, em forma de comentário, explicando o raciocíonio utilizado para resolução da questão.

Observe que neste projeto é mais importante que você entregue um código de qualidade do que todas as funcionalidades exigidas. 
Seu código será avaliado independente da entrega total de funcionalidades.
É esperado que você desenvolva sem ajuda ou intervenção direta de terceiros, mas encorajamos que você pesquise por soluções e boas práticas sem nenhum tipo de restrição, apenas lembre-se que serão realizadas perguntas na entrevista a fim de certificar seu conhecimento total sobre a implementação. Jogue limpo!