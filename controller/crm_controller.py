from model.crm import crm
from view import terminal as view


msg = ""

def capitalize_list_elements(data):
    return list(map(lambda element : element.capitalize(), data))
    

def list_customers():
    # view.print_error_message("Not implemented yet.")
    view.print_message("\nThe list of customers:")
    customers = crm.get_customers()
    
    for index, customer in enumerate(customers):
        customers[index].insert(0, str(index + 1))

    # header = crm.HEADERS
    # header.insert(0, "Lp")
    header = ["Lp"]
    header.extend(crm.HEADERS)
    
    customers.insert(0, header)
    
    view.print_table(customers)


def add_customer():
    # view.print_error_message("Not implemented yet.")
    view.print_message("\nPlease, provide the new customer's data:")
    headers = capitalize_list_elements(crm.HEADERS[1:])
    new_customer_data = view.get_inputs(headers)

    crm.add_customer(new_customer_data)


def save_cursor():
    print("\033[s", end="")


def restore_cursor():
    print("\033[u", end="")
    

def clean_line():
    print("\033[0K", end="")


def get_customer_lp(action_type):
    global msg
    
    entries_number = crm.get_entries_number()
    
    if entries_number == 0:
        view.print_error_message("There is no entries to update.")
        return
    
    customer_lp = view.get_input(f"\nPlease, provide the Lp number of the customer whose data you want to {action_type} or [c] to cancel")
    
    if customer_lp == "":
        msg = "You must provide a digit."
    elif customer_lp == "c":
        return None
    elif not customer_lp.isdigit():
        msg = "You must provide a digit."
        return None
    else:
        customer_lp = int(customer_lp)
        
    if customer_lp not in range(1, entries_number + 1):
        msg = f"The Lp number must be in the range between: {1} and {entries_number}"
        return None
    
    return customer_lp


def update_customer():
    global msg
    NAME_INDEX = 1
    
    all_customers = crm.get_customers()
    customer_lp = get_customer_lp("update")
    if customer_lp is None:
        return
    
    view.print_message("\nPlease, provide updated customer's data.")
    view.print_message("Press ENTER if you want to keep the value.")
    
    header = crm.HEADERS[NAME_INDEX:]
    header = capitalize_list_elements(header)
    
    for index, customer_data in enumerate(all_customers[customer_lp - 1][NAME_INDEX:]):
        header[index] += f" ({customer_data})"
    
    update_customer_data = None
    while update_customer_data is None:
        print("")
        update_customer_data = [str(customer_lp)]
        update_customer_data.extend(view.get_inputs(header))
        
        for index, value in enumerate(update_customer_data):
            if value == "":
                update_customer_data[index] = all_customers[customer_lp - 1][index + NAME_INDEX]
        
        header.insert(0, "Lp")
        update_customer_data_table = [header, update_customer_data]
        print("")
        view.print_table(update_customer_data_table)
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
                update_customer_data = None
            elif user_input == "y":
                crm.update_customer(update_customer_data)
            

def delete_customer():
    # view.print_error_message("Not implemented yet.")
    global msg
    customer_lp = get_customer_lp("delete")
    
    if customer_lp is None:
        return
    
    crm.delete_customer(customer_lp)


def get_subscribed_emails():
    # view.print_error_message("Not implemented yet.")
    emails = crm.get_subscribed_emails()
    view.print_general_results(emails, "\nSubscribed emails")


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    global msg
    operation = None
    while operation != '0':
        display_menu()
        if msg != "":
            view.print_error_message(msg)
            msg = ""
            
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
