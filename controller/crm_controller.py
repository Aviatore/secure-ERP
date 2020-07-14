from model.crm import crm
from view import terminal as view
from model import crud
from controller import crud_controller


def list_customers():
    # view.print_error_message("Not implemented yet.")
    crud_controller.read(crm.data_manager.read_table_from_file(crm.DATAFILE), crm.HEADERS, crud.function_get, "The list of customers:")


def add_customer():
    # view.print_error_message("Not implemented yet.")
    crud_controller.create(crm.data_manager.read_table_from_file(crm.DATAFILE), crm.DATAFILE, crm.HEADERS, "Add a customer:", crud.function_add)


def update_customer():
    view.print_error_message("Not implemented yet.")


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
