def read_expenses():
    """Tool: reads the private expense file."""
    with open("expenses.txt", "r") as file:
        return file.read()


def calculate_food_expenses(data):
    """Tool: calculates food expenses."""
    total = 0

    for line in data.splitlines():
        category, amount = line.split(",")

        if category == "Food":
            total += int(amount)

    return total


def agent(user_question):
    print("\nAgent: I need to inspect the private expense data.")

    # Tool 1
    data = read_expenses()

    print("Agent: I used the expense-reading tool.")

    # Tool 2
    if "food" in user_question.lower():
        total = calculate_food_expenses(data)

        print("Agent: I calculated the food expenses.")

        return f"You spent {total} on food."

    return "I don't know how to answer that question yet."


while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = agent(question)

    print("Agent:", answer)