import pickle

#  1
my_dict = {
    "first_name": "Джон",
    "last_name": "Смит",
    "hobbies": ["кузнечное дело", "программирование",
                "путешествия"],
    "age": 35,
    "children": [
        {
            "first_name": "Алиса",
            "age": 5
        },
        {
            "first_name": "Маруся",
            "age": 3
        }
    ]
}
print(my_dict)
res = pickle.dumps(my_dict, protocol=pickle.DEFAULT_PROTOCOL)
print(f'{res = }')


#  2
def func(a, b, c):
    return a + b + c


my_dict = {
    "numbers": [42, 4.1415, 7 + 3j],
    "functions": (func, sum, max),
    "others": {True, False, 'Hello world!'},
}
with open('my_dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)
