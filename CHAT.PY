# TASK 4: Basic Chatbot

def chatbot_response(user_input):
    # Convert to lowercase for consistent comparison
    user_input = user_input.lower()

    # Predefined responses using if-elif
    if user_input in ["hi", "hello", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm just a Python bot, but I'm doing great! 😊"
    elif user_input in ["what is your name", "who are you"]:
        return "my name is base eco made only for basic talks!"
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"
    else:
        return "I'm not sure how to respond to that 🤔"

# --- Main Program Loop ---
print("🤖 CodeAlpha Basic Chatbot")
print("Type something (like 'hello', 'how are you') or 'bye' to exit.\n")

while True:
    user_message = input("You: ")

    # Check for exit condition
    if user_message.lower() in ["bye", "exit", "quit"]:
        print("Bot:", chatbot_response(user_message))
        break

    # Get chatbot reply
    bot_reply = chatbot_response(user_message)
    print("Bot:", bot_reply)
