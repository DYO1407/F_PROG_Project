import re
from collections import Counter

def read_file_to_vector(filename):

    with open(filename, 'r') as file:
        return list(map(str.strip, file.readlines()))
    

#result = read_file_to_vector('example.txt')
#print(result)




def tokenize_text(text):
    words = re.split(r'\W+', text)
    #words = list(map(lambda x: x.split(), text))
    return list(filter(None,map(str.lower, words)))


#text = ' Hello! Welcome to demofile.txt This file is for testing purposes.Good Luck! '
#
#result = tokenize_text(text)
#print(result)




"""def filter_words(word_list, filter_list):
    return list(filter(lambda word: word in filter_list, word_list))"""


#word_list = ['hello', 'welcome', 'to', 'demofile', 'txt', 'this', 'file', 'is', 'for', 'testing', 'purposes', 'good', 'luck', 'hello']

#filter_list = ['hello', 'welcome']

#result = filter_words(word_list,filter_list)
#print(result)

from functools import reduce

"""def count_word_occurrences(word_list):
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
    return word_count"""

#word_list = [ "banana",  "cherry", "banana", "cherry"]
#word_occurrences = count_word_occurrences(word_list)
#print(word_occurrences)  # Output: {'apple': 3, 'banana': 2, 'cherry': 2}

def map_reduce_term_density(word_data):
    if word_data:
        mapped_data = map(lambda word: word[1], word_data)
        # Reduce Phase: Calculate total distance and word count
        def reducer(accumulator, current):   
            (last_index, total_distance, count) = accumulator
            if last_index == 0:
                current = current
            distance = current - last_index

            return (current, total_distance + distance, count + 1)

        current, total_distance, count = reduce(reducer, mapped_data, (word_data[0][1], 0, 0))
        #Calculate average distance and term density
        average_distance = total_distance / count if count > 1 else 0
        term_density = count / average_distance if average_distance != 0 else 0

        return term_density
    return 0

def give_position_in_text(word, text):
    return [(value, index) for index, value in enumerate(text) if value == word]

from itertools import repeat
def calc_distance(word_list, chapter):
    TmpOccurences = map(give_position_in_text, word_list, repeat(chapter))
    occurences = []
    for list in TmpOccurences:
        for list in list:
            occurences.append(list)
    occurences.sort(key = lambda x: x[1])
    return map_reduce_term_density(occurences)


#chapter = ['hello', 'welcome', 'to', 'demofile', 'txt','this', 'file', 'is', 'for', 'testing', 'purposes', 'good', 'luck', 'hello']     
#word_data = [("apple", 1), ("banana", 4), ("orange", 8), ("pear", 12), ("orange", 22), ("banana", 30)]
#term_density = map_reduce_term_density(word_data)
#print(term_density)

def chapterize_book(text):
    chapter = []
    book = []
    for line in text:
        if line:
            if line[0] != "chapter":
                chapter.append(line)
            else:
                book.append([x for row in chapter for x in row])
                chapter = []
    book.append([x for row in chapter for x in row]) 
    book.pop(0)
    return book

text = read_file_to_vector('example.txt')
WTerms = read_file_to_vector('war_terms.txt')
PTerms = read_file_to_vector('peace_terms.txt')
tokenizedText = list(map(tokenize_text, text))
book = chapterize_book(tokenizedText)
counter = 1
for chapter in book:
    WDensity = calc_distance(WTerms, chapter)
    PDensity = calc_distance(PTerms, chapter)
    print("Chapter " + str(counter) + ": ", end="")
    counter += 1
    if WDensity > PDensity:
        print("war-related ")
    else:
        print("peace-related ")

    

   