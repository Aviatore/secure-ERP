from model.hr import hr
from view import terminal as view
from controller import crud_controller

msg = [""]


def list_employees():
    view.clear_screen()
    
    crud_controller.read(hr.DATAFILE, hr.HEADERS, "The list of employees:")


def add_employee():
    crud_controller.create(hr.DATAFILE, hr.HEADERS, "Add a employee:")
    
    input("\nPress ENTER to continue ...")
    view.clear_screen()


def update_employee():
    crud_controller.update(hr.DATAFILE, hr.HEADERS, "Update employee", msg)
    
    input("\nPress ENTER to continue ...")
    view.clear_screen()


def delete_employee():
    crud_controller.delete(hr.DATAFILE, msg)
    
    input("\nPress ENTER to continue ...")
    view.clear_screen()


def get_oldest_and_youngest():
    view.clear_screen()

    birthday = hr.get_oldest_and_youngest()
    view.print_general_results(birthday, "Oldest and youngest employees")


def get_average_age():
    view.clear_screen()

    age = hr.get_average_age()
    view.print_general_results(age, "Average age of employees")


def the_date_difference_is_lesser_than_14(date1, date2):
    YEAR_INDEX = 0
    MONTH_INDEX = 1
    DAY_INDEX = 2
    days_count = 0
    days_in_the_months_normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_in_the_months_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if date1[YEAR_INDEX] == date2[YEAR_INDEX]:
        if hr.is_leap_year(date1[YEAR_INDEX]):
            days_in_the_months = days_in_the_months_leap_year
        else:
            days_in_the_months = days_in_the_months_normal_year
    else:
        return False
    
    if date2[MONTH_INDEX] == date1[MONTH_INDEX] and date2[DAY_INDEX] > date1[DAY_INDEX]:
        days_count += date2[DAY_INDEX] - date1[DAY_INDEX]
    elif date2[MONTH_INDEX] - date1[MONTH_INDEX] == 1 and date2[DAY_INDEX] < date1[DAY_INDEX]:
        days_count += days_in_the_months[date1[MONTH_INDEX] - 1] - date1[DAY_INDEX]
        days_count += date2[DAY_INDEX]
    
    if days_count <= 14:
        return True
    else:
        return False


def next_birthdays():
    birthdays = hr.get_birthday()
    
    input_date = view.get_input("Please, give a date [YYYY-MM-DD]")
    input_date_list = list(map(int, input_date.split("-")))
    
    employees_with_birthdays = []
    
    for name in birthdays.keys():
        if the_date_difference_is_lesser_than_14(birthdays[name], input_date_list):
            employees_with_birthdays.append(name)
    
    if len(employees_with_birthdays) == 0:
        view.print_message("There is no emplyees having birthdays within the two weeks.")
    else:
        view.print_general_results(employees_with_birthdays, "Employees having birthdays within the two weeks")
    
    input("\nPress ENTER to continue ...")
    view.clear_screen()


def count_employees_with_clearance():
    number_of_employees = hr.count_employees_with_clearance()
    view.print_general_results(number_of_employees, "Number of employees with at least given lvl of Clearance")
    
    input("\nPress ENTER to continue ...")
    view.clear_screen()


def count_employees_per_department():
    view.clear_screen()

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
