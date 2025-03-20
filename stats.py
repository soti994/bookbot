def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_dict = {}
    text = text.lower()
    for character in text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def character_sort(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    for entry in sorted_dict.items():
        if entry[0].isalpha():
            print(f'{entry[0]}: {entry[1]}') 