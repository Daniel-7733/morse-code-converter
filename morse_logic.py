morse_code_dict = {
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
    return ' '.join(morse_code_dict[i] for i in text.upper() if i in morse_code_dict)

def morse_decrypt(code: str) -> str:
    reverse_dict = {v: k for k, v in morse_code_dict.items()}
    return ''.join(reverse_dict[symbol] for symbol in code.split(' ') if symbol in reverse_dict)

def test_morse_converter() -> None:
    # text: str = "HELLO FRIEND"
    text: str = input("Your massage: ")
    encrypted: str = morse_encrypt(text)
    print("Encrypted:", encrypted)

    decrypted: str = morse_decrypt(encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    test_morse_converter()