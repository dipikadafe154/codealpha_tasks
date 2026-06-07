import datetime

print("🤖 Smart ChatBot")
print("Type 'help' for commands.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("🤖 ChatBot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("🤖 ChatBot: I am doing well. How about you?")

    elif user in ["i am fine", "fine", "good", "great"]:
        print("🤖 ChatBot: That's wonderful to hear!")

    elif user == "what is your name":
        print("🤖 ChatBot: My name is Smart ChatBot.")

    elif user == "who created you":
        print("🤖 ChatBot: I was created using Python.")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"🤖 ChatBot: Current time is {current_time}")

    elif user == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"🤖 ChatBot: Today's date is {current_date}")

    elif user == "help":
        print("\n🤖 Available Commands:")
        print("• hello / hi / hey")
        print("• how are you")
        print("• what is your name")
        print("• who created you")
        print("• date")
        print("• time")
        print("• help")
        print("• bye\n")

    elif user == "bye":
        print("🤖 ChatBot: Goodbye! Have a great day. 👋")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand that. Type 'help' to see available commands.")