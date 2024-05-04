import re

class RuleBasedChatbot:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
        self.inquiries = ["how are you?", "what's up?", "how's it going?", "how's your day?"]
        self.farewells = ["bye", "goodbye", "see you later", "take care"]
        self.default_responses = [
            "I'm sorry, I didn't understand that. Can you please rephrase?",
            "Hmm, I'm not sure what you mean. Could you try asking again?",
            "Sorry, I'm just a chatbot and can't understand everything. Can you ask something else?",
            "I'm here to help! What else would you like to know?"
        ]

    def respond(self, user_input):
        # Convert user input to lowercase for case-insensitive matching
        user_input = user_input.lower()

        # Check if user input matches greetings
        if any(greeting in user_input for greeting in self.greetings):
            return "Hello! How can I assist you today?"

        # Check if user input matches inquiries
        elif any(inquiry in user_input for inquiry in self.inquiries):
            return "I'm just a chatbot, but I'm here to help you with any questions you have!"

        # Check if user input matches farewells
        elif any(farewell in user_input for farewell in self.farewells):
            return "Goodbye! Have a great day!"

        # Check if user input contains numbers
        elif any(char.isdigit() for char in user_input):
            return "It seems like you mentioned numbers. How can I assist you further?"

        # Check if user input contains specific keywords
        elif re.search(r'\b(help|assistance)\b', user_input):
            return "Of course! What do you need help with?"

        # Default response if no match is found
        else:
            return self.default_responses[random.randint(0, len(self.default_responses) - 1)]

# Test the chatbot
if __name__ == "__main__":
    chatbot = RuleBasedChatbot()
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
