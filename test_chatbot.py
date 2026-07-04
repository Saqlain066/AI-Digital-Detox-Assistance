from chatbot import ask_wellness_bot

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask_wellness_bot(question)

    print("\nBot:")
    print(answer)
    print()