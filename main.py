
def le_arquivo(nome_arquivo):
    f = open(nome_arquivo, 'r')
    tipo = f.readline()
    linhas = f.readlines()
    return tipo, linhas


def escreve(linha, arquivo):
    arquivo.write((linha[0] + ' ' + linha[1] + ' ' + linha[2] +
                   ' ' + linha[3] + ' ' + linha[4]))


def converte_para_duplamente_infinita(linhas):

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

    # <current state> <current symbol> <new symbol> <direction> <new state>
    for linha in linhas_modificadas:
        tupla = linha
        # se nao for linha em branco
        if tupla[0] != '\n':
            if tupla[3] == 'l':
                # if tupla[1] == '¢':
                escreve(tupla, arquivo)
            else:
                escreve(tupla, arquivo)

    arquivo.close()


def converte_para_sipser(linhas):
    print('a')


def main():

    # recebe nome do arquivo de entrada
    # nome_arquivo = input("Digite o nome do arquivo de entrada com extensão\n")
    nome_arquivo = "entrada.txt"

    # lê o arquivo
    tipo, linhas = le_arquivo(nome_arquivo)

    if ";S" in tipo:
        converte_para_duplamente_infinita(linhas)

    elif ";I" in tipo:
        converte_para_sipser(linhas)
    else:
        print("Tipo invalido")
        exit()


if __name__ == "__main__":
    main()
