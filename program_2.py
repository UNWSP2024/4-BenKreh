user_inputs = []

def get_tickets():
    global user_inputs

    while True:
        value = input("please input the name of the movie AND the tickets required (or type 'done')")
        user_inputs.append(value)

        if value.lower() == "done":
            break

        user_inputs.extend(value.split())

def sum_ticket_numbers():
    total_tickets = sum(int(x) for x in user_inputs if x.isdigit())
    return total_tickets

get_tickets()
print("Total movies and tickets:", user_inputs)
print("Sum of ticket numbers:", sum_ticket_numbers())
