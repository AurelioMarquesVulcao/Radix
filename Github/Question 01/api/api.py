# Escreva um programa que leia um número inteiro e imprima o número de Fibonacci
# correspondente a esse número lido. Lembre-se de que os primeiros elementos da série
# Fibonacci são 0 e 1 e cada termo posterior é calculado a partir do soma dos dois
# precedentes. Todos os números de Fibonacci calculados neste programa devem caber
# em um número não assinado de 64 bits.

# ENTRADA: A primeira linha contém um número inteiro T, identificando a quantidade
# de cenários a serem testados. Cada cenário contém um número inteiro N (0 <= N <= 60),
# correspondente ao último termo de série de Fibonacci.

# SAÍDA: Para cada cenário de teste de entrada, imprimir a mensagem "Fib (N) = X",
# onde X é o último termo da série de Fibonacci
from math import ceil

# um numero não assinado possui inteiro curto possui  2 byte e vai da 0 a 65.535
# 64 bit possuem 8 byte
# numero não assinado inteiro longo possui 4 byte e vai de 0 a 4.294.967.295
# 64 bit possuem 8 byte

# a formula de binet permite que eu encontre qualquer número fibonacci
def fibonacci(x):
    phi = 1.61803398874989
    n = ((phi**x) - (1 - phi)**x) / (5**.5)
    return ceil(n)
