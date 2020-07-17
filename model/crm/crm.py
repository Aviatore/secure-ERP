""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util, crud


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]

def get_subscribed_emails():
    data = crud.read(DATAFILE)
    emails = []
    
    for customer in data:
        if customer[3] == "1":
            emails.append(customer[2])
    
    return emails