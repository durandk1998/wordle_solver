from dictionary import load_dict
from entropy import make_guess
from patterns import pattern_string_to_number
from regex import build_regex, build_regex_matcher

words = load_dict('words.txt')
allowed = load_dict('allowed.txt')

SOLVED = False

print("Pre-guess: ")
preguess = input()
ig = 'Unknown' 

while not SOLVED:
    if not preguess:
        [guess, ig] = make_guess(allowed, words)
    else:
        guess = preguess
        preguess = None

    print("GUESS: {guess}   IG: {ig}".format(guess = guess, ig = ig))

    print("Enter the pattern you got:")
    pattern = pattern_string_to_number(input())
    if pattern == 242: # 22222 in base 3, solved
        print("Solved! Word: " + guess)
        SOLVED = True
        break

    regex = build_regex(guess, pattern)
    matcher = build_regex_matcher(regex)

    words = list(filter(matcher, words))
    allowed = list(filter(matcher, allowed))
