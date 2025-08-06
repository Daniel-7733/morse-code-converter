morse_code_dict: dict[str, str] = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.', 
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',  'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',   

    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....', 
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!' : '-.-.--',
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...',
    ';': '-.-.-.', '=': '-...-',  '+': '.-.-.',  '-': '-....-',  '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def morse_encrypt(text: str) -> str:
    """
    This function will encrypt your text to morse code
    Args:
        text: (String) A word or sentences.

    Returns: (String) morse code

    """
    return ' '.join(morse_code_dict[i] for i in text.upper() if i in morse_code_dict)


def morse_decrypt(code: str, inverse_dictionary: dict) -> str:
    """
    This function will decrypt your morse code to text
    Args:
        inverse_dictionary: (dict) it should be reverse dictionary.
        code: (String) just morse code.

    Returns: (String) text

    """
    # reverse_dict = {v: k for k, v in morse_code_dict.items()}
    return ''.join(inverse_dictionary[symbol] for symbol in code.split(' ') if symbol in inverse_dictionary)

def reverse_dictionary(original_dictionary: dict) -> dict[str, str]:
    """
    This function will reverse the key and value in a dictionary.

    Args:
        original_dictionary: This argument need a dictionary. Type should be str, str.

    Returns: Will return a reverse dictionary (dict[str, str])

    """
    return {v: k for k, v in original_dictionary.items()}


def check_morse() -> bool:
    # TODO: check if user enter the morse code not bunch of text.
    # I might use for loop to see if characters exist in morse code
    # if it was morse character, then return True otherwise False
    raise NotImplementedError("'check_morse()' not made yet")


def test_morse_converter() -> None:
    """
    this function will test other functions to see if the works correctly.

    Returns: None

    """
    # text: str = "HELLO FRIEND"
    text: str = input("Your massage: ")
    encrypted: str = morse_encrypt(text)
    print("Encrypted:", encrypted)

    reverse_dict: dict[str, str] = reverse_dictionary(morse_code_dict)
    decrypted: str = morse_decrypt(encrypted, reverse_dict)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    test_morse_converter()