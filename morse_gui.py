from tkinter import Tk, Frame, Text, Button, Entry, END
from morse_logic import morse_encrypt, morse_decrypt


def handle_text_to_morse() -> None:
    """Convert to morse"""
    user_input: str = text_input_entry.get()
    result: str = morse_encrypt(user_input)
    output_display.delete("1.0", END)
    output_display.insert(END, result)

def handle_morse_to_text() -> None:
    """Convert to text"""
    morse_input: str = morse_input_entry.get()
    try:
        result: str = morse_decrypt(morse_input)
    except Exception as e:
        result: str = f"Error: {e}"
    output_display.delete("1.0", END)
    output_display.insert(END, result)


# ------------- GUI ------------- #
app: Tk = Tk()
app.title("Morse Code")
app.geometry("400x400")

window: Frame = Frame(app)  # Use a Frame to manage layout better
window.pack(padx=10, pady=10)  # Display the frame

# Output area
output_display: Text = Text(window, bg="#BEBEBE", height=10, width=45)  # Adjusted height
output_display.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# ---- Text -> Morse ----
text_input_entry: Entry = Entry(window, width=40)
text_input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

convert_to_morse_btn: Button = Button(window, text="Convert to Morse", command=handle_text_to_morse)
convert_to_morse_btn.grid(row=1, column=2)

# ---- Morse -> Text ----
morse_input_entry: Entry = Entry(window, width=40)
morse_input_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

convert_to_text_btn: Button = Button(window, text="Convert to Text", command=handle_morse_to_text)
convert_to_text_btn.grid(row=2, column=2)

# TODO: Part Three
# Connect to the internet and send the message to another person

app.mainloop()
