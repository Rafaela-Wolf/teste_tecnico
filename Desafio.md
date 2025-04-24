# Instruções e premissas

- O código desenvolvido deve ser escrito totalmente pelo candidato; a cópia de código da internet
  e o uso de inteligência artificial generativa são desqualificadores imediatos.
- Os critérios de avaliação das soluções são, em ordem: corretude,
  clareza, velocidade de execução, e uso de memória.
 

# Desafios

Usando a sua linguagem de programação preferida solucione os seguintes desafios:

## Parte 1
Crie um programa que lê de um arquivo uma lista de cidades e as faixas de CEP que as compõe,
e responde a qual cidade um CEP pertence.

O arquivo de entrada é composto por linhas com um nome de cidade, um CEP inicial, e
um CEP final separados por vírgula, então uma linha com dois traços "--" e por fim
um CEP. O seu programa então deve responder o nome da cidade ao qual esse CEP pertence.

Entrada de exemplo:

```plaintext
E,20000000,20001000
H,30000125,30000375
T,90000500,90001500
R,80000125,80000375
M,60000000,60000500
N,60000125,60000375
L,50000125,50000375
S,90000000,90002000
P,70000500,70001500
B,00000500,00001500
Q,80000000,80000500
O,70000000,70002000
J,40000125,40000375
K,50000000,50000500
C,10000000,10002000
F,20000250,20000750
A,00000000,00002000
I,40000000,40000500
D,10000500,10001500
G,30000000,30000500
--
60000330
```


## Parte 2
Crie um programa que lê de um arquivo uma lista de nomes de cidades
adjacentes e o custo de transporte entre elas, e calcula o
menor custo entre duas cidades não adjacentes.


O arquivo de entrada é composto por linhas com um nome de cidade, um CEP inicial, e
um CEP final separados por vírgula, então uma linha com dois traços "--".
Seguidos de linhas com dois nomes de cidade e um número representando o custo
de transportar uma mercadoria da primeira cidade até a segunda, então uma linha com
dois traços "--". Finalmente deve receber uma linha com dois CEPs.
O seu program deve então responder com a rota mais barata para transportar
uma mercadoria entre o primeiro e o segundo CEP dá ultima linha da entrada, e
o custo total desta rota.

Entrada de exemplo:

```plaintext
K,50000000,50000500
A,00000000,00000500
L,50000125,50000375
Q,80000000,80000500
B,00000125,00000375
E,20000000,20000500
M,60000000,60000500
D,10000375,10001125
H,30000125,30000375
O,70000000,70001000
I,40000000,40001000
N,60000125,60000375
S,90000000,90001500
F,20000125,20000375
P,70000250,70000750
G,30000000,30000500
C,10000000,10001500
J,40000250,40000750
T,90000375,90001125
R,80000125,80000375
--
O,D,44.27
I,T,27.68
S,C,26.34
S,E,17.41
B,O,45.89
S,I,39.53
E,S,28.40
E,N,28.10
M,I,45.30
S,G,40.30
B,I,49.07
O,P,21.38
J,S,22.40
I,N,48.42
K,N,40.63
S,O,38.53
G,I,41.27
A,H,44.85
K,F,41.38
T,M,29.51
L,Q,43.44
B,R,30.36
I,E,46.10
H,T,27.77
I,P,16.24
R,L,45.11
T,J,48.42
G,J,43.37
D,M,15.38
O,R,30.39
M,B,29.43
D,G,30.46
A,C,38.98
K,B,48.46
F,N,15.53
Q,J,37.77
B,H,40.48
O,G,48.95
O,I,26.53
R,K,24.64
J,K,21.34
T,J,46.43
D,C,42.10
L,N,46.63
S,N,46.14
K,N,19.13
G,I,44.50
N,T,26.27
G,N,23.63
S,O,15.70
--
10001086,80000245
```
