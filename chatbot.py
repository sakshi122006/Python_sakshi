def chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")

        elif "name" in user_input:
            print("Chatbot: I am a simple chatbot.")

        elif "help" in user_input:
            print("Chatbot: I can answer simple questions.")

        else:
            print("Chatbot: Sorry, I didn't understand that.")

chatbot()
