from model.crm import crm
from view import terminal as view


def list_customers():
    # view.print_error_message("Not implemented yet.")
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
    new_customer_data = view.get_inputs(crm.HEADERS[1:])
    crm.add_customer(new_customer_data)


def save_cursor():
    print("\033[s", end="")


def restore_cursor():
    print("\033[u", end="")
    

def clean_line():
    print("\033[0K", end="")


def update_customer():
    # view.print_error_message("Not implemented yet.")
    
    # header = crm.HEADERS[1:]
    # header.insert(0, "Lp")
    entries_number = crm.get_entries_number()
    
    if entries_number == 0:
        view.print_error_message("There is no entries to update.")
        return
    
    header = ["Lp"]
    header.extend(crm.HEADERS[1:])
    header = list(map(lambda element : element.capitalize(), header))
    
    update_customer_data = None
    while update_customer_data is None:
        print("")
        update_customer_data = view.get_inputs(header)
        
        if update_customer_data[0] not in range(1, entries_number + 1):
            view.print_error_message(f"The Lp number must be in the range between: {1} and {entries_number}")
            continue
        
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
    customer_lp = None
    
    while customer_lp is None:
        customer_lp = view.get_input("Provide the lp of the customer to delete or input [c] to cancel")
        
        if customer_lp == "":
            customer_lp = None
        elif not customer_lp.isdigit():
            customer_lp = None
            view.print_error_message("The customer lp must be a digit.")
        elif customer_lp == "c":
            pass
        else:
            try:
                crm.delete_customer(customer_lp)
            except IndexError:
                view.print_error_message("Customer lp out of range.")
                customer_lp = None


def get_subscribed_emails():
    # view.print_error_message("Not implemented yet.")
    emails = crm.get_subscribed_emails()
    view.print_general_results(emails, "Subscribed emails")


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
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
