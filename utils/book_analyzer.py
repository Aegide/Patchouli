import json
import re

from pkg_resources import WorkingSet






path_file_lang = "C:/Github/Botania/Common/src/main/resources/assets/botania/lang/fr_fr.json"
path_file_entry = "C:/Github/Botania/Common/src/main/resources/assets/botania/patchouli_books/lexicon/en_us/entries/functional_flowers/orechid_ignem.json"



max_line_score = 464


def clean_entry(raw_entry):
    clean_entry = re.sub(r"\$\([^p]*?\)", "", raw_entry)
    return clean_entry[2:-2] # removes the double-quotes


def get_word_list_from_entry(clean_entry:str):

    word_list = clean_entry.split(" ")
    new_word_list = []

    for word in word_list:

        values = word.split("$(p)")

        if len(values) == 2:
            values = [values[0], "$(p)", values[1]]
        
        elif len(values) != 1:
            print("ERROR", word, values)

        # print(element, values)

        for value in values:
            new_word_list.append(value)

    return new_word_list


def handle_word_list(word_list:list[str]):
    for word in word_list:
        word_score = get_word_score(word)
        print(word_score, word)



def get_word_score(word:str):
    word_score = 0
    for letter in word:
        if letter in value16:
            word_score += 16
        else:
            word_score += 12
    return word_score




value16 = "abcdeghkmnopqrsuvwxyz"
value12 = "fijlt"

some_entry = "Le jasminerai est limité dans ce qu'il peut créer. Il ne peut rien produire qui viens du Nether. Ce qui est facile à régler, en changeant un peu la recette.$(p)Le jasminerai ardent utilise du mana pour synthétiser des minerais du Nether à partir de la netherrack. Cette fleur fonctionne uniquement dans le Nether."

print(" ")







"""
for char in entry:


    char_score = 12 if char in value12 else 16

    if char_score + line_score < max_line_score:
        line += char 
        line_score += char_score
    else:
        print(">>>", line_score, line)
        line_score = char_score
        line = char


print(">", line_score, line)
"""




with open(path_file_lang, 'rb') as file_lang:
    content_lang = file_lang.read().decode("UTF-8")

    with open(path_file_entry, 'r') as file_entry:
        json_data = "".join(file_entry.readlines())
        json_entry = json.loads(json_data)
        json_pages = json_entry["pages"]

        for json_element in json_pages:
            if (json_element["type"]=="text"):

                name_element = json_element["text"]
                print(name_element, "\n")

                pattern = "(.*)" + name_element + "(.*)"
                results = re.search(pattern, content_lang)
                entry = "".join(results[0].split(":")[1:])
                entry = clean_entry(entry)
                print(entry, "\n")

                word_list = get_word_list_from_entry(entry)
                print(word_list, "\n")


                handle_word_list(word_list)






# 16px : abcdeghkmnopqrsuvwxyz
# 12px : fijlt


# 16px = 12px + 4px
# 12px = 10px + 2px


# 18px : (space)
# 34px : (2 spaces)
# 50px : (3 spaces)
# 66px : (4 spaces)
# 82px : (5 spaces)

# 464px = 16*(29)
# 456pxr = 12*(38)


# max = 464 ??




# 20(m) + 12(i)
# 19(m) + 13(i)
# 18(m) + 14(i)
# 17(m) + 16(i)
# 16(m) + 17(i)
# 15(m) + 18(i)




