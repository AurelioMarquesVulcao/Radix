import unicodedata
import re


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'x', 'z', 'w'
]

# Checks whether a given character is alphabetic.
# Verifica se um dado caracter é alfabético.
def verification_alphabet(x):
    for c in range(0, len(alphabet)):
        if x == alphabet[c]:
            return x
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


def character_text_100():
    i = []
    for c in range(0, 100):
        i += 'a'
    return ''.join(map(str, i))


def character_text_101():
    i = []
    for c in range(0, 101):
        i += 'a'
    return ''.join(map(str, i))



# testes rapidos para a função
# print(verification('a'))    # retorno esperado -  'a'
# print(verification('ar'))   # retorno esperado -  'False'
# print(verification('1'))    # retorno esperado -  'False'
# print( verification_extension(character_text_100()))  # retorno esperado -  'a....'
# print( verification_extension(character_text_101()))  # retorno esperado -  'False'
