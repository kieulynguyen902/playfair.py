from tkinter import Tk, Label, Entry, Button, Text
from playfair_cipher import PlayfairCipher

class PlayfairApp:
    def __init__(self, master):
        self.master = master
        master.title("Playfair Cipher Decoder")

        self.key_label = Label(master, text="Key:")
        self.key_label.grid(row=0, column=0)

        self.key_entry = Entry(master)
        self.key_entry.grid(row=0, column=1)

        self.input_label = Label(master, text="Cipher Text:")
        self.input_label.grid(row=1, column=0)

        self.input_entry = Entry(master)
        self.input_entry.grid(row=1, column=1)

        self.decode_button = Button(master, text="Decode", command=self.decode)
        self.decode_button.grid(row=2, columnspan=2)

        self.output_label = Label(master, text="Plain Text:")
        self.output_label.grid(row=3, column=0)

        self.output_text = Text(master, height=5, width=30)
        self.output_text.grid(row=3, column=1)

    def decode(self):
        key = self.key_entry.get().upper()
        cipher_text = self.input_entry.get().upper()
        cipher = PlayfairCipher(key)
        plain_text = cipher.decrypt(cipher_text)
        self.output_text.delete(1.0, "end")
        self.output_text.insert("end", plain_text)

def main():
    root = Tk()
    app = PlayfairApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
