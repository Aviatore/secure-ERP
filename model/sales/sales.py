""" Sales module

Data table structure:
    - id (string)
    - customer id (string)
    - product (string)
    - price (float)
    - transaction date (string): in ISO 8601 format (like 1989-03-21)
"""

from model import data_manager, util, crud

DATAFILE = "model/sales/sales.csv"
HEADERS = ["Id", "Customer", "Product", "Price", "Date"]


def get_biggest_revenue_transaction():
    data = crud.read(DATAFILE)
    revenue_transaction = []
    revenue_transactions = []
    for transaction in data:
        revenue_transaction.append(list(transaction[3]))
    for i in range(len(revenue_transaction)):
        revenue_transactions.append(converter(revenue_transaction[i], float))
    biggest_revenue_transaction = str(max(revenue_transactions))
    for transaction in data:
        if biggest_revenue_transaction in transaction:
            return transaction


def converter(list, mode):
    list_converter = map(str, list)
    list_converter = ''.join(list_converter)
    list_converter = mode(list_converter)
    return list_converter


def get_biggest_revenue_product():
    data = crud.read(DATAFILE)
    revenue_product = []
    revenue_products = []
    value = values()
    list_of_max_value = []
    biggest_revenue_product = []
    dic_of_products = {}
    for product in data:
        revenue_product.append(list(product[2]))
    for i in revenue_product:
        revenue_products.append("".join(i))
    unique_revenue_products = list(dict.fromkeys(revenue_products))
    for word in set(revenue_products):
        count = revenue_products.count(word)
        index = revenue_products.index(word)
        word_value = value[index]
        word_max_value = word_value * count
        dic_of_products[word] = word_max_value
        list_of_max_value.append(word_max_value)
        if len(list_of_max_value) == len(unique_revenue_products):
            max_value = max(list_of_max_value)
            for x in dic_of_products:
                if dic_of_products[x] == max_value:
                    name_of_product = x
                    biggest_revenue_product.append(name_of_product)
                    biggest_revenue_product.append(max_value)
                    return biggest_revenue_product


def values():
    data = crud.read(DATAFILE)
    product_value = []
    product_values = []
    product_name = []
    product_names = []
    for product in data:
        product_value.append(list(product[3]))
        product_name.append(list(product[2]))
    for i in range(len(product_value)):
        product_values.append(converter(product_value[i], float))
    for i in product_name:
        product_names.append("".join(i))
        return product_values
