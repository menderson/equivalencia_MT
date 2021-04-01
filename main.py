
def le_arquivo(nome_arquivo):
    f = open(nome_arquivo, 'r')
    tipo = f.readline()
    linhas = f.readlines()
    return tipo, linhas


def escreve(linha, arquivo):
    arquivo.write((linha[0] + ' ' + linha[1] + ' ' + linha[2] +
                   ' ' + linha[3] + ' ' + linha[4]))


def alfabeto_da_fita(linhas):
    # <current state> <current symbol> <new symbol> <direction> <new state>
    alfabeto_fita = ['_']

    for linha in linhas:
        tupla = linha.split(' ')
        # linhas não vazias
        if tupla[0] != '\n':
            if tupla[1] in alfabeto_fita:
                continue
            else:
                alfabeto_fita.append(tupla[1])

            if tupla[2] in alfabeto_fita:
                continue
            else:
                alfabeto_fita.append(tupla[2])
    return alfabeto_fita


def converte_para_duplamente_infinita(linhas, alfabeto_da_fita):

    # cria o arquivo ou substitui se já existir
    arquivo = open('saida.txt', 'w')
    arquivo.write((";I\n"))
    arquivo.close()

    # abre o aquivo em modo apend
    arquivo = open('saida.txt', 'a')

    # cria estados auxiliares para inserir "¢" como marcador do inicio da fita
    first_step = ["0", "*", "*", "l", "firstaux\n"]
    second_step = ["firstaux", "_", "¢", "r", "second_aux\n"]

    escreve(first_step, arquivo)
    escreve(second_step, arquivo)

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
            if tupla[3] == 'l':
                tupla_aux = tupla
                estado_destino = tupla_aux[4]
                tupla_aux[4] = "aux" + tupla_aux[4]
                estado_aux_copia = tupla_aux[4]
                escreve(tupla_aux, arquivo)

                # se ler o caracater que indica o inicio da fita
                tupla_aux = [tupla_aux[4].rstrip(
                    '\n'), "¢", "¢", "r", estado_destino]
                escreve(tupla_aux, arquivo)

                # <current state> <current symbol> <new symbol> <direction> <new state>
                # se ler qualquer outro simbolo, simula o movimento estacionario
                tupla_aux2 = tupla
                tupla_aux2[4] = "aux2" + tupla_aux[4]
                estado_aux2 = tupla_aux2[4]
                for simbolo in alfabeto_da_fita:
                    tupla_aux = [estado_aux_copia.rstrip(
                        '\n'), simbolo, simbolo, "r", estado_aux2]
                    escreve(tupla_aux, arquivo)
                    tupla_aux = [estado_aux2.rstrip(
                        '\n'), simbolo, simbolo, "l", estado_destino]
                    escreve(tupla_aux, arquivo)

                # escreve(aux2, arquivo)

            else:
                escreve(tupla, arquivo)

    arquivo.close()


def converte_para_sipser(linhas, alfabeto_da_fita):
    # cria o arquivo ou substitui se já existir
    arquivo = open('saida.txt', 'w')
    arquivo.write((";I\n"))
    arquivo.close()

    # abre o aquivo em modo apend
    arquivo = open('saida.txt', 'a')

    # cria estados auxiliares para fazer o deslocamento até o final da fita
    aux1 = "aux1\n"
    aux2 = "aux2\n"
    aux3 = "aux3\n"
    aux4 = "aux4\n"
    aux5 = "aux5\n"

    # tuplas auxiliares para deslocar todos os simbolos umas vez para a direita
    tupla_aux = ["0", "0", "¢", "r", aux1]
    escreve(tupla_aux, arquivo)

    tupla_aux = ["0", "1", "¢", "r", aux2]
    escreve(tupla_aux, arquivo)

    tupla_aux = [aux1.rstrip('\n'), "0", "0", "r", aux1]
    escreve(tupla_aux, arquivo)
    tupla_aux = [aux1.rstrip('\n'), "1", "0", "r", aux2]
    escreve(tupla_aux, arquivo)

    tupla_aux = [aux2.rstrip('\n'), "1", "1", "r", aux2]
    escreve(tupla_aux, arquivo)
    tupla_aux = [aux2.rstrip('\n'), "0", "1", "r", aux1]
    escreve(tupla_aux, arquivo)

    tupla_aux = [aux1.rstrip('\n'), "_", "0", "r", aux3]
    escreve(tupla_aux, arquivo)
    tupla_aux = [aux2.rstrip('\n'), "_", "1", "r", aux3]
    escreve(tupla_aux, arquivo)
    tupla_aux = ["0", "_", "_", "r", aux3]
    escreve(tupla_aux, arquivo)

    # tupla para inserir simbolo de final da palavra de entrada §
    tupla_aux = [aux3.rstrip('\n'), "_", "§", "l", aux4]
    escreve(tupla_aux, arquivo)

    # tuplas para voltar o cabeçote para a posição inicial
    tupla_aux = [aux4.rstrip('\n'), "0", "0", "l", aux4]
    escreve(tupla_aux, arquivo)
    tupla_aux = [aux4.rstrip('\n'), "1", "1", "l", aux4]
    escreve(tupla_aux, arquivo)

    # o estado inicial agora se chamará aux5
    tupla_aux = [aux4.rstrip('\n'), "¢", "¢", "r", aux5]
    escreve(tupla_aux, arquivo)

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
                # captura o estado destino e vai para um estado auxiliar
                estado_destino = tupla[4].rstrip("\n")
                tupla[4] = estado_destino + "auxinicio\n"
                escreve(tupla, arquivo)

                # tupla para verificar se o simbolo lido é o de inicio da fita ¢
                tupla_aux = [estado_destino + "auxinicio", "¢",
                             "_", "r", estado_destino + "auxinicio2\n"]
                escreve(tupla_aux, arquivo)

                # desenvolver

                # se o simbolo lido nao for o de inicio da fita, simula o movimento estacionario e vai para o estado destino
                for simbolo in alfabeto_da_fita:
                    if simbolo != "*":
                        tupla = [estado_destino + "auxinicio", simbolo,
                                 simbolo, "r", estado_destino + "estadoauxnotend\n"]
                        escreve(tupla, arquivo)
                tupla = [estado_destino + "estadoauxnotend", "*",
                         "*", "l", estado_destino + "\n"]
                escreve(tupla, arquivo)

            else:
                # captura o estado destino e vai para um estado auxiliar
                estado_destino = tupla[4].rstrip("\n")
                tupla[4] = estado_destino + "auxfinal\n"
                escreve(tupla, arquivo)

                # tupla para verificar se o simbolo lido é o de final da fita §, apaga o simbolo e insere branco
                tupla_aux = [estado_destino + "auxfinal", "§",
                             "_", "r", estado_destino + "auxfinal2\n"]
                escreve(tupla_aux, arquivo)

                # escreve o simbolo final e vai para a esquerda
                tupla_aux = [estado_destino + "auxfinal2",
                             "_", "§", "l", estado_destino + "\n"]
                escreve(tupla_aux, arquivo)

                # se o simbolo lido nao for o de final da fita, simula o movimento estacionario e vai para o estado destino
                for simbolo in alfabeto_da_fita:
                    if simbolo != "*":
                        tupla = [estado_destino + "auxfinal", simbolo,
                                 simbolo, "l", estado_destino + "estadoauxnotend\n"]
                        escreve(tupla, arquivo)
                tupla = [estado_destino + "estadoauxnotend", "*",
                         "*", "r", estado_destino + "\n"]
                escreve(tupla, arquivo)

    # <current state> <current symbol> <new symbol> <direction> <new state>


def main():

    # recebe nome do arquivo de entrada
    # nome_arquivo = input("Digite o nome do arquivo de entrada com extensão\n")

    nome_arquivo = "entrada.txt"

    # lê o arquivo
    tipo, linhas = le_arquivo(nome_arquivo)

    # encontra alfabeto da fita
    alfabeto_fita = alfabeto_da_fita(linhas)

    if ";S" in tipo:
        converte_para_duplamente_infinita(linhas, alfabeto_fita)

    elif ";I" in tipo:
        converte_para_sipser(linhas, alfabeto_fita)
    else:
        print("Tipo invalido")
        exit()


if __name__ == "__main__":
    main()
