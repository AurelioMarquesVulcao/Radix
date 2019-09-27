from analyzer import result_possibilities
''' 
pedra esmaga tesoura;
pedra esmaga lagarto;

papel cobre pedra;
papel refuta Spock;

tesoura corta papel;
tesoura decapita lagarto;

lagarto envenena Spock;
lagarto come o papel;

Spock esmaga tesouras;
Spock vaporiza a pedra;
 '''

# Indicates the winner after analyzing the possibilities.
# Indica o vencedor após a análise das possibilidades.
def winner_is(choice01, choice02):
    result = result_possibilities(choice01, choice02)
    winner = ''
    if result['p1'] > result['p2']:
        winner = 'Bazinga!'
    elif result['p1'] < result['p2']:
        winner = 'Raj trapaceou'
    elif result['p1'] == result['p2']:
        winner = 'De novo!'
    return winner
