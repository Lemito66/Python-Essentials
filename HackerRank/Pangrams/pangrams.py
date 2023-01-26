def pangrams(sentence: str):
    result = ''
    new_sentence = sentence.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    alphabet_dict = dict.fromkeys(alphabet, 0)
    if len(new_sentence) <= 1000:
        for i in new_sentence:
            if i in alphabet_dict.keys():
                alphabet_dict[i] += 1
    else:
        return f'Your sentence have much length'
    """ for i in alphabet_dict:
        if i in alphabet_dict.values() == 0:
            return f'Not paragram'
        else:
            pass
            return f'Paragram, {alphabet_dict}' """
    for value in alphabet_dict.values():
        if value == 0:
            return f'Not Pangram'
            break
        else:
            return f'Pangram'

    return alphabet_dict


#print(pangrams('We promptly judged antique ivory buckles for the next prize'))
#print(pangrams('We promptly judged antique ivory buckles for the prize'))

""" alphabet_dict = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 1
}
for key in alphabet_dict.values():
    if key == 0:
        print('Not Pangram')
        break
    else:
        print('Pangram') """
