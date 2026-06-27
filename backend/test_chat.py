from backend.chat import ask


while True:

    question = input("\nYou: ")

    if question.lower() in [
        "exit",
        "quit"
    ]:
        break

    answer = ask(question)

    print()

    print("AI:")

    print(answer)
