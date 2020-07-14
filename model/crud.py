from model import data_manager, util


def copy_nested_list(data):
    new_list = []
    for line in data:
        tmp = []
        for element in line:
            tmp.append(element)
        new_list.append(tmp)
    return new_list


def function_get(data):
    new_data = copy_nested_list(data)
    return new_data


def function_add(data, data_file, new_data):
    new_id = util.generate_id()
    data_new_customer = [new_id]
    data_new_customer.extend(new_data)
    data.append(data_new_customer)

    data_manager.write_table_to_file(data_file, data)


def function_update(data, data_file, update_data):
    data_ids = list(range(len(data)))

    data[data_ids.index(int(update_data[0]) - 1)][1:] = update_data[1:]

    data_manager.write_table_to_file(data_file, data)


def function_delete(data, data_file, data_lp):
    data.pop(int(data_lp) - 1)

    data_manager.write_table_to_file(data_file, data)