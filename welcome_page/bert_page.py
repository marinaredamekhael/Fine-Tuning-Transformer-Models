from pathlib import Path
from models import BERT ,mapping_value

from tkinter import Canvas, Entry, Button, PhotoImage,Toplevel,Label,font


def bert_window(window):
    def open_home():
        window.deiconify()  # Re-show the main window
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets1/frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def retrieve_input():
        input_value = entry_1.get()
        # Assuming BERT and mapping_value are predefined functions:
        value = BERT(input_value)
        result_map = mapping_value(value)
        result_label.config(text=result_map)

    bert_page = Toplevel()
    bert_page.title("Page bert")
    bert_page.geometry("950x600")
    bert_page.images = []  # List to hold image references to prevent garbage collection

    canvas_bert = Canvas(bert_page, bg="#FFFFFF", height=600, width=950, bd=0, highlightthickness=0, relief="ridge")
    canvas_bert.place(x=0, y=0)

    # Load and place images
    for i in range(1, 7):
        img = PhotoImage(file=relative_to_assets(f"image_{i}.png"))
        bert_page.images.append(img)  # Store reference to prevent garbage collection
        if i==2:
            x,y=125,44
        elif i < 5:
            x, y = [125, 44, 128, 358][i - 1], [300, 44, 122, 142][i - 1]
        elif i == 5:
            x, y = 126, 302
        else:
            x, y = 590, 98
        canvas_bert.create_image(x, y, image=img)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    bert_page.images.append(button_image_1)  # Store reference
    button_1 = Button(bert_page, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: [bert_page.destroy(), open_home()], relief="flat")
    button_1.place(x=0.0, y=487.0, width=250.0, height=50.0)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    bert_page.images.append(entry_image_1)  # Store reference
    entry_bg_1 = canvas_bert.create_image(603.5, 263.0, image=entry_image_1)
    entry_1 = Entry(bert_page, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_1.place(x=397.0, y=195.0, width=413.0, height=134.0)

    # Buttons and labels
    submit_button = Button(bert_page, text="Submit", command=retrieve_input, cursor='heart', font=('Helvetica', 12, 'bold'), bg='#4A90E2', fg='black', activebackground='#357ABD', activeforeground='black', padx=10, pady=5, borderwidth=2, relief="raised")
    submit_button.place(x=550, y=350)

    result_label = Label(bert_page, text="Analyzing.....", font=font.Font(family='Helvetica', size=12, weight='bold'), bg='white', fg='black', padx=10, pady=5, borderwidth=2, relief="solid")
    result_label.place(x=550, y=390)

    bert_page.resizable(False, False)
    window.withdraw()  # Hide the main window

