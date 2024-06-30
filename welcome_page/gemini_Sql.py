from pathlib import Path
from PIL import Image, ImageTk
from tkinter import Canvas, Entry, Button, PhotoImage,Toplevel,Label,font
from models import execute_sql ,gemini,extract_sql_query,parse_records_to_table

def gemini_sql(window):
    def open_home():
        window.deiconify()  # Re-show the main window

    # def submit_reply():
    #     request = reply_entry.get()
    #     result = palm(request, 'reply')
    #     response_text.delete(1.0, tk.END)
    #     response_text.insert(tk.END, result)

    def submit_question():
        request = question_entry.get()
        sql_query = extract_sql_query(gemini(request))
        attibutes,results = execute_sql(sql_query)
        if attibutes==None:
            response_text.delete(1.0, tk.END)
            response_text.insert(tk.END,"Query executed successfully.")
        else:
            response_text.delete(1.0, tk.END)
            response_text.insert(tk.END,parse_records_to_table(results,attibutes))

    import tkinter as tk
    palm_page=Toplevel()
    palm_page.configure(bg="white")  # Set the background color to white

    palm_page.title("Welcome to Gemini")
    palm_page.geometry("950x600")

    top_frame = tk.Frame(palm_page, bg="white")
    top_frame.place(x=0, y=0, width=270, height=600)

    image_path = "/Users/apple/Desktop/ml_text_minig_project/sql.png"  # Replace with your image path
    image = Image.open(image_path)
    image = image.resize((270, 100), Image.LANCZOS)  # Resize the image as needed
    photo = ImageTk.PhotoImage(image)

    # Create a label for the image
    image_label = tk.Label(top_frame, image=photo, bg="#D9D9D9")
    image_label.image = photo  # Keep a reference to the image to prevent garbage collection
    image_label.place(x=0, y=0)  # Adjust x and y to position the image within the frame

    # Create a label for the text
    text_label = tk.Label(top_frame, text="Gemini, an advanced tool for\n database management, is\ndeveloped to streamline complex\ntasks and enhance data handling\nefficiency.Leveraging cutting-edge\n machine learning algorithms,\n it provides robust solutions\n for organizing, querying, and\n maintaining large datasets.\n Gemini is highly versatile,\nsupporting various database systems\n and ensuring data integrity and\nsecurity. One of the most\n popular applications of Gemini\nis in control and automation\nof database tasks.\nHere’s how users can utilize\n Gemini for effective\ndatabase management.", bg="#D9D9D9",fg="black", font=("Helvetica", 17))
    text_label.place(x=0, y=105)

    image_path = "ml_app/welcome_page/button_1.png"  # Replace with your image path
    button_image = Image.open(image_path)
    button_image = button_image.resize((270, 45), Image.LANCZOS)  # Resize the image if needed
    button_photo = ImageTk.PhotoImage(button_image)

    # Create a button with the image
    button_1 = tk.Button(top_frame, image=button_photo, borderwidth=0, highlightthickness=0,
                        command=lambda: [palm_page.destroy(), open_home()], relief="flat")
    button_1.image = button_photo  # Keep a reference to the image to prevent garbage collection
    button_1.place(x=0, y=500) 

    image_path = "/Users/apple/Desktop/ml_text_minig_project/pp.webp"  # Replace with your image path
    image = Image.open(image_path)
    image = image.resize((100, 100), Image.LANCZOS)  # Resize the image if needed
    photo = ImageTk.PhotoImage(image)

    # Create a label for the image
    image_label = tk.Label(palm_page, image=photo, bg="white")
    image_label.image = photo  # Keep a reference to the image to prevent garbage collection
    image_label.place(y=10,x=530)  # Place the image at the top with some padding

    # Create a label for the text
    text_label = tk.Label(palm_page, text="Welcome to Gemini", bg="white",fg="black", font=("Helvetica", 32))
    text_label.place(y=110,x=450)  # Place the text below the image with some padding

    reply_label = tk.Label(palm_page, text="The response", font=("Arial", 14),bg="white",fg="black")
    reply_label.place(y=150,x=300)
    # Create a text widget for the response area
    response_text = tk.Text(palm_page, bg="lightgray",fg="black", font=("Helvetica", 12), height=10, width=90, wrap="word", padx=10, pady=10)
    response_text.place(x=280,y=170)  # Place the text area with padding
    # Entry for replying to the response
    # reply_label = tk.Label(palm_page, text="Replay on the response", font=("Arial", 14),bg="white",fg="black")
    # reply_label.place(y=350,x=340)

    # reply_entry = tk.Entry(palm_page,bg="lightgray",fg="black", font=("Helvetica", 12), width=73)
    # reply_entry.place(y=370,x=340)

    # reply_button = tk.Button(palm_page, text="Submit Reply",bg="white", command=submit_reply, font=("Helvetica", 12))
    # reply_button.place(y=400,x=390)

    reply_label = tk.Label(palm_page, text="Enter new Question", font=("Arial", 14),bg="white",fg="black")
    reply_label.place(y=450,x=340)

    question_entry = tk.Entry(palm_page,bg="lightgray",fg="black", font=("Helvetica", 12), width=73)
    question_entry.pack(side="top", pady=10, padx=20, ipady=10) 
    question_entry.place(y=470,x=340)

    question_button = tk.Button(palm_page, text="Submit Question",bg="white", command=submit_question, font=("Helvetica", 12))
    question_button.place(y=500,x=530)

    window.withdraw()  