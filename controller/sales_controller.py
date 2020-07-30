from model.sales import sales
from view import terminal as view
from controller import crud_controller


msg = [""]


def list_transactions():
    view.clear_screen()

    crud_controller.read(sales.DATAFILE, sales.HEADERS, "The list of transactions:")


def add_transaction():
    crud_controller.create(sales.DATAFILE, sales.HEADERS, "Add a transaction:")

    input("\nPress ENTER to continue ...")
    view.clear_screen()


def update_transaction():
    crud_controller.update(sales.DATAFILE, sales.HEADERS, "Update transaction", msg)

    input("\nPress ENTER to continue ...")
    view.clear_screen()


def delete_transaction():
    crud_controller.delete(sales.DATAFILE, msg)

    input("\nPress ENTER to continue ...")
    view.clear_screen()


def get_biggest_revenue_transaction():
    view.clear_screen()

    revenue_transaction = sales.get_biggest_revenue_transaction()
    view.print_general_results(revenue_transaction, "Biggest revenue transaction.")


def get_biggest_revenue_product():
    view.clear_screen()

    revenue_product = sales.get_biggest_revenue_product()
    view.print_general_results(revenue_product, "Biggest revenue product.")


def count_transactions_between():
    count_transactions_between = sales.count_transactions_between()
    view.print_general_results(count_transactions_between, "Count transactions between given dates.")

    input("\nPress ENTER to continue ...")
    view.clear_screen()


def sum_transactions_between():
    sum_transactions_between = sales.sum_transactions_between()
    view.print_general_results(sum_transactions_between, "Sum transactions between given dates.")

    input("\nPress ENTER to continue ...")
    view.clear_screen()


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
