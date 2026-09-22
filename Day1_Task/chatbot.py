def chatbot(question):
    private_data = """
    Food: 500
    Transport: 200
    Food: 300
    Entertainment: 400
    Food: 250
    Transport: 100
    """

    if "food" in question.lower():
        return "Based on the information provided, Food expenses are 1050."

    return "I can answer questions about the provided expense information."


while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    print("Chatbot:", chatbot(question))