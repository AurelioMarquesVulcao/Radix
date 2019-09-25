from validation_str import verification_letter
from validation_str import slicing_word

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


#corta_1_caractere('Jaca')
#corta_1_caractere_final('apaw')
#corta_1_ultima('Bananas')
# print(palindrome('bananas'))
# print((palindrome('amã')))
# print(exit('amã'))
# print(exit('Bananas'))
# print(exit('ama'))
#palindromos = ['osso', 'ama']
#not_palindromos = ['pata', 'bananas', 'mamão']
#x = [1, 2, 3, 4]


#print(validator.verification_alphabet('a'))
#print(validator.verification_alphabet('a'))
#print(verification_extension('x'))
# print()
