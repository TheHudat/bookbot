def word_count(text):
    return len(text.split())

def character_count(text):
    lower_case_text = text.lower()
    character_dict = {}
    for c in lower_case_text:
        if c in character_dict:
            character_dict[c] += 1
        else: 
            character_dict[c] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def sort_char_list(dict):
    dict_list = []
    for char in dict:
        if char.isalpha():
            dict_list.append({"char": char, "num" : dict[char]})
    dict_list.sort(reverse=True, key = sort_on)
    return dict_list
    