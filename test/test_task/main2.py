import csv


def add_percent(my_dict: dict) -> None:
    for cur_date in my_dict:
        cur_sum = sum(my_dict[cur_date].values())
        for i in my_dict[cur_date]:
            my_dict[cur_date][i] = (my_dict[cur_date][i], round(my_dict[cur_date][i] / (cur_sum / float(100))))


def add_date(my_dict: dict) -> None:
    for cur_date in my_dict:
        my_dict[cur_date]["date"] = cur_date


with(
    open('data.csv', mode='r', newline='') as db_file,
    open('result.csv', mode='w', newline='') as res
):
    csv_read = csv.DictReader(db_file, delimiter=';',
                              fieldnames=["contract", "office", "cash", "date"],
                              quoting=csv.QUOTE_ALL)

    contract_set = set()
    next(csv_read)
    result = {}

    for dict_row in csv_read:
        current_date = dict_row["date"][:-9]
        current_office = dict_row["office"]

        contract_set.add(current_office)
        sum_cash = result.setdefault(current_date, {}).setdefault(current_office, 0)
        result[current_date][current_office] = sum_cash + round(float(dict_row["cash"]), 2)

    add_percent(result)
    add_date(result)

    csv_write = csv.DictWriter(res, fieldnames=["date"] + sorted(contract_set), quoting=csv.QUOTE_NONNUMERIC)

    csv_write.writeheader()
    for row in sorted(result):
        csv_write.writerow(result[row])
