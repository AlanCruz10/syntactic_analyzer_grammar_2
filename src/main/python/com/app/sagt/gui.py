from pathlib import Path
from syntactic_analyzer import analyze_syntax
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\exala\Documents\proyectos\projects-8\python\syntactic_analyzer_grammar_2\src\main\python\com\app\sagt\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def analyze(entry_1, entry_2):
    entry_2.delete('1.0', END)
    report = analyze_syntax(entry_1.get())
    entry_2.insert(END, report)


def show_window():
    window = Tk()

    window.geometry("562x418")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(window, bg="#FFFFFF", height=418, width=562, bd=0, highlightthickness=0, relief="ridge")

    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(281.0, 209.0, image=image_image_1)

    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(216.0, 114.0, image=image_image_2)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(216.0, 114.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_1.place(x=31.0, y=95.0, width=370.0, height=37.0)

    image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(281.0, 263.0, image=image_image_3)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(281.5, 263.5, image=entry_image_2)
    entry_2 = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
    entry_2.place(x=38.0, y=186.0, width=487.0, height=153.0)

    # button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    # button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0,
    #                   command=lambda: print("button_2 clicked"), relief="flat")
    # button_1.place(x=239.0, y=361.0, width=95.0, height=25.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0,
                      command=lambda: analyze(entry_1, entry_2), relief="flat")
    button_2.place(x=445.0, y=102.0, width=95.0, height=25.0)

    window.resizable(False, False)
    window.mainloop()
