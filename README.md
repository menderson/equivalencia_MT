<h1 align="center">Equivalencia de duas variantes de Maquinas de Turing<h1>

<h2 align="center">Trabalho final da disciplina de Teoria da Computação </h2>
<br/>

O objetivo deste trabalho é demonstrar a equivalência de duas variantes disponíveis no 
simulador online de máquinas de Turing em http://morphett.info/turing/turing.html
Mais especificamente: será possível notar que a variante de fita duplamente infinita e  a variante de fita semi-infinita (modelo de Sipser) podem simular uma à outra.

## Requisitos

Python3 instalado na máquina

## Para executar:
### Na pasta do projeto:

```bash
$ python3 main.py <nome_do_arquivo_de_entrada_com extensão>
```

### Exemplo:
```bash
$ python3 main.py entrada.txt
```

## Saída

O programa de Maquina de Turing equivalente estará salvo no arquivo "saida.txt"

<br />

## Enunciado do trabalho

Trabalho Prático
O objetivo deste trabalho é demonstrar a equivalência de duas variantes disponíveis no 
simulador online de máquinas de Turing em http://morphett.info/turing/turing.html
Mais especificamente: será possível notar que a variante de fita duplamente infinita e 
a variante de fita semi-infinita (modelo de Sipser) podem simular uma à outra.

O trabalho consistirá em um programa que receberá um arquivo txt com uma entrada para o simulador, 
onde a primeira linha será

;I
caso seja um programa para máquina de Turing com fita duplamente infinita

;S
caso seja um programa para máquina de Turing com fita semi-infinita (modelo de Sipser)

O restante do arquivo será constituído exclusivamente de linhas no formato
    <current state> <current symbol> <new symbol> <direction> <new state>
conforme especificado no site do simulador, sem uso de novos comentários.

Tem-se a garantia de que os símbolos £,¢,§ não serão utilizados em nenhum arquivo de entrada, podendo ser utilizados como eventuais símbolos auxiliares.

O programa deverá retornar como saída um arquivo txt com um programa equivalente para o simulador online com tipo de fita inverso ao indicado no arquivo de entrada.

Os arquivos de entrada serão apenas de máquinas de Turing determinísticas e com codificação válida para o simulador. Todos os programas dados como entrada serão para reconhecimento de linguagens sobre o alfabeto {0,1}. Note, portanto, que a máquina de Turing dada como saída também será um reconhecedor para essa mesma linguagem sobre o alfabeto {0,1}.
O programa deve ser possível de ser executado em um computador com sistema operacional Ubuntu 20.04.2 LTS de 64 bits. A linguagem de implementação é livre dentro destas restrições.
A entrega deverá ser feita via moodle, com o programa final, instruções claras de execução caso necessárias e endereço de repositório público no github com todo o código-fonte.


<h4 align="center"> <em>&lt;/&gt;</em> by <a href="https://github.com/menderson" target="_blank">mendersoncosta</a> </h4>