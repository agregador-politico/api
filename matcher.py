import pandas
import math

DATABASE = "database.csv"


def convert_input(data=None):
    data.pop("nome")
    data.pop("comentario")
    return data


def open_file(database=DATABASE):
    csv_data = pandas.read_csv(database)
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
        ] = calculate_distance(y, vote_list)
    distance_dict = sort_compare_dict(distance_dict)
    return distance_dict


def do_match(user=None, database=None):
    compare = compare_user(user, database)
    items = compare.keys()
    closest = list(items)[:5]
    distant = list(items)[-5:]
    return closest, distant


if __name__ == "__main__":
    y = [1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0]
    database = load_database()
    print(do_match(y, database))
