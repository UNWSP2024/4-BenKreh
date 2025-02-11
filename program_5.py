def get_total():
    total = 0.0
    budget = float(input("Input your total budget for the month"))

    while True:
        user_input = input("Enter Your expenses one at a time (0.00) (or type done to finish):")

        if user_input.lower() == "done":
            break

        try:
            expenses = float(user_input)
            total += expenses

        except ValueError:
            print("Invalid input, please enter a number or 'done'.")

    return budget - total




total_price = get_total()
if total_price > 0:
    print(f"Your total is ${total_price:.2f} You are on budget!")
else:
    print(f"Your total is ${total_price:.2f} You spent to much :'(")
