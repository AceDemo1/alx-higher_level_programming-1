#!/usr/bin/python3i
def best_score(a_dictionary):
    if a_dictionary:
        k = None
        l = list(a_dictionary)
        i = a_dictionary[l[0]]
        for j in a_dictionary:
            if a_dictionary[j] > i:
                i = a_dictionary[j]
                k = j
        return k
    return None