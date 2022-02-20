from patterns import get_pattern
from default_dict import get_default_dict
from math import log2

from dictionary import load_dict

allowed_words = load_dict('allowed.txt')
answer_words = load_dict('words.txt')


"""
Makes a guess based off of allowed guesses and possible answers.
"""
def make_guess(allowed, answers):
    best_guess = ''
    best_ig = 0

    for word in allowed:
        expected_ig = calculate_entropy(word, answers)
        if expected_ig >= best_ig:
            best_guess = word
            best_ig = expected_ig
    
    return [best_guess, best_ig]

def calculate_entropy(guess, answers):
    patterns = get_default_dict(0)
    total_entropy = 0

    for answer in answers:
        pattern = get_pattern(guess, answer)
        patterns[pattern] +=1
    
    total_count = len(answers)
    
    for pattern in patterns:
        count = patterns[pattern]
        pattern_prob = count / total_count

        entropy = -(pattern_prob * log2(pattern_prob))
        total_entropy += entropy

    return total_entropy


