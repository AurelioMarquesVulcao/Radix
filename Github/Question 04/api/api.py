from collections import Counter
# irá verificar se está tudo ok

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'x', 'z', 'w'
]

def verification(x):
    for c in range(0, len(alphabet)):
        if x == alphabet[c]:
            return x


# irá realizar de fato a função desejada
def check_occurrence(word, letter):
    word = word.lower()
    letter = letter.lower()
    if verification(letter) == letter:
        d = Counter(word)
        count_letter = d[letter]
        return count_letter
    else:
        return 'consulta inválida'



# print(check_occurrence('arara', 'ar'))
# print(check_occurrence('arAra', 'a'))
'''
print(check_occurrence('arara', 'ar'))
#print(check_occurrence('arara', 'ar1'))
print(check_occurrence('arara', 'a1'))
print(check_occurrence('arara', '1'))
print(check_occurrence('arara', 'r'))'''
