def all_lower(x):
    x.lower()


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'x', 'z', 'w'
]


def verification(x):
    for c in range(0, len(alphabet)):
        print(alphabet[c])
        print("x" * 60)
        if x == alphabet[c]:
            return x




#print(verification('n'))
#print(len(alphabet))
#print(alphabet[2])
