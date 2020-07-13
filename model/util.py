import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    
    small_letters_list = list(string.ascii_lowercase)
    capital_letters_list = list(string.ascii_uppercase)
    digits_list = list(string.digits)
    special_chars_list = list(allowed_special_chars)
    
    id_list = []
    id_list.extend(random.sample(small_letters_list, number_of_small_letters))
    id_list.extend(random.sample(capital_letters_list, number_of_capital_letters))
    id_list.extend(random.sample(digits_list, number_of_digits))
    id_list.extend(random.sample(special_chars_list, number_of_special_chars))
    
    random.shuffle(id_list)
    id = "".join(id_list)
              
    return id
