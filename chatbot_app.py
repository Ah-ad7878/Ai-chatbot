import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# -----------------------------
# Chatbot response function
# -----------------------------
def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you": "I'm doing great!",
        "what is your name": "I'm your AI chatbot.",
        "who made you": "I was created using Python.",
        "what can you do": "I can answer simple questions and chat with you.",
        "bye": "Goodbye! Have a nice day.",
        "time": f"Current time is {datetime.now().strftime('%H:%M:%S')}",
        "date": f"Today's date is {datetime.now().strftime('%d-%m-%Y')}",
        "python": "Python is a powerful programming language.",
        "ai": "AI means Artificial Intelligence.",
        "thank you": "You're welcome!",
        "thanks": "No problem!",
        "what is your favorite color": "I like blue.",
        "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
        "what is computer": "A computer is an electronic machine that processes data.",
        "what is coding": "Coding is writing instructions for computers.",
        "your age": "I don't have an age like humans.",
        "where are you from": "I live inside this Python program.",
        "help": "I can answer questions about programming, AI, and general knowledge. Just ask me anything!",
        "weather": "I don't have access to weather data, but I hope it's nice where you are!",
        "favorite food": "I don't eat, but I love processing data!",
        "machine learning": "Machine Learning is a subset of AI that helps systems learn from data without explicit programming.",
        "hello world": "That's the classic first program! It's a great way to start programming.",
        "see you": "See you later! Feel free to come back anytime.",
        "good morning": "Good morning! I hope you have a great day!",
        "good night": "Good night! Sleep well and sweet dreams!",
        "sorry": "No problem at all! Don't worry about it.",
        "who are you": "I'm an AI chatbot made with Python. I'm here to help and chat with you!",
        "flutter": "Flutter is an open-source UI framework by Google that allows you to build beautiful, natively compiled applications for mobile, web, and desktop from a single codebase.",
        "dart": "Dart is a modern, object-oriented programming language developed by Google. It's designed for building fast, multi-platform applications and is the language used in Flutter.",
        "java": "Java is a widely-used, object-oriented programming language known for its portability and use in building large-scale applications, Android apps, and enterprise software.",
        "iub": "IUB commonly refers to an intrauterine device used for long-term birth control. If you meant something else, feel free to ask with more details.",
        "pakistan university": "Pakistan has many universities, including top national institutions like the National University of Sciences and Technology (NUST), Lahore University of Management Sciences (LUMS), and the University of the Punjab.",
        "pakistan cities": "Major cities in Pakistan include Karachi, Lahore, Islamabad, Rawalpindi, Peshawar, Quetta, and Multan. Each city has its own cultural, economic, and historical importance.",
        "bahawalpur": "Bahawalpur is a historic city in Punjab, Pakistan, known for its palaces, museums, and nearby Cholistan Desert. It is also an important center for agriculture and education in the region.",
        "fuji fertilizer": "Fuji Fertilizer is a brand name associated with agricultural nutrients. It usually refers to products designed to improve crop growth and soil health.",
    }

    for question, answer in responses.items():
        if question in user_input:
            return answer

    return "Sorry, I don't understand that yet."


# -----------------------------
# Send message function
# -----------------------------
def send_message():
    user_message = user_entry.get()

    if user_message.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)

    # Show user message
    chat_area.insert(tk.END, "You: " + user_message + "\n")

    # Bot response
    response = chatbot_response(user_message)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    user_entry.delete(0, tk.END)


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("AI Chatbot App")
root.geometry("500x600")
root.config(bg="#1e1e1e")

# -----------------------------
# Heading
# -----------------------------
heading = tk.Label(
    root,
    text="AI Chatbot",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)
heading.pack(pady=10)

# -----------------------------
# Chat Area
# -----------------------------
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state=tk.DISABLED)

# -----------------------------
# Input Frame
# -----------------------------
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(fill=tk.X, padx=10, pady=10)

# User Entry
user_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# Send Button
send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=send_message
)
send_button.pack(side=tk.RIGHT)

# Press Enter to send
root.bind('<Return>', lambda event: send_message())

# Welcome Message
chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hello! I am your AI chatbot.\n\n")
chat_area.config(state=tk.DISABLED)

# Run App
root.mainloop()
