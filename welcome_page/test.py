import tkinter as tk
from tkinter import scrolledtext
from models import palm
# Function to handle the response generation
def generate_response():
    response_text.insert(tk.END,"This is a generated response.")

# Create the main window
root = tk.Tk()
root.title("Welcome to Gemini")
root.geometry("800x600")

# Top frame for the logo and introduction text
top_frame = tk.Frame(root, bg="lightgray")
top_frame.pack(side=tk.TOP, fill=tk.X)

# Logo
logo = tk.PhotoImage(file="/Users/apple/Desktop/ml_text_minig_project/pl.png")  # Replace with the path to your logo image
logo_label = tk.Label(top_frame, image=logo, bg="lightgray")
logo_label.pack(side=tk.LEFT, padx=10, pady=10)

# Introduction text
intro_text = "PaLM AI, short for Pathways Language Model, is an advanced language model developed by Google Research. It leverages state-of-the-art machine learning techniques to understand and generate human-like text, making it a powerful tool for various applications, including natural language processing (NLP), conversational agents, and information retrieval. One of the most popular applications of PaLM AI is in conversational agents or chatbots. Here’s how users can utilize PaLM AI for chatting."
intro_label = tk.Label(top_frame, text=intro_text, justify=tk.LEFT, wraplength=300, bg="lightgray", anchor="w")
intro_label.pack(side=tk.LEFT, padx=10, pady=10)

# Right frame for the chatbot interface
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Chatbot response area
response_label = tk.Label(right_frame, text="Response", font=("Arial", 14))
response_label.pack(pady=10)

response_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, height=10, width=50)
response_text.pack(pady=10)

# Entry for new question
question_label = tk.Label(right_frame, text="Enter new question", font=("Arial", 14))
question_label.pack(pady=10)

question_entry = tk.Entry(right_frame, font=("Arial", 12), width=50)
question_entry.pack(pady=10)

# Entry for replying to the response
reply_label = tk.Label(right_frame, text="Replay on the response", font=("Arial", 14))
reply_label.pack(pady=10)

reply_entry = tk.Entry(right_frame, font=("Arial", 12), width=50)
reply_entry.pack(pady=10)

# Button to generate response
generate_button = tk.Button(right_frame, text="Generate Response", command=generate_response, font=("Arial", 12))
generate_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
