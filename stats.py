def get_num_words(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    dictionary_one = {}
    for character in text:
        lower = character.lower()
        if lower not in dictionary_one:
            dictionary_one[lower] = 1
        else:
            dictionary_one[lower] += 1
    return dictionary_one

def sort_on(items):
    return items["num"]

def list_of_dicts(xxx):
    new_list = []

    for char, count in xxx.items():
        new_dict = {"char": char, "num": count}
        new_list.append(new_dict)

    
    new_list.sort(reverse=True, key=sort_on)
    
    
    
    return new_list
