def create_alphabet_dict():
    alphabet_dict = {}
    for char in range(ord('a'), ord('z')+1):
        alphabet_dict[chr(char)] = char
    return alphabet_dict

alphabet_dict = create_alphabet_dict()


print(alphabet_dict)