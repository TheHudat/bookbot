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
    print (character_dict)