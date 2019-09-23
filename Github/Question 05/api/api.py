from validation_str import verification_alphabet
from validation_str import verification_extension
from validation_str import remove_accents


# fatia a palavra para podermos trabalhar com os caracteres separadamente
def slicing_word(x):
    a = []
    for c in range(0, len(x)):
        a.append(remove_accents(x[c]))
    return a
    

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


print(palindrome('bananas'))
print((palindrome('amã')))
palindromos = ['osso', 'ama']
not_palindromos = ['pata', 'bananas', 'mamão']
x = [1, 2, 3, 4]


#print(validator.verification_alphabet('a'))
#print(validator.verification_alphabet('a'))
#print(verification_extension('x'))
# print()
