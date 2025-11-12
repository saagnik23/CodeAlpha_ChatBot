def get_bot_response(user_input):
    """Function to generate bot responses based on user input"""
    # Convert input to lowercase for easier matching
    user_input = user_input.lower().strip()

    # Greeting responses
    if user_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi! How can I help you today?"

    # How are you responses
    elif user_input in ["how are you", "how's it going", "what's up"]:
        return "I'm fine, thanks! How about you?"

    # User's wellbeing responses
    elif user_input in ["i'm good", "i'm fine", "good", "great", "fine", "i am good"]:
        return "That's great to hear! What can I do for you?"

    elif user_input in ["i'm bad", "not good", "bad", "sad", "i am sad"]:
        return "I'm sorry to hear that. I hope things get better soon!"

    # Name-related responses
    elif user_input in ["what is your name", "what's your name", "your name"]:
        return "I'm Saerion a ChatBot, your friendly assistant!"

    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        return f"Nice to meet you, {name.title()}!"

    # Help responses
    elif user_input in ["help", "help me", "can you help"]:
        return "Sure! I can chat with you. Try asking me how I am or saying hello!"

    # Age responses
    elif user_input in ["how old are you", "your age", "what is your age"]:
        return "I'm just a program, so I don't have an age!"

    # Thank you responses
    elif user_input in ["thank you", "thanks", "thank you very much", "thx"]:
        return "You're welcome! Happy to help!"

    # Joke request
    elif user_input in ["tell me a joke", "joke", "make me laugh"]:
        return "Why don't programmers like nature? It has too many bugs! 🐛", "Rule no 1. If the code is working don't touch it."

    # Time/Date (simplified)
    elif user_input in ["what time is it", "time", "what's the time"]:
        return "I don't have access to real-time data, but you can check your device!☺️"

    # Goodbye responses
    elif user_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! Have a great day!👋"

    # Default response for unrecognized input
    else:
        return "I'm not sure I understand. Can you rephrase that or type 'help' for options?"


def display_welcome():
    """Display welcome message"""
    print("=" * 50)
    print("        WELCOME TO CHATBOT!")
    print("=" * 50)
    print("Type 'bye' or 'exit' to end the conversation.")
    print("Type 'help' to see what I can do.\n")


def display_help():
    """Display available commands"""
    print("\n--- Things you can say: ---")
    print("• Greetings: hello, hi, hey")
    print("• Questions: how are you, what's your name")
    print("• Requests: help, tell me a joke")
    print("• Exit: bye, goodbye, exit")
    print("• And more! Just try chatting with me!\n")


def main():
    """Main chatbot function"""
    display_welcome()

    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check if user wants to exit
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Bot:", get_bot_response(user_input))
            break

        # Check if input is empty
        if not user_input:
            print("Bot: Please say something!\n")
            continue

        # Special case for help command
        if user_input.lower() == "help":
            display_help()
            continue

        # Get and display bot response
        response = get_bot_response(user_input)
        print(f"Bot: {response}\n")

    print("\nThanks for chatting! See you next time! 👋")


# Run the chatbot
if __name__ == "__main__":
    main()