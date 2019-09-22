# Faça um programa para criar uma matriz quadrada, onde todos os seus
# elementos são iguais a 0 (zero) com exceção de sua diagonal
# principal que deve ser preenchida com o valor 1 (um).

# ENTRADA: A primeira linha contém um número inteiro T, identificando
# a quantidade de cenários a serem testados. Cada cenário contém
# um número inteiro N (0 <= N <= 20), correspondendo ao tamanho da matriz N x N.

# SAÍDA: Para cada cenário de teste de entrada, imprima a
# mensagem "Matrix (NxN)" seguida da matriz.
w = []
matrix = []
def matrix_generator(x, y):
    for c in range(0, x):
        w.append(0)
    for i in range(0, y):
        matrix.append(w)
    #print(matrix)


def matrix_printer(x,y):
    print('Matriz (', x, 'x', y, ')')
    for c in range(0,x):
        matrix[c][c] = 1
        for i in range(0,y):
            matrix[c][c-1] = 0
            print(matrix[c][i], end='')
        print()


def solucao_temporaria(x):
    matrix_generator(x, x)
    matrix_printer(x, x)


solucao_temporaria(3)
