# Simple Rule-Based Chatbot

# Knowledge Base (Dictionary)
responses ={
    # Greetings
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "hey": "Hey! Nice to see you.",
    "good morning": "Good morning! Have a great day ahead.",
    "good afternoon": "Good afternoon!",
    "good evening": "Good evening!",

    # Academic Questions
    "what is python": "Python is a high-level, interpreted programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that enables systems to learn from data.",
    "what is data science": "Data Science is the field of extracting insights from data.",

    # Programming
    "what is a variable": "A variable is a container used to store data values.",
    "what is a loop": "A loop is used to execute a block of code repeatedly.",
    "what is a function": "A function is a reusable block of code that performs a specific task.",
    "what is recursion": "Recursion is when a function calls itself.",

    # Time and Date
    "what day is today": "I cannot check the current day unless programmed to do so.",
    "what time is it": "I cannot access the current time in this version.",

    # Help
    "help": "You can greet me, ask about Python, AI, programming, or tell me to tell a joke.",
    "commands": "Try: hello, what is python, what is ai, tell me a joke, thanks",

    # Farewell
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "bye": "Goodbye! Have a great day!"
}

print("Chatbot: Hello! Type 'bye' or 'exit' to end the conversation.")

# Continuous Input Loop
while True:
    # Input + Sanitization
    user_input = input("You: ").lower().strip()

    # Exit Strategy
    if user_input in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a great day!")
        break

    # Process and Output
    response = responses.get(user_input, "I do not understand.")
    print("Chatbot:", response)