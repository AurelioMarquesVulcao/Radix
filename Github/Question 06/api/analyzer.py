# Checking the result possibilities.
# Checagem das possibilidades de resultado.
def result_possibilities(x,y):
    player_1 = 0
    player_2 = 0
    if x == 'pedra':
        if y == 'tesoura':
            player_1 += 1
        elif y == 'lagarto':
            player_1 += 1
        elif y == 'papel':
            player_2 += 1
        elif y == 'Spock':
            player_2 += 1
        result={'p1':player_1, 'p2':player_2}

    elif x == 'papel':
        if y == 'pedra':
            player_1 += 1
        elif y == 'Spock':
            player_1 += 1
        elif y == 'tesoura':
            player_2 += 1
        elif y == 'lagarto':
            player_2 += 1
        result={'p1':player_1, 'p2':player_2}
    
    elif x == 'tesoura':
        if y == 'papel':
            player_1 += 1
        elif y == 'lagarto':
            player_1 += 1
        elif y == 'pedra':
            player_2 += 1
        elif y == 'Spock':
            player_2 += 1
        result={'p1':player_1, 'p2':player_2}

    elif x == 'lagarto':
        if y == 'Spock':
            player_1 += 1
        if y == 'papel':
            player_1 += 1
        elif y == 'tesoura':
            player_2 += 1
        elif y == 'pedra':
            player_2 += 1
        result={'p1':player_1, 'p2':player_2}

    elif x == 'Spock':
        if y == 'tesoura':
            player_1 += 1
        elif y == 'pedra':
            player_1 += 1
        elif y == 'papel':
            player_2 += 1
        elif y == 'lagarto':
            player_2 += 1

        result={'p1':player_1, 'p2':player_2}
    
    return result
        