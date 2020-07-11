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

def get_customers():
    return data

def add_customer(new_customer):
    data.append(new_customer)
    data_manager.write_table_to_file(DATAFILE, data)