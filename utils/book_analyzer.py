import json
import re

outer_path = "C:/Github/Botania/Common/src/main/resources/assets/botania"



chapter = "functional_flowers"
entry = "orechid_ignem"


# where all the actual text is
path_file_lang = "C:/Github/Botania/Common/src/main/resources/assets/botania/lang/fr_fr.json"

# full of links
path_file_entry = f"{outer_path}/patchouli_books/lexicon/en_us/entries/{chapter}/{entry}.json"






max_line_score = 464
space_score = 16

value16 = "abcdeghkmnopqrsuvwxyzéèêàüûILCN"
value14 = "t"
value4 = "'"
value8 = "."
#value12 = "fijlt"



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

    is_loud = True

    line = ""
    line_score = 0
    line_count = 1

    for word in word_list:
        word_score = get_word_score(word) 
        # print(">>>", word_score, word)

        if word == "$(p)":
            if is_loud:
                print(line_count, ":", line_score, ")", line)

            line = ""
            line_score = 0
            line_count += 1
            if is_loud:
                print(line_count, ":", line_score, ")", line)

            line = ""
            line_score = 0
            line_count += 1

        else:
            
            if word_score + line_score < max_line_score:
                line += word + " "
                line_score += word_score + space_score

            else:
                if is_loud:
                    print(line_count, ":", line_score, ")", line)
                line = word + " "
                line_score = word_score + space_score
                line_count += 1

    if is_loud:
        print(line_count, ":", line_score, ")", line)


def get_word_score(word:str):
    word_score = 0
    for letter in word:
        if letter in value16:
            word_score += 16
        elif letter in value14:
            word_score += 14
        elif letter in value8:
            word_score += 8
        elif letter in value4:
            word_score += 4
        else:
            word_score += 12
    return word_score








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

                # entry = "créer. Il ne peut rien"

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




"""


some_entry = "Le jasminerai est limité dans ce qu'il peut créer. Il ne peut rien produire qui viens du Nether. Ce qui est facile à régler, en changeant un peu la recette.$(p)Le jasminerai ardent utilise du mana pour synthétiser des minerais du Nether à partir de la netherrack. Cette fleur fonctionne uniquement dans le Nether."

print(" ")

"""