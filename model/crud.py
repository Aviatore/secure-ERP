from model import data_manager, util


def read(data_file):
    data = data_manager.read_table_from_file(data_file)

    return data


def create(data_file, new_data):
    data = read(data_file)

    new_id = util.generate_id()

    data_new_customer = [new_id]
    data_new_customer.extend(new_data)
    
    data.append(data_new_customer)

    data_manager.write_table_to_file(data_file, data)


def update(data_file, update_data):
    data = read(data_file)

    data_ids = list(range(len(data)))

    data[data_ids.index(int(update_data[0]) - 1)][1:] = update_data[1:]

    data_manager.write_table_to_file(data_file, data)


def delete(data_file, data_lp):
    data = read(data_file)

    data.pop(int(data_lp) - 1)

    data_manager.write_table_to_file(data_file, data)