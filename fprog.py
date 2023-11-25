import re
from collections import Counter

"""def count_word_occurrences(word_list):
    return Counter(word_list)

text = ' Hello! Welcome to demofile.txtThis file is for testing purposes.Good Luck! Hello Dudu, Today we start a new Test'
result = count_word_occurrences()"""

def read_file_to_vector(filename):

    with open(filename, 'r') as file:

        return list(map(str.strip, file.readlines()))
    

#result = read_file_to_vector('example.txt')
#print(result)




def tokenize_text(text):
    words = re.split(r'\W+', text)
    return list(filter(None,map(str.lower, words)))

#text = ' Hello! Welcome to demofile.txt This file is for testing purposes.Good Luck! '
#
#result = tokenize_text(text)
#print(result)




def filter_words(word_list, filter_list):
    return list(filter(lambda word: word in filter_list, word_list))


#word_list = ['hello', 'welcome', 'to', 'demofile', 'txt', 'this', 'file', 'is', 'for', 'testing', 'purposes', 'good', 'luck', 'hello']

#filter_list = ['hello', 'welcome']

#result = filter_words(word_list,filter_list)
#print(result)

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

#word_list = [ "banana",  "cherry", "banana", "cherry"]
#word_occurrences = count_word_occurrences(word_list)
#print(word_occurrences)  # Output: {'apple': 3, 'banana': 2, 'cherry': 2}

def map_reduce_term_density(word_data):
    mapped_data = map(lambda word: word[1], word_data)

    # Reduce Phase: Calculate total distance and word count
    def reducer(accumulator, current):   
        (last_index, total_distance, count) = accumulator
        if last_index == 0:
            current = current
        print(accumulator)
        print(current)
        distance = current - last_index
        
        return (current, total_distance + distance, count + 1)

    current, total_distance, count = reduce(reducer, mapped_data, (word_data[0][1], 0, 0))
    #Calculate average distance and term density
    average_distance = total_distance / count if count > 1 else 0
    term_density = count / average_distance if average_distance != 0 else 0

    return term_density

def give_position_in_text(word, text):
    #if word in text:
    #positions = 
    return [(value, index) for index, value in enumerate(text) if value is word]


import itertools
from itertools import repeat
def calc_distance(word_list, chapter):
    TmpOccurences = map(give_position_in_text, word_list, repeat(chapter))
    occurences = []
    for list in TmpOccurences:
        for list in list:
            occurences.append(list)
    occurences.sort(key = lambda x: x[1])
    return map_reduce_term_density(occurences)

chapter = ['hello', 'welcome', 'to', 'demofile', 'txt','this', 'file', 'is', 'for', 'testing', 'purposes', 'good', 'luck', 'hello']     
term = ['hello', 'is', 'good']
calc_distance(term,chapter)

#word_data = [("apple", 1), ("banana", 4), ("orange", 8), ("pear", 12), ("orange", 22), ("banana", 30)]
#term_density = map_reduce_term_density(word_data)
#print(term_density)


def compare_war_vs_peace(distanceW, distanceP):
    lambda x: "peace-related" if distanceP > distanceW else "war-related"

text = read_file_to_vector('example.txt')
#tokenizedText = tokenize_text(text)
#WTerms = read_file_to_vector('war_terms.txt')
#PTerms = read_file_to_vector('peace_terms.txt')
#print(text)
#print(WTerms)
#print(PTerms)











"""


import itertools
from itertools import repeat
def give_position_in_text(word, text):
    #if word in text:
    #positions = 
    return [(index, value) for index, value in enumerate(text) if value is word]

def calc_distance(word_list, chapter):
    TmpOccurences = map(give_position_in_text, word_list, repeat(chapter))
    occurences = []
    for list in TmpOccurences:
        for list1 in list:
            occurences.append(list1[0])
    occurences.sort()
    def calc_averageDistance(x,y):
        return 
    
    #averageDistances = reduce(calc_averageDistance, occurences)
    #print(occurences)
    #print(averageDistances)

chapter = ['hello', 'welcome', 'to', 'demofile', 'txt','this', 'file', 'is', 'for', 'testing', 'purposes', 'good', 'luck', 'hello']     
term = ['hello', 'is', 'good']
calc_distance(term, chapter)



#calc_distance(maped)



def word_occurence_with_position(chapter,terms):
    zresult = []
    for term in terms:
        zresult.append([(i, v) for i, v in enumerate(chapter) if v is term])
    return list(itertools.chain.from_iterable(zresult))

#chapter = ['hello', 'welcome', 'to', 'demofile', 'txt', 'this', 'file', 'is', 'for', 'testing', 'purposes', 'good', 'luck', 'hello']     
#term = ['hello', 'is', 'good']
#maped = a(chapter, term)
#print(sorted(maped))





def find_pair(word):
    

def calc_relative_distance(word_list):
 mapped_terms = map(find_pair, word_list)
def is_in_chapter(term):
    mapExists = [x for x in chapter if term in x]
    mapPosition

def count_occurences(word_list, chapter):
    mapped_word_list = map(is_in_chapter, word_list)"""

