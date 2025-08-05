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


def morse_decrypt(code: str) -> str:
    """
    This function will decrypt your morse code to text
    Args:
        code: (String) just morse code.

    Returns: (String) text

    """
    reverse_dict = {v: k for k, v in morse_code_dict.items()}
    return ''.join(reverse_dict[symbol] for symbol in code.split(' ') if symbol in reverse_dict)


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

    decrypted: str = morse_decrypt(encrypted)
    print("Decrypted:", decrypted)


if __name__ == "__main__":
    test_morse_converter()