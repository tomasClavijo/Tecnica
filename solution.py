#Ejercicio 1: O(N)

def add_between_zeroes(arr):
    first_zero_index = -1
    last_zero_index = -1
    sum_elements = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            if first_zero_index == -1:
                first_zero_index = i
            last_zero_index = i
    if first_zero_index != -1 and last_zero_index != -1 and first_zero_index != last_zero_index:
        sum_elements = sum(arr[first_zero_index + 1: last_zero_index])
    
    print(sum_elements)
    return(sum_elements)

# Ejemplo de llamada:
#add_between_zeroes([0, 4, 5, 6, 0, 7, 8])

#Ejercicio 2

import requests

dictionary_url = "https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt"

def silly_autocomplete(word):
    if len(word) < 3:
        return None
    
    response = requests.get(dictionary_url)
    dictionary = response.text.splitlines()
    
    word = word.lower()
    for w in dictionary:
        if w.lower().startswith(word) and w.lower() != word:
            print(w)
            return w
    
    return None

# Ejemplo de llamada:
#silly_autocomplete("nomatchforthisword")
