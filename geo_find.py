import json

from geopy.distance import geodesic


def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data


def find_distance(top, point, data):
    list1 = []
    for i in data:
        kms = geodesic((i[1], i[2]), point).km
        i.append(kms)
        list1.append(i)
    list1.sort(key=lambda x: x[3])
    return list1[:top]


data = load_data()
point = (43.256274, 76.789275)
top = 10
print(find_distance(top, point, data))
