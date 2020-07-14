from view import terminal as view


def save_cursor():
    print("\033[s", end="")


def restore_cursor():
    print("\033[u", end="")
    

def clean_line():
    print("\033[0K", end="")


def get_data_lp(data, function_get_entries_number, action_type, msg):   
    entries_number = function_get_entries_number(data)
    
    if entries_number == 0:
        view.print_error_message("There is no entries to update.")
        return
    
    customer_lp = view.get_input(f"Please, provide the Lp number of the customer whose data you want to {action_type} or [c] to cancel")
    
    if customer_lp == "":
        msg[0] = "You must provide a digit."
        return None
    elif customer_lp == "c":
        return None
    elif not customer_lp.isdigit():
        msg[0] = "You must provide a digit."
        return None
    else:
        customer_lp = int(customer_lp)
        
    if customer_lp not in range(1, entries_number + 1):
        msg[0] = f"The Lp number must be in the range between: {1} and {entries_number}"
        return None
    
    return customer_lp


def capitalize_list_elements(data):
    return list(map(lambda element : element.capitalize(), data))


def create(data, data_file, headers, label, function_add):
    # view.print_error_message("Not implemented yet.")
    view.print_message(f"{label}:")
    headers = capitalize_list_elements(headers[1:])
    new_data = view.get_inputs(headers)

    function_add(data, data_file, new_data)


def read(data, headers, function_get, label):
    view.print_message(f"{label}:")
    data = function_get(data)
    number_of_elements = len(data)
    
    for index in range(number_of_elements):
        data[index].insert(0, str(index + 1))

    header = ["Lp"]
    header.extend(headers)
    
    data.insert(0, header)
    
    view.print_table(data)


def update(data, data_file, headers, label, function_get_entries_number, function_get, function_update, msg):
    NAME_INDEX = 1
    
    old_data = function_get(data)
    data_lp = get_data_lp(data, function_get_entries_number, "update", msg)
    if data_lp is None:
        return
    
    view.print_message(f"{label}:")
    view.print_message("Press ENTER if you want to keep the value.")
    
    header = headers[NAME_INDEX:]
    header = capitalize_list_elements(header)
    
    for index, customer_data in enumerate(old_data[data_lp - 1][NAME_INDEX:]):
        header[index] += f" ({customer_data})"
    
    update_data = None
    while update_data is None:
        print("")
        update_data = [str(data_lp)]
        update_data.extend(view.get_inputs(header))
        
        for index, value in enumerate(update_data):
            if value == "":
                update_data[index] = old_data[data_lp - 1][index + NAME_INDEX]
        
        header.insert(0, "Lp")
        update_data_table = [header, update_data]
        print("")
        view.print_table(update_data_table)
        print("")
        save_cursor()
        user_input = None
        while user_input is None:
            restore_cursor()
            clean_line()
            
            user_input = view.get_input("Are the above values correct? [y]es [n]o")

            if user_input == "":
                user_input = None
            elif len(user_input) > 1:
                user_input = None
            elif user_input not in ["y", "n"]:
                user_input = None
            elif user_input == "n":
                update_data = None
            elif user_input == "y":
                function_update(data, data_file, update_data)


def delete(data, data_file, function_get_entries_number, function_delete, msg):
    data_lp = get_data_lp(data, function_get_entries_number, "delete", msg)
    
    if data_lp is None:
        return
    
    function_delete(data, data_file, data_lp)
