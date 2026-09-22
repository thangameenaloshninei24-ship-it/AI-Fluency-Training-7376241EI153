def calculate_food_expenses():
    total = 0

    with open("expenses.txt", "r") as file:
        for line in file:
            category, amount = line.strip().split(",")
            
            if category == "Food":
                total += int(amount)

    return total


total = calculate_food_expenses()

print("Food expenses:", total)