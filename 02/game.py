#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from itertools import permutations
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7
DICTIONARY_UPPER = [i.upper() for i in DICTIONARY]


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    return random.choices(POUCH, k = NUM_LETTERS)


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    word = input("Please enter word to play:")
    _validation(word, draw)
    return word


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    draw_copy = draw[:]
    result = True
    for letter in word:
        if letter not in draw_copy:
            result = False
            break
        else:
            draw_copy.remove(letter)
    result = result and word in DICTIONARY
    if not result:
        raise ValueError("Invalid word from player")


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    # result = []
    # for permutation in _get_permutations_draw(draw):
    #     if permutation.upper() in DICTIONARY_UPPER:
    #         result.append(permutation)
    # return result
    return [i for i in _get_permutations_draw(draw) if i.upper() in DICTIONARY_UPPER]


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    perms = []
    for i in range(1, NUM_LETTERS+1):
        perms.extend([''.join(i) for i in permutations(draw, i)])
    return perms
    return [''.join(i) for i in range(1, NUM_LETTERS + 1)]


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
