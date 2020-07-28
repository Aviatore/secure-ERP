from model.sales import sales
from view import terminal as view
from controller import crud_controller


msg = [""]


def list_transactions():
    crud_controller.read(sales.DATAFILE, sales.HEADERS, "The list of transactions:")


def add_transaction():
    crud_controller.create(sales.DATAFILE, sales.HEADERS, "Add a transaction:")


def update_transaction():
    crud_controller.update(sales.DATAFILE, sales.HEADERS, "Update transaction", msg)


def delete_transaction():
    crud_controller.delete(sales.DATAFILE, msg)


def get_biggest_revenue_transaction():
    revenue_transaction = sales.get_biggest_revenue_transaction()
    view.print_general_results(revenue_transaction, "Biggest revenue transaction.")


def get_biggest_revenue_product():
    revenue_product = sales.get_biggest_revenue_product()
    view.print_general_results(revenue_product, "Biggest revenue product.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions()
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum the price of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
