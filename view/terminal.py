def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f"{title}:")
    for index, option_name in enumerate(list_options):
        print(f"({index + 1}) {option_name}")

    print("(0) Exit program")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    
    if isinstance(result, int):
        print(f"{label}: {result}")
    elif isinstance(result, float):
        print(f"{label}: {result:.2f}")
    elif isinstance(result, list) or isinstance(result, tuple):
        print(f"{label}:")
        print("; ".join(map(str, result)))
    elif isinstance(result, dict):
        print(f"{label}:")
        print("; ".join(list(map(lambda element : ": ".join(map(str, element)), list(result.items())))))


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    # Create a list with max lengths of column elements
    max_col_len = list(map(len, table[0]))
    for line_index, line in enumerate(table):
        for element_index, element in enumerate(line):
            if max_col_len[element_index] < len(element):
                max_col_len[element_index] = len(element)
    
    # Create a table line that matches the lengths of column elements
    table_line = ""
    for index, col_len in enumerate(max_col_len):
        table_line += "-" * (col_len + 2)
        if index < len(table[0]) - 1:
            table_line += "+"
    
    # Print the table
    print(table_line)
    for index, line in enumerate(table):
        print("|".join(map(lambda element : element[1].center(max_col_len[element[0]] + 2), enumerate(line))))
        if index == 0:
            print(table_line)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    pass


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    pass
