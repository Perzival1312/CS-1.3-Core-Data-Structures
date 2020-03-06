
# # create a frozenset with all words in dictionary file
# # generate all possible arrangements of input word
# # check if in set and then store in a list if true
# # 
# # after doing so with all words get the letters at specific positions
# # this is where things get weird
# # do the same as an original input word and if that returns nothing
# # look for a pair of words that can be made with the new letter set
# # just look up stirling numbers of a second kind itll explain the idea
# # just need to write some algo to get that set up.....
# # prolly gotta be able to explain it b4 i can effectively write the algo tho


# def _load_words():
#    f = open('/usr/share/dict/words', 'r')
#    words_list = f.readlines()
#    f.close()
#    for ind, word in enumerate(words_list):
#        words_list[ind] = word.strip()
#    return words_list
# # create an constant time lookup for all possible words
# WORDS = frozenset(_load_words())

# def assemble_perms(word):
#     real_permutations = []
#     # print('here')
#     # print('here pt 2')
#     for letter_sets in perms(word):
#         real_permutations.append(''.join(letter_sets))
#     # all_permutations = list(perms(word))
#     # for letter_sets in all_permutations:
#     #     real_permutations.append(''.join(letter_sets))

#     return real_permutations

# def find_all_possible_words(possiblilities):
#     assert isinstance(possiblilities, list)
#     possibles = []
#     for word in possiblilities:
#         if word in WORDS:
#             possibles.append(word)
#             # after finding a dictionary word there is no 
#             # need to keep searching for another one
#             # break
#     return possibles

# def get_letters(words, spots):
#     assert isinstance(spots, dict)
#     assert isinstance(words, list)
#     letters = []
#     for key, val in spots.items():
#         for ind in val:
#             letters.append(words[key][ind])
#     return letters

# def find_answer_simple(letters):
#     answer = []
#     # print('here')
#     answer.extend(find_all_possible_words(letters))
#     # print(answer)
#     if not answer:
#         print('yeah this aint happening....')
#         # print('gimme a sec this isnt a dictionary word')
#         answer.extend(annoying_af_stirling_func(letters))
#     # print('The corect answer is one of the following: ', answer)
#     return answer[0]

# def annoying_af_stirling_func(letters):
#     possible_perms, actual_perms = [], []
#     for i in range(2,len(letters)-3):
#         possible_perms.append(perms(letters, i))
#         # print(possible_perms)
#     actual_perms.append(find_all_possible_words(possible_perms))
#     # print(actual_perms)
#     return 'word'

# def parse_input(input):
#     words = []
#     spots = {} # word_index in words_list : [letter_index in word]
#     # do parsing
#     return words, spots

# def main(input_stuff):
#     actuals = []
#     letters = ''
#     # words, spots = parse_input(input_stuff)
#     # words = ['mbipl', 'hoves', 'funsie', 'nioide']
#     # spots = {0:[0,1,3], 1:[0,1,4], 2:[0,2,4,5], 3:[2,3,5]}
#     # words = ['ulqit', 'lavees','beeestrmp','svrtaeh','tecthuns','autmnu','atolflob']
#     # spots = {0:[0], 1:[5], 2:[0], 3:[6], 5:[5]}
#     # letters += 's'
#     words = ['knidy','legia','cronee','tuvedo']
#     spots = {0:[0,1], 1:[0,2], 2:[1,3], 3:[0,5]}

#     # solve all of the initial anagrams
#     for word in words:
#         # get perm, call possibles func, append to new arr
#         actuals.extend(find_all_possible_words(assemble_perms(word)))
#     print('Actual Words: ', ', '.join(actuals))
#     # get letters for final anagram
#     letters += ''.join(get_letters(actuals, spots))
#     # print(letters)
#     # get all permutations of the final anagram
#     perm = assemble_perms(letters)
#     # print(perms)
#     # solve final anagram
#     print('Answer: ', find_answer_simple(perm))
    
# main('stuff')







'''
get all unique letters in original word
create trie based on all words stating wiith set of letters
find valid words in the trie
'''
import pygtrie as trie 
from itertools import permutations as perms

letter_set = set(['k','n','i','d','y','l','e','g','i','a','c','r','o','n','e','e','t','u','v','e','d','o'])

def _load_words():
    f = open('/usr/share/dict/words', 'r')
    words_list = f.readlines()
    f.close()
    for ind, word in enumerate(words_list):
        if word[0] in letter_set:
            words_list[ind] = word.strip()
    word_trie = trie.StringTrie.fromkeys(words_list)
    return word_trie
# create an constant time lookup for all possible words
WORDS = _load_words()

def assemble_perms(word):
    real_permutations = []
    # print('here')
    # print('here pt 2')
    for letter_sets in perms(word):
        real_permutations.append(''.join(letter_sets))
    # all_permutations = list(perms(word))
    # for letter_sets in all_permutations:
    #     real_permutations.append(''.join(letter_sets))

    return real_permutations

def find_all_possible_words(possiblilities):
    assert isinstance(possiblilities, list)
    possibles = []
    for word in possiblilities:
        if word in WORDS:
            possibles.append(word)
            # after finding a dictionary word there is no 
            # need to keep searching for another one
            # break
    return possibles

def get_letters(words, spots):
    assert isinstance(spots, dict)
    assert isinstance(words, list)
    letters = []
    for key, val in spots.items():
        for ind in val:
            letters.append(words[key][ind])
    return letters

def find_answer_simple(letters):
    answer = []
    # print('here')
    answer.extend(find_all_possible_words(letters))
    # print(answer)
    if not answer:
        print('yeah this aint happening....')
        # print('gimme a sec this isnt a dictionary word')
        answer.extend(annoying_af_stirling_func(letters))
    # print('The corect answer is one of the following: ', answer)
    return answer[0]

def annoying_af_stirling_func(letters):
    possible_perms, actual_perms = [], []
    for i in range(2,len(letters)-3):
        possible_perms.append(perms(letters, i))
        # print(possible_perms)
    actual_perms.append(find_all_possible_words(possible_perms))
    # print(actual_perms)
    return 'word'

def parse_input(input):
    words = []
    spots = {} # word_index in words_list : [letter_index in word]
    # do parsing
    return words, spots

def main(input_stuff):
    actuals = []
    letters = ''
    # words, spots = parse_input(input_stuff)
    # words = ['mbipl', 'hoves', 'funsie', 'nioide']
    # spots = {0:[0,1,3], 1:[0,1,4], 2:[0,2,4,5], 3:[2,3,5]}
    # words = ['ulqit', 'lavees','beeestrmp','svrtaeh','tecthuns','autmnu','atolflob']
    # spots = {0:[0], 1:[5], 2:[0], 3:[6], 5:[5]}
    # letters += 's'
    words = ['knidy','legia','cronee','tuvedo']
    spots = {0:[0,1], 1:[0,2], 2:[1,3], 3:[0,5]}

    # solve all of the initial anagrams
    for word in words:
        # get perm, call possibles func, append to new arr
        actuals.extend(find_all_possible_words(assemble_perms(word)))
    print('Actual Words: ', ', '.join(actuals))
    # get letters for final anagram
    # letters += ''.join(get_letters(actuals, spots))
    # print(letters)
    # get all permutations of the final anagram
    # perm = assemble_perms(letters)
    # print(perms)
    # solve final anagram
    # print('Answer: ', find_answer_simple(perm))
    

main(None)



def get_file_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines

def solve_word_jumble(words, circles, final):
    """Solve a word jumble by unscrambling four jumbles, then a final jumble.
    Parameters:
    - words: list of strings, each is the scrambled letters for a single word
    - circles: list of strings, each marks whether the letter at that position
        in the solved anagram word will be used to solve the final jumble.
        This string contains only two different characters:
        1. O (letter "oh") = the letter is in the final jumble
        2. _ (underscore) = the letter is not in the final jumble
    - final: list of strings in the same format as circles parameter that shows
        how the final jumble's letters are arranged into a word or phrase."""
    # Get all English words in the built-in dictionary
    all_words = get_file_lines()
    # TODO: Solve this word jumble with data structures and algorithms

def main2():
    # Word Jumble 1. Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his ___."
    words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles1 = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final1 = ['OO', 'OOOOOO']
    solve_word_jumble(words1, circles1, final1)

    # Word Jumble 2. Cartoon prompt for final jumble: "What a dog house is."
    words2 = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles2 = ['____O', '_OO__', '_O___O', 'O____O']
    final2 = ['OOOO', 'OOO']
    solve_word_jumble(words2, circles2, final2)

if __name__ == '__main__':
    main2()