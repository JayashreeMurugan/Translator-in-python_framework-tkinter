import tkinter as tk
from tkinter import ttk
from translate import Translator

class TranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Translator")

        self.create_widgets()

    def create_widgets(self):
        # Creating widgets
        self.input_text = tk.Text(self.master, width=50, height=10)
        self.input_text.grid(row=0, column=0, padx=10, pady=10)

        self.output_text = tk.Text(self.master, width=50, height=10)
        self.output_text.grid(row=0, column=1, padx=10, pady=10)

        self.translate_button = tk.Button(self.master, text="Translate", command=self.translate)
        self.translate_button.grid(row=1, column=0, padx=10, pady=10)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=1, column=1, padx=10, pady=10)

    def translate(self):
        # Getting input text
        input_text = self.input_text.get("1.0", tk.END)

        # Creating a translator object
        translator = Translator(to_lang="Tamil")

        # Translating the text
        translation = translator.translate(input_text)

        # Displaying the translated text
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, translation)

# Creating Tkinter window
root = tk.Tk()
app = TranslatorApp(root)
root.mainloop()