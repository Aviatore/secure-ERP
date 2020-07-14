from view import terminal as view
from model import crud



def save_cursor():
    print("\033[s", end="")


def restore_cursor():
    print("\033[u", end="")
    

def clean_line():
    print("\033[0K", end="")


def function_get_entries_number(data):
    return len(data)


def get_data_lp(data, action_type, msg=None):   
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


def create(data, data_file, headers, label):
    # view.print_error_message("Not implemented yet.")
    view.print_message(f"{label}:")
    headers = capitalize_list_elements(headers[1:])
    new_data = view.get_inputs(headers)

    crud.function_add(data, data_file, new_data)


def read(data, headers, label):
    view.print_message(f"{label}:")
    data = crud.function_get(data)
    number_of_elements = len(data)
    
    for index in range(number_of_elements):
        data[index].insert(0, str(index + 1))

    header = ["Lp"]
    header.extend(headers)
    
    data.insert(0, header)
    
    view.print_table(data)


def copy_list(data):
    new_list = []

    for line in data:
        new_list.append(line)

    return new_list


def update(data, data_file, headers, label, msg=None):
    NAME_INDEX = 1
    
    old_data = crud.function_get(data)
    data_lp = get_data_lp(data, "update", msg)
    if data_lp is None:
        return
    
    view.print_message(f"{label}:")
    view.print_message("Press ENTER if you want to keep the value.")
    
    header = headers[NAME_INDEX:]
    header_capitalized = capitalize_list_elements(header)
    
    for index, customer_data in enumerate(old_data[data_lp - 1][NAME_INDEX:]):
        header_capitalized[index] += f" ({customer_data})"
    
    update_data = None
    while update_data is None:
        header = headers[NAME_INDEX:]

        update_data = view.get_inputs(header_capitalized)
        
        for index, value in enumerate(update_data):
            if value == "":
                update_data[index] = old_data[data_lp - 1][index + NAME_INDEX]
        
        update_data.insert(0, str(data_lp))
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
                crud.function_update(data, data_file, update_data)


def delete(data, data_file, msg=None):
    data_lp = get_data_lp(data, "delete", msg)
    
    if data_lp is None:
        return
    
    crud.function_delete(data, data_file, data_lp)
