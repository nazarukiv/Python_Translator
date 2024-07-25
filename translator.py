from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import googletrans
from textblob import TextBlob

root = Tk()
root.title("Translator")
root.geometry("1080x400")


def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)


def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END).strip()
        c2 = combo1.get()
        c3 = combo2.get()

        print(f"Original text: {text_}")
        print(f"From language: {c2}")
        print(f"To language: {c3}")

        if text_:
            words = TextBlob(text_)
            lan = words.detect_language()
            lan_ = None
            for i, j in language.items():
                if j == c3:
                    lan_ = i
                    break

            print(f"Detected language: {lan}")
            print(f"Target language code: {lan_}")

            if lan_:
                words = words.translate(from_lang=lan, to=lan_)
                text2.delete(1.0, END)
                text2.insert(END, str(words))
            else:
                messagebox.showerror("Translation Error", "Unable to detect target language code.")
    except Exception as e:
        print(e)
        messagebox.showerror("googletrans", "Please try again")


# Icon
image_icon = PhotoImage(
    file='/Users/ivan/Desktop/coding/programming/petprojects/Python_Translator/Google_Translate_Icon.png')
root.iconphoto(False, image_icon)

# Load and resize the arrow image
arrow_image = Image.open("/Users/ivan/Desktop/coding/programming/petprojects/Python_Translator/arrow.png")
arrow_image = arrow_image.resize((60, 60), Image.LANCZOS)
arrow_photo = ImageTk.PhotoImage(arrow_image)

# Display the resized arrow image
image_label = Label(root, image=arrow_photo, width=60, height=60)
image_label.place(x=500, y=150)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()


# Function to update labels based on combobox selection
def update_label1(event):
    label1.config(text=combo1.get())


def update_label2(event):
    label2.config(text=combo2.get())


combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state='readonly')
combo1.place(x=110, y=20)
combo1.set("English")
combo1.bind("<<ComboboxSelected>>", update_label1)

label1 = Label(root, text="English", font="segoe 30 bold", bg='white', width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg='white', fg='black', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state='readonly')
combo2.place(x=700, y=20)
combo2.set("Select language")
combo2.bind("<<ComboboxSelected>>", update_label2)

label2 = Label(root, text="Select language", font="segoe 30 bold", bg='white', width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Roboto 20", bg='white', fg='black', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                   activebackground='purple', cursor='hand2', bd=5,
                   bg='red', fg='white', command=translate_now)
translate.place(x=480, y=250)

root.configure(bg='white')
root.mainloop()
