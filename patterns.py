from default_dict import get_default_dict
from match import Matches
"""
Returns dictionary of letter occurrences within a given word.
"""
def letter_counts(word):
    counts = get_default_dict(0)
    for char in word:
        counts[char] += 1
    return counts

"""
Gets pattern represented as a base 3 number -- 0 is none, 1 is wrong location, 2 is match.
"""
def get_pattern(guess, word):
    pattern = 0
    chars = letter_counts(word)

    for i in range(5):
        match = Matches.NONE
        if guess[i] == word[i]:
            match = Matches.MATCH
            chars[guess[i]] -= 1
        elif chars[guess[i]] > 0:
            match = Matches.PRESENT
            chars[guess[i]] -= 1
        pattern += (match * (3 ** (4 - i)))

    return pattern

def pattern_string_to_number(pattern):
    total = 0
    cur_exp = 0
    for i in reversed(range(len(pattern))):
        total += int(pattern[i]) * (3 ** cur_exp)
        cur_exp += 1
    
    return total
