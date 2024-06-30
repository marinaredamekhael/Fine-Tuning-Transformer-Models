
from pathlib import Path
from palm_page import gemini
from bert_page import bert_window
from tkinter import Tk, Canvas,Button, PhotoImage
from t5_page import t5_window
from gemini_Sql import gemini_sql

def open_page(button_number,window):
    match button_number:
        case 1:#palm
            gemini(window)
        case 2:
            bert_window(window)
        case 3:
            t5_window(window)  # Change to open t5_window
        case 4:
            gemini_sql(window)
        case 5:
            bert_window(window)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("950x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 950,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    113.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    560.0,
    173.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    105.0,
    136.0,
    image=image_image_3
)

canvas.create_text(
    279.0,
    278.0,
    anchor="nw",
    text='''    Welcome to M²ASK, where advanced language models meet
    everyday tasks and challenges. Experience a new level of 
    interaction—from engaging in meaningful conversations to 
    getting instant feedback analysis and even solving complex coding
    problems, all powered by the latest in artificial intelligence.''',
    fill="#000000",
    font=("Inter ExtraBold", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    585.0,
    528.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(1,window),
    relief="flat"
)
button_1.place(
    x=2.0,
    y=383.0,
    width=224.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(2,window),
    relief="flat"
)
button_2.place(
    x=2.0,
    y=188.0,
    width=224.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(3,window),
    relief="flat"
)
button_3.place(
    x=2.0,
    y=318.0,
    width=224.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_page(4,window),
    relief="flat"
)
button_4.place(
    x=0.0,
    y=253.0,
    width=224.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_5.place(
    x=0.0,
    y=41.0,
    width=224.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
