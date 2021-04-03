# Desenvolvido por: Menderson Nicolau Costa

import sys


def le_arquivo(nome_arquivo):
    try:
        f = open(nome_arquivo, 'r')
        tipo = f.readline()
        linhas = f.readlines()

        # se a ultima linha nao tiver quebra de linha "\n" no final, então acrescenta "\n"
        if linhas[len(linhas)-1].find("\n") == -1:
            linhas[len(linhas)-1] = linhas[len(linhas)-1] + "\n"

        return tipo, linhas
    except:
        print("Erro ao abrir o arquivo")
        exit()

# função que acrescenta uma tuplas a lista de tuplas de saida


def acresenta(linha, tuplas):
    tupla = (linha[0] + ' ' + linha[1] + ' ' +
             linha[2] + ' ' + linha[3] + ' ' + linha[4])

    tuplas.append(tupla)

# função que retorna os simbolos da fita


def alfabeto_da_fita(linhas):
    alfabeto_fita = ['_']

    # percorre todas as tuplas procurando por simbolos diferentes nas segundas e terceiras posições
    for linha in linhas:

        tupla = linha.split(' ')

        # linhas não vazias
        if tupla[0] != '\n':

            if tupla[1] not in alfabeto_fita:
                alfabeto_fita.append(tupla[1])

            if tupla[2] not in alfabeto_fita:
                alfabeto_fita.append(tupla[2])

    return alfabeto_fita


def converte_para_duplamente_infinita(linhas, alfabeto_da_fita, tuplas):

    tuplas.append(";I\n")

    # cria estados auxiliares para inserir "¢" como marcador do inicio da fita
    tupla = ["0", "*", "*", "l", "firstaux\n"]
    acresenta(tupla, tuplas)
    tupla = ["firstaux", "_", "¢", "r", "second_aux\n"]
    acresenta(tupla, tuplas)

    linhas_modificadas = []
    # as demais menções ao estado "0" agr devem ser chamadas de  "second_aux"
    for linha in linhas:
        tupla = linha.split(' ')
        # linhas não vazias
        if tupla[0] != '\n':
            if tupla[0] == '0':
                tupla[0] = "second_aux"
            if tupla[4].rstrip('\n') == '0':
                tupla[4] = "second_aux\n"
        linhas_modificadas.append(tupla)

    for linha in linhas_modificadas:
        tupla = linha
        # se nao for linha em branco
        if tupla[0] != '\n':
            # para os movimentos a esquerda
            if tupla[3] == 'l':
                tupla_aux = tupla
                estado_destino = tupla_aux[4]
                tupla_aux[4] = "aux" + tupla_aux[4]
                estado_aux_copia = tupla_aux[4]
                acresenta(tupla_aux, tuplas)

                # se ler o caracater que indica o inicio da fita
                tupla_aux = [tupla_aux[4].rstrip(
                    '\n'), "¢", "¢", "r", estado_destino]
                acresenta(tupla_aux, tuplas)

                # se ler qualquer outro simbolo, simula o movimento estacionario
                tupla_aux2 = tupla
                tupla_aux2[4] = "aux2" + tupla_aux[4]
                estado_aux2 = tupla_aux2[4]
                for simbolo in alfabeto_da_fita:
                    tupla_aux = [estado_aux_copia.rstrip(
                        '\n'), simbolo, simbolo, "r", estado_aux2]
                    acresenta(tupla_aux, tuplas)
                    tupla_aux = [estado_aux2.rstrip(
                        '\n'), simbolo, simbolo, "l", estado_destino]
                    acresenta(tupla_aux, tuplas)

            else:
                acresenta(tupla, tuplas)


def converte_para_sipser(linhas, alfabeto_da_fita, tuplas):

    tuplas.append(";S\n")

    # cria estados auxiliares para fazer o deslocamento até o final da fita
    aux1 = "aux1\n"
    aux2 = "aux2\n"
    aux3 = "aux3\n"
    aux4 = "aux4\n"
    aux5 = "aux5\n"

    # remove simbolo * do alfabeto da fita
    if "*" in alfabeto_da_fita:
        alfabeto_da_fita.remove("*")

    # tuplas auxiliares para deslocar todos os simbolos do alfabeto de entrada umas vez para a direita
    tupla_aux = ["0", "0", "¢", "r", aux1]
    acresenta(tupla_aux, tuplas)

    tupla_aux = ["0", "1", "¢", "r", aux2]
    acresenta(tupla_aux, tuplas)

    tupla_aux = [aux1.rstrip('\n'), "0", "0", "r", aux1]
    acresenta(tupla_aux, tuplas)
    tupla_aux = [aux1.rstrip('\n'), "1", "0", "r", aux2]
    acresenta(tupla_aux, tuplas)

    tupla_aux = [aux2.rstrip('\n'), "1", "1", "r", aux2]
    acresenta(tupla_aux, tuplas)
    tupla_aux = [aux2.rstrip('\n'), "0", "1", "r", aux1]
    acresenta(tupla_aux, tuplas)

    tupla_aux = [aux1.rstrip('\n'), "_", "0", "r", aux3]
    acresenta(tupla_aux, tuplas)
    tupla_aux = [aux2.rstrip('\n'), "_", "1", "r", aux3]
    acresenta(tupla_aux, tuplas)
    tupla_aux = ["0", "_", "_", "r", aux3]
    acresenta(tupla_aux, tuplas)

    # tupla para inserir simbolo de final da palavra de entrada §
    tupla_aux = [aux3.rstrip('\n'), "_", "§", "l", aux4]
    acresenta(tupla_aux, tuplas)

    # tuplas para voltar o cabeçote para a posição inicial
    tupla_aux = [aux4.rstrip('\n'), "0", "0", "l", aux4]
    acresenta(tupla_aux, tuplas)
    tupla_aux = [aux4.rstrip('\n'), "1", "1", "l", aux4]
    acresenta(tupla_aux, tuplas)

    # o estado inicial agora se chamará aux5
    tupla_aux = [aux4.rstrip('\n'), "¢", "¢", "r", aux5]
    acresenta(tupla_aux, tuplas)

    # trocar todas as menções de estado "0" por "aux5"
    linhas_modificadas = []
    for linha in linhas:
        tupla = linha.split(' ')
        # linhas não vazias
        if tupla[0] != '\n':
            if tupla[0] == '0':
                tupla[0] = "aux5"
            if tupla[4].rstrip('\n') == '0':
                tupla[4] = "aux5\n"
        linhas_modificadas.append(tupla)

    # iniciamos a ler as tuplas de entrada
    for linha in linhas_modificadas:
        tupla = linha
        # se nao for linha em branco
        if tupla[0] != '\n':
            # se o movimento for a esquerda
            if tupla[3] == 'l':

                # captura o estado destino e cria um estado auxiliar
                estado_destino = tupla[4].rstrip("\n")
                tupla[4] = estado_destino + "auxinicio\n"
                acresenta(tupla, tuplas)

                # se o simbolo lido nao for o de inicio da fita, simula o movimento estacionario e vai para o estado destino
                for simbolo in alfabeto_da_fita:
                    if simbolo != "*" and simbolo != "¢":
                        tupla = [estado_destino + "auxinicio", simbolo,
                                 simbolo, "r", estado_destino + "estadoauxnotbegin\n"]
                        acresenta(tupla, tuplas)
                tupla = [estado_destino + "estadoauxnotbegin", "*",
                         "*", "l", estado_destino + "\n"]
                acresenta(tupla, tuplas)

                # tupla para verificar se o simbolo lido é o de inicio da fita ¢
                tupla_aux = [estado_destino + "auxinicio", "¢",
                             "¢", "r", estado_destino + "auxinicio2\n"]
                acresenta(tupla_aux, tuplas)

                # acresenta simbolo final e inicial ao alfabeto da fita
                if "§" not in alfabeto_da_fita:
                    alfabeto_da_fita.append("§")
                if "¢" not in alfabeto_da_fita:
                    alfabeto_da_fita.append("¢")

                # faz o deslocamento de todos os elementos da fita uma casa para a direita
                estado_auxiliar = estado_destino + "auxinicio2"
                for simbolo in alfabeto_da_fita:

                    estado_auxiliar_simbolo = estado_destino + "auxinicio2" + simbolo
                    tupla = [estado_auxiliar, simbolo,
                             "_", "r", estado_auxiliar_simbolo + "\n"]
                    acresenta(tupla, tuplas)

                    for simbolo_aux in alfabeto_da_fita:
                        if simbolo_aux != "§":
                            tupla = [estado_auxiliar_simbolo, simbolo_aux, simbolo,
                                     "r", estado_destino + "auxinicio2" + simbolo_aux + "\n"]
                            acresenta(tupla, tuplas)
                        else:
                            tupla = [estado_auxiliar_simbolo, simbolo_aux, simbolo,
                                     "r", "estado_auxiliar_voltar_final" + estado_destino + "\n"]
                            acresenta(tupla, tuplas)
                            tupla = ["estado_auxiliar_voltar_final" + estado_destino, "*", "§",
                                     "l", "estado_auxiliar_voltar" + estado_destino + "\n"]
                            acresenta(tupla, tuplas)

                # tuplas para achar o inicio
                alfabeto_da_fita.remove("§")
                for simbolo in alfabeto_da_fita:
                    if simbolo != "¢":
                        tupla = ["estado_auxiliar_voltar" + estado_destino, simbolo,
                                 simbolo, "l", "estado_auxiliar_voltar" + estado_destino + "\n"]
                        acresenta(tupla, tuplas)
                    else:
                        tupla = ["estado_auxiliar_voltar" + estado_destino, simbolo,
                                 simbolo, "r", estado_destino + "\n"]
                        acresenta(tupla, tuplas)

            # movimento para a direita
            else:
                # captura o estado destino e vai para um estado auxiliar
                estado_destino = tupla[4].rstrip("\n")
                tupla[4] = estado_destino + "auxfinal\n"
                acresenta(tupla, tuplas)

                # tupla para verificar se o simbolo lido é o de final da fita §, apaga o simbolo e insere branco
                tupla_aux = [estado_destino + "auxfinal", "§",
                             "_", "r", estado_destino + "auxfinal2\n"]
                acresenta(tupla_aux, tuplas)

                # escreve o simbolo final e vai para a esquerda
                tupla_aux = [estado_destino + "auxfinal2",
                             "_", "§", "l", estado_destino + "\n"]
                acresenta(tupla_aux, tuplas)

                # se o simbolo lido nao for o de final da fita, simula o movimento estacionario e vai para o estado destino
                for simbolo in alfabeto_da_fita:
                    tupla = [estado_destino + "auxfinal", simbolo,
                             simbolo, "l", estado_destino + "estadoauxnotend\n"]
                    acresenta(tupla, tuplas)
                tupla = [estado_destino + "estadoauxnotend", "*",
                         "*", "r", estado_destino + "\n"]
                acresenta(tupla, tuplas)


def main():

    # confere numero de argumentos
    if len(sys.argv) != 2:
        print("Numero de argumentos invalido")
        exit()
    nome_arquivo = sys.argv[1]

    # lê o arquivo
    tipo, linhas = le_arquivo(nome_arquivo)

    # encontra alfabeto da fita
    alfabeto_fita = alfabeto_da_fita(linhas)

    # lista de tuplas convertidas
    tuplas = []

    equivalente = None
    # chama as funções de conversão
    if ";S" in tipo:
        equivalente = "Maquina de Turing com fita duplamente infinita"
        converte_para_duplamente_infinita(linhas, alfabeto_fita, tuplas)

    elif ";I" in tipo:
        equivalente = "Maquina de Turing com fita infinita a direita (Sipser)"
        converte_para_sipser(linhas, alfabeto_fita, tuplas)
    else:
        print("O tipo informado na primeira linha do arquivo de entrada é invalido\n")
        exit()

    # remove possiveis linhas duplicadas
    new_lines = []
    for line in tuplas:
        if line not in new_lines:
            new_lines.append(line)

    # escreve no arquivo de saida
    output_file = "saida.txt"
    f = open(output_file, 'w')
    f.write("".join(new_lines))

    print("Programa de " + equivalente + ' equivalente salva em "saida.txt"')


if __name__ == "__main__":
    main()
