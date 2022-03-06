import json
import re






path_file_lang = "C:/Github/Botania/Common/src/main/resources/assets/botania/lang/fr_fr.json"
path_file_entry = "C:/Github/Botania/Common/src/main/resources/assets/botania/patchouli_books/lexicon/en_us/entries/functional_flowers/orechid_ignem.json"



max_line_score = 464


def clean_entry(raw_entry):
    clean_entry = re.sub(r"\$\([^p]*?\)", "", raw_entry)
    return clean_entry





value16 = "abcdeghkmnopqrsuvwxyz"
value12 = "fijlt"

entry = "Le jasminerai est limité dans ce qu'il peut créer. Il ne peut rien produire qui viens du Nether. Ce qui est facile à régler, en changeant un peu la recette.$(p)Le jasminerai ardent utilise du mana pour synthétiser des minerais du Nether à partir de la netherrack. Cette fleur fonctionne uniquement dans le Nether."


line_score = 0
line = ""


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



"""

with open(path_file_lang, 'rb') as file_lang:

    content_lang = file_lang.read().decode("UTF-8")

    with open(path_file_entry, 'r') as file_entry:
        json_data = "".join(file_entry.readlines())
        # print(json_data)

        json_entry = json.loads(json_data)

        json_pages = json_entry["pages"]

        for x in json_pages:
            if (x["type"]=="text"):
                
                pattern = "(.*)" + x["text"] + "(.*)"
                print(" ")
                print(pattern)

                results = re.search(pattern, content_lang)
                entry = "".join(results[0].split(":")[1:])
                print(" ")
                print(">>>", entry)


                entry = clean_entry(entry)
                print(" ")
                print(">>>", entry)

"""






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




