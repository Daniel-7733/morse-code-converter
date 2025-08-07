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

    is_morse: bool = check_morse(code)

    if is_morse:
        return ''.join(inverse_dictionary[symbol] for symbol in code.split(' ') if symbol in inverse_dictionary)

    return "Write the code"


def reverse_dictionary(original_dictionary: dict) -> dict[str, str]:
    """
    This function will reverse the key and value in a dictionary.

    Args:
        original_dictionary: This argument need a dictionary. Type should be str, str.

    Returns: Will return a reverse dictionary (dict[str, str])

    """
    return {v: k for k, v in original_dictionary.items()}


def check_morse(user_input: str) -> bool:
    """
    Function will check if the user input is actual morse code not a text.
    Args:
        user_input: (String) should be morse code

    Returns: Will return True if user input is morse code otherwise False

    """

    valid_morse_chars: set[str] = {'.', '-', '/', ' '}
    return all(char in valid_morse_chars for char in user_input) # all() will return if all the element are true


def test_morse_converter() -> None:
    """
    this function will test other functions to see if the works correctly.

    Returns: None

    """
    while True:

        a_text: str = input("write 'n' for normal text and 'c' for code: ").lower()

        if a_text == 'n':
            text: str = input("Your massage: ")
            encrypted: str = morse_encrypt(text)
            print("Encrypted:", encrypted)
        elif a_text == 'c':
            c_text: str = input("Your massage: ")
            reverse_dict: dict[str, str] = reverse_dictionary(morse_code_dict)
            decrypted: str = morse_decrypt(c_text, reverse_dict)
            print("Decrypted:", decrypted)
        else:
            break



if __name__ == "__main__":
    test_morse_converter()