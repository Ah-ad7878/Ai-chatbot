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
        "what is software development": "Software development is the process of creating software applications.",
        "what is frontend development": "Frontend development focuses on the user interface of websites and apps.",
        "what is backend development": "Backend development handles servers, databases, and application logic.",
        "what is full stack development": "Full stack development includes both frontend and backend development.",
        "what is html": "HTML is used to create the structure of web pages.",
        "what is css": "CSS is used to style web pages.",
        "what is javascript": "JavaScript adds interactivity to websites.",
        "what is react": "React is a JavaScript library for building user interfaces.",
        "what is django": "Django is a Python framework for web development.",
        "what is flask": "Flask is a lightweight Python web framework.",
        "what is api": "API stands for Application Programming Interface.",
        "what is database": "A database stores and manages data.",
        "what is sql": "SQL is used to manage and query databases.",
        "what is git": "Git is a version control system used by developers.",
        "what is github": "GitHub is a platform for hosting and sharing code.",
        "what is debugging": "Debugging means finding and fixing errors in code.",
        "what is bug": "A bug is an error or problem in a program.",
        "what is programming": "Programming is writing instructions for computers.",
        "what is machine learning": "Machine learning allows computers to learn from data.",
        "what is artificial intelligence": "Artificial Intelligence enables machines to simulate human intelligence.",
        "what is mobile app development": "Mobile app development is creating apps for smartphones.",
        "what is web development": "Web development is building websites and web applications.",
        "what is software engineer": "A software engineer designs and develops software systems.",
        "what is algorithm": "An algorithm is a step-by-step solution to a problem.",
        "what is data structure": "Data structures organize and store data efficiently.",
        "what is oop": "OOP stands for Object-Oriented Programming.",
        "what is python used for": "Python is used for web development, AI, automation, and more.",
        "what is java": "Java is a popular object-oriented programming language.",
        "what is c++": "C++ is a powerful programming language used in games and systems.",
        "what is software testing": "Software testing checks if software works correctly.",
        "what is electrical engineering": "Electrical engineering is the study of electricity, electronics, and power systems.",
        "what is voltage": "Voltage is the electrical pressure that pushes current through a circuit.",
        "what is current": "Current is the flow of electric charge in a circuit.",
        "what is resistance": "Resistance opposes the flow of electric current.",
        "what is ohms law": "Ohm's Law states that V = I × R.",
        "what is power in electricity": "Electrical power is calculated using P = V × I.",
        "what is ac": "AC stands for Alternating Current.",
        "what is dc": "DC stands for Direct Current.",
        "what is transformer": "A transformer changes voltage levels in AC circuits.",
        "what is generator": "A generator converts mechanical energy into electrical energy.",
        "what is motor": "An electric motor converts electrical energy into mechanical energy.",
        "what is capacitor": "A capacitor stores electrical energy temporarily.",
        "what is inductor": "An inductor stores energy in a magnetic field.",
        "what is circuit": "A circuit is a path through which electricity flows.",
        "what is pcb": "PCB stands for Printed Circuit Board.",
        "what is diode": "A diode allows current to flow in one direction only.",
        "what is transistor": "A transistor is used to amplify or switch electronic signals.",
        "what is relay": "A relay is an electrically operated switch.",
        "what is fuse": "A fuse protects circuits from excessive current.",
        "what is battery": "A battery stores chemical energy and converts it to electrical energy.",
        "what is solar panel": "A solar panel converts sunlight into electricity.",
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
