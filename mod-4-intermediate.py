'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    new_ord = ord(letter) + shift;
    
    if ord(letter) == 32:
        return " ";
    else:
        pass
    
    if new_ord <= 90 and new_ord >= 65:
        return chr(new_ord);
    else:
        return chr(64+(new_ord-90));

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message_list = [];
    alphabet_dictionary = {
        0: "A", 
        1: "B", 
        2: "C", 
        3: "D", 
        4: "E", 
        5: "F", 
        6: "G", 
        7: "H", 
        8: "I", 
        9: "J", 
        10: "K", 
        11: "L", 
        12: "M", 
        13: "N", 
        14: "O", 
        15: "P", 
        16: "Q", 
        17: "R", 
        18: "S", 
        19: "T", 
        20: "U", 
        21: "V", 
        22: "W", 
        23: "X", 
        24: "Y", 
        25: "Z"}

    inverse_dictionary = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25}
    for i in message:
        message_list.append(i);
    
    for number in range(len(message)):
        if message_list[number] == " ":
            pass
        else:
            if inverse_dictionary[message_list[number]] + shift <= 25:
                message_list[number] = alphabet_dictionary[inverse_dictionary[message_list[number]] + shift];
            else:
                message_list[number] = alphabet_dictionary[((inverse_dictionary[message_list[number]] + shift) - 26)];
            
    encrypted_message = "";

    for k in range(len(message)):
        encrypted_message = encrypted_message + message_list[k];
    
    return encrypted_message;


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    new_ord = ord(letter) + ord(letter_shift) - 65;
    
    if ord(letter) == 32:
        return " ";
    else:
        pass
    
    if new_ord <= 90 and new_ord >= 65:
        return chr(new_ord);
    else:
        return chr(64+(new_ord-90));

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    
    encrypted_message = "" 
    message_list = [];
    key_list = [];
    key_full = "";
    alphabet_dictionary2 = {
                0: "A", 
                1: "B", 
                2: "C", 
                3: "D", 
                4: "E", 
                5: "F", 
                6: "G", 
                7: "H", 
                8: "I", 
                9: "J", 
                10: "K", 
                11: "L", 
                12: "M", 
                13: "N", 
                14: "O", 
                15: "P", 
                16: "Q", 
                17: "R", 
                18: "S", 
                19: "T", 
                20: "U", 
                21: "V", 
                22: "W", 
                23: "X", 
                24: "Y", 
                25: "Z"}

    inverse_dictionary2 = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7,
        "I": 8,
        "J": 9,
        "K": 10,
        "L": 11,
        "M": 12,
        "N": 13,
        "O": 14,
        "P": 15,
        "Q": 16,
        "R": 17,
        "S": 18,
        "T": 19,
        "U": 20,
        "V": 21,
        "W": 22,
        "X": 23,
        "Y": 24,
        "Z": 25}

    for g in message:
        message_list.append(g);
    
    if len(message_list) % len(key) == 0:
        while len(key_full) < len(message_list):
            key_full = key_full + key;
        for h in key_full:
            key_list.append(h);
    
    elif len(message_list) % len(key) != 0:
        key_fragment = key[0: len(message) % len(key)]
        for i in range(len(message) // len(key)):
            key_full = key_full + key;
        key_full = key_full + key_fragment;
        for j in key_full:
            key_list.append(j)
    
    print(key_full);
    for k in range(len(key_list)):
        key_list[k] = inverse_dictionary2[key_list[k]];
     
    for l in range(len(message)):
        if message_list[l] == " ":
            pass
        else:
            if inverse_dictionary2[message_list[l]] + key_list[l] <= 25:
                message_list[l] = alphabet_dictionary2[inverse_dictionary2[message_list[l]] + key_list[l]]
            else:
                message_list[l] = alphabet_dictionary2[((inverse_dictionary2[message_list[l]] + key_list[l]) - 26)]
                                               
    for m in range(len(message_list)):
        encrypted_message = encrypted_message + message_list[m]
    
    return encrypted_message