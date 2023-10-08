import time, random

def criacao_lista(N):
    lista = []
    # N = int(input("Digite o tamanho da lista: "))
    for i in range(N):
        lista.append(random.randint(0, N))
    return lista
def troca(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]

def empurra(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            troca(lista, i, i+1)

def bubble_sort(lista):
    n = len(lista)
    while n > 1:
        empurra(lista)
        n -= 1
    return lista

def selection_sort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            #seleciona o menor elemento em cada iteração
            if seq[j] < seq[min_index]:
                #troca os elementos - atribuição paralela
                seq[j], seq[min_index] = seq[min_index], seq[j]

def insertion_sort(lista):
    for i in range (1, len(lista)):
        pivo = lista[i]
        j = i-1
        while ((j >= 0) and (pivo < lista[j])):
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = pivo

def merge_sort(lista):
    if len(lista) > 1:

        # Encontrando o meio da lista
        meio = len(lista) // 2  # Parte inteira da lista

        # dividindo a lista em duas
        esquerda = lista[:meio]  # esquerdo do meio até a metade
        direita = lista[meio:]  # Direito do meio pra frente

        # chamada recursiva
        merge_sort(esquerda)  # ordenar as sub-listas
        merge_sort(direita)  # ordenar as sub-listas

        # Variáveis de controle
        # i - fará o controle da lista esquerda
        # j - fará o controle da lista direita
        # k - fará o controle da lista anterior à recursão
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1

            k += 1

        # Verificação dos elementos da lista da esquerda
        while (i < len(esquerda)):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Verificação dos elementos da lista da direita
        while (j < len(direita)):
            lista[k] = direita[j]
            j += 1
            k += 1

def get_time(arg):
    inicio = time.time()
    arg
    fim = time.time()
    return fim - inicio

def continuar():
    val = 0
    while val != 1:
        c = input("Iniciar ordenação de lista? S ou N:").upper()
        if c != 'S' and c != 'N':
            print("Digite S ou N")
        else:
            val = 1
    return c

def ordenação():
    val = 0
    while val != 1:
        alg = input("Digite o algoritmo que você deseja usar para ordenar:\n"
                     "bubble -> 1\n"
                     "selection -> 2\n"
                     "insertion -> 3\n"
                     "merge -> 4\n"
                    "R:")
        match alg:
            case '1':
                sort = 'bubble'
                tempo = get_time(bubble_sort(listaCopy))
                val = 1
            case '2':
                sort = 'selection'
                tempo = get_time(selection_sort(listaCopy))
                val = 1
            case '3':
                sort = 'insertion'
                tempo = get_time(insertion_sort(listaCopy))
                val = 1
            case '4':
                sort = 'merge'
                tempo = get_time(merge_sort(listaCopy))
                val = 1
            case _:
                print("Digite o algoritmo que você deseja usar para ordenar:\n"
                     "bubble -> 1\n"
                     "selection -> 2\n"
                     "insertion -> 3\n"
                     "merge -> 4\n"
                     "R:")
    return sort, tempo

def escolher_lista():
    val = 0
    lista = []
    while val != 1:
        numero = int(input("Qual a lista desejada para teste?"
                           "\n1 - Lista de 10.000 elementos"
                           "\n2 - Lista de 100.000 elementos"
                           "\n3 - Lista de 500.000 elementos"
                           "\n4 - Lista de 1.000.000 elementos"
                           "\nR: "))
        match numero:
            case 1:
                lista = criacao_lista(10000)
                val = 1
            case 2:
                lista = criacao_lista(100000)
                val = 1
            case 3:
                lista = criacao_lista(500000)
                val = 1
            case 4:
                lista = criacao_lista(1000000)
                val = 1
            case _:
                print("Escolha uma opção válida")
    return lista

def verificacao_lista(lista):
    if len(lista) == 0:
        return True
    else:
        return False

def mostrar_lista(lista):
    ver = verificacao_lista(lista)
    var = 0
    while var != 1:
        if ver == True:
            lista = escolher_lista()
            var = 1
        else:
            op = input("Você quer mudar a lista? S ou N\nR:").upper()
            match op:
                case 'S':
                    lista = escolher_lista()
                    var = 1
                case 'N':
                    var = 1
                case _:
                    print("Escolha uma opção válida")
    return lista

# Principal
tempo = {"bubble": [], "selection": [], "insertion": [], "merge": []} # Representação de um banco de dados
lista = [] # Representação de um banco de dados
c = continuar() # Variavel para controle do While

while c == 'S':

    # Escolhendo a lista a ser trabalhada e a fazendo uma copia da mesma para a execução das ordenações
    lista = mostrar_lista(lista)
    listaCopy = lista

    # Guardando tempo na lista respectiva dentro do dicionário
    tipo_tempo = ordenação() # Recuperando a tupla com a string referente a key do discionário e o tempo que demorou para ordenar.
    tempo[tipo_tempo[0]].append(tipo_tempo[1]) # Inserindo o tempo no dicionário no seu respectivo lugar
    # A linha acima, na teoria, é para simular a inserção no banco de dados

    # Restaurando a lista para o formato não ordenado
    listaCopy = lista

    # Saida dos tempos:
    print(tempo)

    # Finalizar ou continuar aplicação
    c = continuar()
