import random
 
RULES = {'R':('S', 'Rock breaks Scissors'), 'P':('R', 'Paper covers Rock'), 'S':('P', 'Scissors cuts Paper')}
PLAYS = list(RULES.keys())
 
def RPS():
    results = {'Win':0, 'Lose':0, 'Tie':0}
    play = None
    while play != 'Q':
        play = input("Choose R(ock)/P(aper)/S(cissors)/Q(uit): ").upper()
        if play in PLAYS:  # If the input is valid
            computer = random.choice(PLAYS)
            if play == computer:
                print("You tied!")
                results['Tie'] += 1
            elif RULES[play][0] == computer:  # Did you win?
                print(f'{RULES[play][1]}.  You win!')
                results['Win'] += 1
            else:
                print(f'{RULES[computer][1]}.  You lose')
                results['Lose'] += 1
    for result in results.items(): # Print results
        print(*result)
 
RPS()