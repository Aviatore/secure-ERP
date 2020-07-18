from model.hr import hr
from view import terminal as view
from controller import crud_controller

msg = [""]


def list_employees():
    crud_controller.read(hr.DATAFILE, hr.HEADERS, "The list of employees:")


def add_employee():
    crud_controller.create(hr.DATAFILE, hr.HEADERS, "Add a employee:")


def update_employee():
    crud_controller.update(hr.DATAFILE, hr.HEADERS, "Update employee", msg)


def delete_employee():
    crud_controller.delete(hr.DATAFILE, msg)


def get_oldest_and_youngest():
    birthday = hr.get_oldest_and_youngest()
    view.print_general_results(birthday, "Oldest and youngest employees")


def get_average_age():
    age = hr.get_average_age()
    view.print_general_results(age, "Average age of employees")


def next_birthdays():
    view.print_error_message("Not implemented yet.")


def count_employees_with_clearance():
    number_of_employees = hr.count_employees_with_clearance()
    view.print_general_results(number_of_employees, "Number of employees with at least given lvl of Clearance")


def count_employees_per_department():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_employees()
    elif option == 2:
        add_employee()
    elif option == 3:
        update_employee()
    elif option == 4:
        delete_employee()
    elif option == 5:
        get_oldest_and_youngest()
    elif option == 6:
        get_average_age()
    elif option == 7:
        next_birthdays()
    elif option == 8:
        count_employees_with_clearance()
    elif option == 9:
        count_employees_per_department()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List employees",
               "Add new employee",
               "Update employee",
               "Remove employee",
               "Oldest and youngest employees",
               "Employees average age",
               "Employees with birthdays in the next two weeks",
               "Employees with clearance level",
               "Employee numbers by department"]
    view.print_menu("Human resources", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
