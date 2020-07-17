""" Human resources (HR) module

Data table structure:
    - id (string)
    - name (string)
    - birth date (string): in ISO 8601 format (like 1989-03-21)
    - department (string)
    - clearance level (int): from 0 (lowest) to 7 (highest)
"""

from model import data_manager, util, crud

DATAFILE = "model/hr/hr.csv"
HEADERS = ["Id", "Name", "Date of birth", "Department", "Clearance"]


def get_age():
    data = crud.read(DATAFILE)

    birthday = []

    for employees in data:
        birthday.append(employees[2])

    age = []

    return birthday


def get_oldest_and_youngest():
    data = crud.read(DATAFILE)
    birthday = []
    names = []

    for employees in data:
        birthday.append(employees[2])
        names.append(employees[1])

    oldest = "2020-01-01"
    youngest = "1900-01-01"
    oldest_name = ""
    youngest_name = ""

    for i in range(len(birthday)):
        if birthday[i] < oldest:
            oldest = birthday[i]
            oldest_name = names[i]

        if birthday[i] > youngest:
            youngest = birthday[i]
            youngest_name = names[i]

    return oldest_name, youngest_name


