# Simple Rule-Based Chatbot - Short Version

# Knowledge base (dictionary)
responses = {
    'hello': "Hello! Welcome to DecodeLabs!",
    'hi': "Hi there! Ready to build AI?",
    'how are you': "I'm doing great, thanks!",
    'your name': "I'm ChatBot, your AI assistant!",
    'help': "I understand: hello, hi, how are you, your name, joke, bye",
    'tell me a joke': "Why do programmers prefer dark mode? Light attracts bugs! 😄",
    'bye': None  # Exit signal
}
print("=" * 50)
print("🤖 Rule-Based Chatbot (Type 'bye' to exit)")
print("=" * 50)

while True:
    # Get and clean user input
    user_input = input("\nYou: ").lower().strip()
    
    # Check exit
    if user_input == 'bye':
        print("Bot: Goodbye! Have a great day! 👋")
        break
    
    # Dictionary lookup with fallback
    response = responses.get(user_input, "I don't understand that. Type 'help' for options.")
    
    print(f"Bot: {response}")
