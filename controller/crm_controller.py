from model.crm import crm
from view import terminal as view
from controller import crud_controller


msg = [""]

def list_customers():
    crud_controller.read(crm.data, crm.HEADERS, "The list of customers")


def add_customer():
    crud_controller.create(crm.data, crm.DATAFILE, crm.HEADERS, "Please, provide the new customer's data")


def update_customer():
    crud_controller.update(crm.data, crm.DATAFILE, crm.HEADERS, "Please, provide updated customer's data", msg)


def delete_customer():
    crud_controller.delete(crm.data, crm.DATAFILE, msg)


def get_subscribed_emails():
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
    global msg

    operation = None
    while operation != '0':
        display_menu()
        
        if msg[0] != "":
            print("")
            print(msg[0])
            msg[0] = ""

        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
