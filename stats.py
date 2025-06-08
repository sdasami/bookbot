def number_of_words(file_contents):
    num_words = 0
    return len(file_contents.split())
    #print(f"Found {num_words} total words")

# Oma koodi:
"""def number_of_characters(file_contents):
    word_list = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'æ': 0, 'ë': 0, 'â': 0, 'ê': 0, 'ô': 0
                 }
    characters_lenght = len(file_contents)
    characters = list(file_contents)
    #word_list = set(characters)
    c = 0
    #print(word_list)

    for c in range(c, characters_lenght):
        #print(c)
        #print(characters[c].lower())
        #print(word_list[characters[c].lower()])
        if characters[c].lower() in word_list:
            #print(word_list[characters[c].lower()])
            word_list[characters[c].lower()] += 1
            #print(word_list)
        
        c += 1
    print(word_list)
    #print(characters_lenght)
    #print(characters)"""

def number_of_characters(file_contents):
    word_list = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in word_list:
            word_list[lowered] += 1
        else:
            word_list[lowered] = 1
    #print(word_list)
    return word_list

def sort_on(dict):
    return dict["num"]

def sort_characters(characters_and_numbers):
    #print(characters_and_numbers)
    dictionary = []
    dictionary_total = {}
    for c in characters_and_numbers:
        dictionary.append({"char": c, "num": characters_and_numbers[c]})
    dictionary.sort(reverse=True, key=sort_on)
    return dictionary
    #print(dictionary)

