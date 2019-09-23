def palindrome(x):
    a = []
    b = []
    i = 0
    for c in range(0,len(x)):
        a.append(x[c])
    for d in range(0, len(x),1):
        b.insert(0, x[d])
    return a, b
    # return a.reverse()
    return 'Oi. Tudo bem?'


print(palindrome('bananas'))
print((palindrome('ama')))
x = [1,2,3,4]
print(x.reverse())