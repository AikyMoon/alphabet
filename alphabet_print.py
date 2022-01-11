from letters_defs import letters_dict

def parser(text):
    parse_text = []
    for letter in text.lower():
        parse_text.append(letter)

    return parse_text

def print_text(parse_list:list, letters:dict):
    for letter in parse_list:
        letters[letter]()

text = input()
parse = parser(text)
print_text(parse, letters_dict)
