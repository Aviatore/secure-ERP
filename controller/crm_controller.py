from model.crm import crm
from view import terminal as view


def list_customers():
    # view.print_error_message("Not implemented yet.")
    customers = crm.get_customers()
    
    for index, customer in enumerate(customers):
        customers[index].insert(0, str(index + 1))

    header = crm.HEADERS
    header.insert(0, "Lp")
    
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
    
    header = crm.HEADERS[1:]
    header.insert(0, "Lp")
    header = list(map(lambda element : element.capitalize(), header))
    
    update_customer_data = None
    while update_customer_data is None:
        print("")
        update_customer_data = view.get_inputs(header)
        
        update_customer_data_table = [header, update_customer_data]
        print("")
        view.print_table(update_customer_data_table)
        print("")
        save_cursor()
        user_input = None
        while user_input is None:
            restore_cursor()
            clean_line()
            
            user_input = view.get_input("Are the above values correct? [y]es [n]o: ")

            if len(user_input) == "":
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
    view.print_error_message("Not implemented yet.")


def get_subscribed_emails():
    view.print_error_message("Not implemented yet.")


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
