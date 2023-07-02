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

class Node:
    def __init__(self):
        self.children = {} #Almacena los nodos hijos
        self.is_word = False #Indica si el nodo representa el final de una palabra

class Trie:
    def __init__(self):
        self.root = Node() # Nodo Raiz

    def insert(self, word): 
        node = self.root # Parto del nodo raiz
        for char in word:
            if char not in node.children: # Verificamos si el caracter actual no esta presente en los hijos del nodo actual
                node.children[char] = Node() # Si no esta presente en los hijos del nodo actual, se crea un nuevo nodo y se agrega como hijo del actual
            node = node.children[char] # Despues de agregar el nuevo nodo, se actualiza el actual para pasar al siguiente nivel del arbol. 
        node.is_word = True # Una vez  que se recorrieron todos los caracteres, se marca el nodo final como una palabra completa.

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

def load_dictionary():
    response = requests.get(dictionary_url)
    dictionary = response.text.splitlines()
    return dictionary

Trie = Trie()
dictionary = load_dictionary()
for word in dictionary:
    Trie.insert(word)

def silly_autocomplete(word):
    if len(word) < 3:
        return None

    prefix = word.upper()
    node = Trie.search_prefix(prefix)
    if node:
        for char, child in node.children.items():
            if child.is_word:
                print(prefix + char)
                return prefix + char

    return None