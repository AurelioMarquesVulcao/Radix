import unicodedata
import re


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'x', 'z', 'w',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Y', 'X', 'Z', 'W'
]

# fatia a palavra para podermos trabalhar com os caracteres separadamente
def slicing_word(x):
    a = []
    for c in range(0, len(x)):
        a.append(remove_accents(x[c]))
    return a


# Checks whether a given character is alphabetic.
# Verifica se um dado caracter é alfabético.
def verification_alphabet(x):
    if x in alphabet:
        return x
    else:
        return False


# It will remove the accents from the words to be analyzed.
# Removerá os acentos das palavras a serem análizadas.
def remove_accents(x):  
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', x)
    letter = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', letter)


# Checks if word is less than 100 characters
# Verifica se a palavra possui menos de 100 caracteres
def verification_extension(x):
    if len(x) <= 100:
        return x
    return False


# cria uma super string de exatos 100 caracteres
def character_text_100():
    i = []
    for c in range(0, 100):
        i += 'a'
    return ''.join(map(str, i))

# cria uma super string de exatos 101 caracteres
def character_text_101():
    i = []
    for c in range(0, 101):
        i += 'a'
    return ''.join(map(str, i))


# excuta todas as verificações para poder liberar ou não a palavra.
def verification_letter(word):
    word = remove_accents(word)
    if verification_extension(word) != False:
        a = word
        a = remove_accents(a)
        a = slicing_word(a)
        b = []
        for c in range(0, len(word)):
            if verification_alphabet(a[c]) == False:
                b.append(a[c])
        if len(b)>0:
            return 'Entrada invalida'
        else:
            return remove_accents(word.lower())
    else:
        return 'Entrada invalida' # mais de 100 caracteres


# testes rapidos para a função
#print(f'1 - {verification_letter(character_text_101())}')
