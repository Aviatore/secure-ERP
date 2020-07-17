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


def get_year_of_birth():
    data = crud.read(DATAFILE)

    birthday = []
    year_of_birth = []

    for employees in data:
        birthday.append(list(employees[2]))
        year_of_birth.append("0")

    for i in range(len(birthday)):
        for j in range(0, 4):
            year_of_birth[i] += birthday[i][j]

    for i in range(len(year_of_birth)):
        year_of_birth[i] = int(year_of_birth[i])

    return year_of_birth


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

    old_and_young = tuple((oldest_name, youngest_name))

    return old_and_young


def get_average_age():
    years = get_year_of_birth()
    age = []

    for i in range(len(years)):
        age.append(2020 - years[i])

    average_age = sum(age) / len(age)

    return average_age
