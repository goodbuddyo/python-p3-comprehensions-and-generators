#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [x for x in num_list if x % 2 == 0]
    print(new_list)
    return new_list


return_evens([0, 1, 3, 5, 7, 8, 9])


# use comprehension - take a list of sentence strings and returns the list w/exclamation marks at the end.

def make_exclamation(sentence_list):
    List_new = [i + '!' for i in sentence_list]
    return List_new


make_exclamation(["Hello", "I'm doing great", "Python is fun"])
