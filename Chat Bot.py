import random

rules = {
    "hey": ["Hello!", "Hi there!", "Hey!"],
    "what's your name": ["I'm just a simple chatbot.", "I don't have a name, but you can call me Chatbot.",
                         "I'm your friendly neighborhood chatbot!"],
    "what is AI?":["AI, or artificial intelligence, refers to the simulation of human intelligence by machines, enabling them to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision-making."],
    "what is web development":["The word Web Development is made up of two words, that is: Web: It refers to websites, "
                               "web pages or anything that works over the internet."
                               " Development: It refers to building the application from scratch"],
    "what is ML": ["Machine learning (ML) is a branch of artificial intelligence (AI) and computer science that focuses on the using data "
                  "and algorithms to enable AI "
                  "to imitate the way that humans learn, gradually improving its accuracy."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?",
                "I'm still learning. Can you ask me something else?"]
}


def generate_response(user_input):

    user_input = user_input.lower()

    for pattern, responses in rules.items():
        if pattern in user_input:
            return random.choice(responses)

    return random.choice(rules["default"])


def chat():
    print("Welcome to the Rule-Based Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: " + generate_response(user_input))
            break
        else:
            print("Chatbot: " + generate_response(user_input))

# Run the chatbot
if __name__ == "__main__":
    chat()
