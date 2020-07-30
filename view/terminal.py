from os import system, name, get_terminal_size


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
    print("")
    print(f"{title}:")
    for index, option_name in enumerate(list_options[1:]):
        print(f"({index + 1}) {option_name}")

    print(f"(0) {list_options[0]}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print("")
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    print("")
    
    if isinstance(result, int):
        print(f"{label}: {result}")
        
    elif isinstance(result, float):
        print(f"{label}: {result:.2f}")
        
    elif isinstance(result, list) or isinstance(result, tuple):
        print(f"{label}:")
        print("; ".join(map(str, result)))
        
    elif isinstance(result, dict):
        result_dict_pairs = list(result.items())
        result_dict_pairs_colon_sep = list(map(lambda element : ": ".join(map(str, element)), result_dict_pairs))
        
        print(f"{label}:")
        print("; ".join(result_dict_pairs_colon_sep))


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
    INDEX = 0
    VALUE = 1
    PADDING = 2 # A space between the value and a table cell wall
    print("")
    print(table_line)
    
    for index, line in enumerate(table):
        
        # The first line is treated as a header which is capitalized
        if index == 0:
            line = list(map(lambda element : element.capitalize(), line))
            
        print("|".join(map(lambda element : element[VALUE].center(max_col_len[ element[INDEX] ] + PADDING), enumerate(line))))
        
        if index == 0:
            print(table_line)


def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    print("")
    
    return input(f"{label}: ")


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    print("")
    user_inputs = []
    
    for label in labels:
        user_inputs.append(get_input(label))
    
    return user_inputs


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print("")
    print(f"Error! {message}")


def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def terminal_size():
    size = get_terminal_size()
    
    return (size.lines, size.columns)