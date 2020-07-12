""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

data = data_manager.read_table_from_file(DATAFILE)


def copy_list(data):
    new_list = []
    for line in data:
        tmp = []
        for element in line:
            tmp.append(element)
        new_list.append(tmp)
    return new_list


def get_customers():
    new_data = copy_list(data)
    return new_data


def add_customer(new_customer):
    data.append(new_customer.insert(0, util.generate_id()))
    data_manager.write_table_to_file(DATAFILE, data)
    
    
def update_customer(customer_to_update):
    data_ids = list(range(len(data)))
    data[data_ids.index(int(customer_to_update[0]) - 1)][1:] = customer_to_update[1:]
    data_manager.write_table_to_file(DATAFILE, data)


def delete_customer(customer_lp):
    data.pop(int(customer_lp) - 1)
    data_manager.write_table_to_file(DATAFILE, data)

def get_subscribed_emails():
    pass