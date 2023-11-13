import re
from collections import Counter





"""



def count_word_occurrences(word_list):
    return Counter(word_list)

text = ' Hello! Welcome to demofile.txtThis file is for testing purposes.Good Luck! Hello Dudu, Today we start a new Test'
result = count_word_occurrences()

"""


def read_file_to_vector(filename):

    with open(filename, 'r') as file:

        return list(map(str.strip, file.readlines()))
    

result = read_file_to_vector('example.txt')
print(result)




def tokenize_text(text):
    words = re.split(r'\W+', text)
    return list(filter(None,map(str.lower, words)))

text = ' Hello! Welcome to demofile.txt This file is for testing purposes.Good Luck! '

result = tokenize_text(text)
print(result)

def filter_words(word_list, filter_list):
    return list(filter(lambda word: word in filter_list, word_list))


word_list = ['hello', 'welcome', 'to', 'demofile', 'txt', 'this', 'file', 'is', 'for', 'testing', 'purposes', 'good', 'luck', 'hello']

filter_list = ['hello', 'welcome']

result = filter_words(word_list,filter_list)
print(result)



WAR_PEACE_result = read_file_to_vector('War_Peace.txt')
Example_reault = read_file_to_vector('example.txt')

Peace_terms_result = read_file_to_vector('peace_terms.txt')
War_terms_result = read_file_to_vector('war_terms.txt')

#print(Peace_terms_result)
#print(tokenize_text(Example_reault))

from functools import reduce

def count_word_occurrences(word_list):
    # Mapping: Convert each word in the list to a (word, 1) pair
    mapped_words = map(lambda word: (word, 1), word_list)

    # Reducing: Aggregate counts for each word
    def reducer(count_map, word_pair):
        word, count = word_pair

        if word in count_map:
            count_map[word] += count
        else:
            count_map[word] = count
        return count_map

    word_count = reduce(reducer, mapped_words, {})
    return word_count

word_list = [ "banana",  "cherry", "banana", "cherry"]
word_occurrences = count_word_occurrences(word_list)
print(word_occurrences)  # Output: {'apple': 3, 'banana': 2, 'cherry': 2}




