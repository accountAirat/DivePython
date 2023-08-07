import csv

# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", "height", "weight", "office"],
#                               restkey="new", restval="Main Office", quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(f'{line = }')
#     print(f'{line["name"] = }\t{line["age"] = }')


with open('biostats.csv', 'r', newline='') as f:
    csv_file = csv.DictReader(f, fieldnames=["name", "sex", "age", ], restkey="new", restval="Main Office", quoting=csv.QUOTE_NONNUMERIC)
    for line in csv_file:
        print(f'{line = }')
    print(f'{line["name"] = }\t{line["age"] = }')