from validation_str import verification_letter
from validation_str import slicing_word
from validation_str import remove_accents

# fatia a palavra e inverte seus caracteres
def invert_word(x):
    b = []
    for d in range(0, len(x), 1):
        b.insert(0, x[d])
    return b    


# testa se a palvra é um palindromo
def palindrome(x):
    x = verification_letter(x)
    if slicing_word(x) == invert_word(x):
        return x
    else:
        return 'sem resultado'


def find_palindrome(x):
    c = []
    if verification_letter(x) == 'Entrada invalida':
        c.append(verification_letter(x))
    a =  remove_accents(x)
    b = []
    w = 1
    for i in range(0,len(x)):
        w += 1
        y = w
        for j in range(0, (len(a)-1)):
            b.append(a[j: y])
            y += 1
    # o Laço vai colocar todas as possilidades de 
    # palindromos na lista, sendo a ultima a maior substring possivel
    for k in range(0, len(b)):
        if palindrome(b[k]) != 'sem resultado':
            c.append(palindrome(b[k]))
            # print(c)
    if len(c) < 1:
        c.append('sem resultado')
    c.reverse()
    return c[0]


# print('1-', find_palindrome('bananas'))
# print('2-', palindrome('bananas'))
# print('3-', find_palindrome('aoo'))
# print('4-', find_palindrome('ooa1'))

# Código menos elegante que localiza e texta Palindromos.
'''
def corta_1_caractere(x):
    b = slicing_word(x)
    #print(b)
    b.remove(b[0])
    #print(b)
    b = ''.join(map(str, b))
    #print(b)
    return palindrome(b)


def corta_1_caractere_final(x):
    b = slicing_word(x)
    #print(b)
    b = invert_word(b)
    b.remove(b[0])
    b = invert_word(b)
    #print(b)
    b = ''.join(map(str, b))
    #print(b)
    return palindrome(b)


def corta_1_ultima(x):
    b = slicing_word(x)
    #print(b)
    b.remove(b[0])
    #print(b)
    b = ''.join(map(str, b))
    #print(b)
    b = slicing_word(b)
    #print(b)
    b = invert_word(b)
    b.remove(b[0])
    b = invert_word(b)
    #print(b)
    b = ''.join(map(str, b))
    #print(b)
    return palindrome(b)


def sub_strig_palindrome(x):
    result = []
    if corta_1_caractere(x) != 'sem resultado':
        result.insert(0, corta_1_caractere(x))
    elif corta_1_caractere_final(x) != 'sem resultado':
        result.insert(0, corta_1_caractere_final(x))
    elif corta_1_ultima(x) != 'sem resultado':
        result.insert(0, corta_1_ultima(x))
    return result
'''
