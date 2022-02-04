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

def calculate_distance(user=None, deputy=None):
    sum = 0
    for i in range(len(user)):
        sum += math.pow((user[i] - deputy[i]), 2)
    distance = math.pow(sum, 1/2)
    return distance

def compare_user(user=None, database=None):
    distance_dict = dict()
    data = database
    for deputy in data:
        print(deputy)
        #data = deputy.tail(12)
        #distance_dict[deputy.tail(-1)] = calculate_distance(y,data)
    return distance_dict




if __name__ == "__main__":
    y = [1.0,1.0,1.0,0.5,0.5,1.0,0.0,1.0,1.0,1.0,0.0,1.0]
    database = load_database()
    compare = compare_user(y, database)
    #print(compare)
    #print(distance)
