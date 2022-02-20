from py_compile import _get_default_invalidation_mode
from default_dict import get_default_dict
from patterns import letter_counts
from match import Matches
import re

def letter_set():
    return set([letter for letter in 'abcdefghijklmnopqrstuvwxyz'])

ALLOWED_LETTERS = [letter_set() for _ in range(5)]
NEGATIVE_LETTERS = set()

PLACEHOLDER_CHAR = '0'

def build_regex(word, pattern):
    global ALLOWED_LETTERS
    pattern2 = pattern
    regex = '' 
    pos_letters = get_default_dict(0)
    possibly_allowed = set()
    discard_letters = set()

    for i in range(5):
        letter = word[i]
        match = pattern // (3 ** (4 - i)) 
        pattern -= match * (3 ** (4 - i))

        if match == Matches.NONE.value:
            NEGATIVE_LETTERS.add(letter)
            discard_letters.add(letter)
            regex += PLACEHOLDER_CHAR 
        elif match == Matches.PRESENT.value:
            pos_letters[letter] += 1 
            ALLOWED_LETTERS[i].discard(letter)
            possibly_allowed.add(letter)
            regex += PLACEHOLDER_CHAR
        elif match == Matches.MATCH.value:
            regex += letter
    
    for letter in discard_letters:
        if letter not in possibly_allowed:
            for i in range(len(ALLOWED_LETTERS)):
                ALLOWED_LETTERS[i].discard(letter)
    
    for i in range(5):
        letter = word[i]
        match = pattern2 // (3 ** (4 - i)) 
        pattern2 -= match * (3 ** (4 - i))

        if match != Matches.MATCH.value:
            allowed_chars = build_char_regex(i)
            regex = regex.replace(PLACEHOLDER_CHAR, allowed_chars, 1)

    regex = build_pos_look(pos_letters) + regex
    return regex

def build_pos_look(pos_letters):
    regex = ''
    for letter in pos_letters:
        regex += '(?=' + (('.*' + letter) * pos_letters[letter]) + ')'
    
    return regex

def build_char_regex(pos):
    global ALLOWED_LETTERS
    regex = '['
    for letter in ALLOWED_LETTERS[pos]:
        regex += letter
    regex += ']'

    return regex

def build_regex_matcher(regex):
    def matcher(considered):
        return True if re.search(regex, considered) is not None else False
    return matcher



# print(build_regex('heney', 135)) # 135 = 12000(3) -- matching 'teach'
# print(build_char_regex())
# print(len(build_char_regex()))
# print(build_pos_look(letter_counts("hene")))
    