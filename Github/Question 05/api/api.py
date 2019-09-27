from validation_str import verification_letter
from validation_str import slicing_word
from validation_str import remove_accents

# Slice the word and invert its characters.
# Fatia a palavra e inverte seus caracteres.
def invert_word(x):
    b = []
    for d in range(0, len(x), 1):
        b.insert(0, x[d])
    return b    


# Tests if the word is a palindrome.
# Testa se a palvra é um palindromo.
def palindrome(x):
    x = verification_letter(x)
    if slicing_word(x) == invert_word(x):
        return x
    else:
        return 'sem resultado'


''' Parses the string and checks all possible combinations to form a 
palindrome string without changing the order of letters, just removing letters. '''
''' Analisa a string e verifica todas as combinações possíveis para formar 
uma string palíndromo sem mudar a ordem das letras, apenas removendo letras. '''
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
    ''' The repeating loop will put all possibilities of palindromes in one list, 
    with the last item in the list being the largest possible palindrome string. '''
    ''' O laço de repetição vai colocar todas as possibilidades de palíndromos 
    em uma lista, sendo o último item da lista a maior string palíndromo possível. '''
    for k in range(0, len(b)):
        if palindrome(b[k]) != 'sem resultado':
            c.append(palindrome(b[k]))
            # print(c)
    if len(c) < 1:
        c.append('sem resultado')
    c.reverse()
    return c[0]
