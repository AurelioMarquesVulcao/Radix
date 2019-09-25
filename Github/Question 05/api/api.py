from validation_str import verification_alphabet
from validation_str import verification_extension
from validation_str import remove_accents
from validation_str import slicing_word


# fatia a palavra e inverte seus caracteres
def invert_word(x):
    b = []
    for d in range(0, len(x), 1):
        b.insert(0, remove_accents(x[d]))
    return b    


# testa se a palvra é um palindromo
def palindrome(x):
    if slicing_word(x) == invert_word(x):
        return x
    else:
        return 'sem resultado'


def exit(x):
    check_word = ''
    return 'oi', check_word


# print(palindrome('bananas'))
# print((palindrome('amã')))
# print(exit('amã'))
# print(exit('Bananas'))
# print(exit('ama'))
palindromos = ['osso', 'ama']
not_palindromos = ['pata', 'bananas', 'mamão']
x = [1, 2, 3, 4]


#print(validator.verification_alphabet('a'))
#print(validator.verification_alphabet('a'))
#print(verification_extension('x'))
# print()
