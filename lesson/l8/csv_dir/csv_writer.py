import csv

with (
    open('biostats.csv', 'r', newline='') as f_read,
    open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write
):
    csv_read = csv.reader(f_read, quoting=csv.QUOTE_NONNUMERIC)
    csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    all_data = []
    for _ in range(10):
        print(len(next(csv_read)))
    # for i, line in enumerate(csv_read):
    #     if i == 0:
    #         csv_write.writerow(line)
    #     else:
    #         line[2] += 1
    #         for j in range(2, 4 + 1):
    #             line[j] = int(line[j])
    #         all_data.append(line)
    #     csv_write.writerows(all_data)
