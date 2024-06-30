from pathlib import Path
from models import summarize_text

from tkinter import Canvas, Entry, Button, PhotoImage, Toplevel, Label, font

def t5_window(window):
    def open_home():
        window.deiconify()  # Re-show the main window

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets2/frame2")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    def retrieve_input():
        input_value = entry_1.get()
        print(f"Input value: {input_value}")  # For debugging purposes
        summary = summarize_text(input_value)
        print(f"Summary: {summary}")  # For debugging purposes
        result_label.config(text=summary)

    t5_page = Toplevel()
    t5_page.title("Page T5")
    t5_page.geometry("950x600")
    t5_page.images = []  # List to hold image references to prevent garbage collection

    canvas_t5 = Canvas(t5_page, bg="#FFFFFF", height=600, width=950, bd=0, highlightthickness=0, relief="ridge")
    canvas_t5.place(x=0, y=0)

    # Load and place images
    for i in range(1, 7):
        img = PhotoImage(file=relative_to_assets(f"image_{i}.png"))
        t5_page.images.append(img)  # Store reference to prevent garbage collection
        if i == 2:
            x, y = 125, 44
        elif i < 5:
            x, y = [125, 44, 128, 358][i - 1], [300, 44, 122, 142][i - 1]
        elif i == 5:
            x, y = 126, 302
        else:
            x, y = 590, 98
        canvas_t5.create_image(x, y, image=img)

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    t5_page.images.append(button_image_1)  # Store reference
    button_1 = Button(t5_page, image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: [t5_page.destroy(), open_home()], relief="flat")
    button_1.place(x=0.0, y=487.0, width=250.0, height=50.0)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    t5_page.images.append(entry_image_1)  # Store reference
    entry_bg_1 = canvas_t5.create_image(603.5, 263.0, image=entry_image_1)
    entry_1 = Entry(t5_page, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
    entry_1.place(x=397.0, y=195.0, width=413.0, height=134.0)

    # Buttons and labels
    submit_button = Button(t5_page, text="Submit", command=retrieve_input, cursor='heart', font=('Helvetica', 12, 'bold'), bg='#4A90E2', fg='black', activebackground='#357ABD', activeforeground='black', padx=10, pady=5, borderwidth=2, relief="raised")
    submit_button.place(x=550, y=350)

    result_label = Label(t5_page, text="Summarizing...", font=font.Font(family='Helvetica', size=12, weight='bold'), bg='white', fg='black', padx=10, pady=5, borderwidth=2, relief="solid")
    result_label.place(x=525, y=390)

    t5_page.resizable(False, False)
    window.withdraw()  # Hide the main window
