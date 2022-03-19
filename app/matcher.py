import pandas
import math

DATABASE = "database.csv"


def convert_input(data=None):
    data.pop("nome")
    data.pop("comentario")
    for key in data.keys():
        if data[key] == "":
            data[key] = 0.5
        else:
            data[key] = float(data[key])
    return list(data.values())


def open_file(file_name=DATABASE):
    csv_data = pandas.read_csv(file_name)
    return csv_data


def load_database(database=DATABASE):
    database = open_file(database)
    return database


def calculate_distance(user=None, vote_list=None):
    sum = 0
    for i in range(len(user)):
        sum += math.pow((user[i] - vote_list[i]), 2)
    distance = math.pow(sum, 1 / 2)
    return distance


def sort_compare_dict(compare_dict=None):
    sorted_dict = dict(sorted(compare_dict.items(), key=lambda item: item[1]))
    return sorted_dict


def compare_user(user=None, data=None):
    distance_dict = dict()
    for i in range(len(data)):
        vote_list = data.loc[i].tail(12)
        distance_dict[
            f'{data.loc[i, "nome"]} {data.loc[i, "siglaPartido"]}'
        ] = calculate_distance(user, vote_list)
    distance_dict = sort_compare_dict(distance_dict)
    return distance_dict


def do_match(user=None, database=None):
    compare = compare_user(user, database)
    items = compare.keys()
    closest = list(items)[:5]
    distant = list(items)[-5:]
    return closest, distant


if __name__ == "__main__":
    database = load_database()
    user_data = {
        "nome": "Arthur",
        "pergunta-1": "1.0",
        "pergunta-2": "1.0",
        "pergunta-3": "",
        "pergunta-4": "",
        "pergunta-5": "",
        "pergunta-6": "",
        "pergunta-7": "",
        "pergunta-8": "",
        "pergunta-9": "",
        "pergunta-10": "0.5",
        "pergunta-11": "0.0",
        "pergunta-12": "0.5",
        "comentario": "",
    }
    # user_list = [1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0]
    # print(do_match(user_list, database))

    converted_data = convert_input(user_data)
    print(converted_data)
    # print(do_match(converted_data, database))
