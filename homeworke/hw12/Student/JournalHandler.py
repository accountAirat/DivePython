import csv
from getpass import getuser
import Student


class JournalHandler:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = getuser()
        return cls._instance

    def __init__(self, student: Student, group_number: int = 1, len_number: int = 6):
        self.file_name = f'group№{group_number:0>{len_number}}.csv'
        self.student = student

    def subjects_loader(self) -> dict:
        pass

    def __enter__(self):

        with open(self.file_name, 'r', newline='') as f:
            csv_file = csv.reader(f, quoting=csv.QUOTE_MINIMAL)

            self.header = next(csv_file)
            self.subjects = self.header[4::2]
            self.full_name = ['Фамилия', 'Имя', 'Отчество']
            self.model = {'grades': [], 'tests': []}
            self.model_journal_dict: dict = dict.fromkeys(self.subjects, self.model)
            # model_journal_dict.update(dict.fromkeys(full_name, ''))

            self.journal_dict: dict = {}
            for line in csv_file:
                line = iter(line)
                id_student = next(line)
                self.journal_dict[id_student] = self.model_journal_dict.copy()

                for name in self.full_name:
                    self.journal_dict[id_student][name] = next(line)

                for subject in self.subjects:
                    for key in self.model:
                        self.journal_dict[id_student][subject][key] = next(line)

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, 'w', newline='') as f:
            csv_file = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

            csv_file.writerow(self.header)
            line = []
            for id_student in self.journal_dict:
                for i in id_student:
                    if isinstance(i, dict):
                        for j in i:
                            line.append(j)
                    else:
                        line.append(i)

    # id, Фамилия, Имя, Отчество, Математика,, Русский
    # язык,, Литература,, Английский
    # язык,
    # 1, Иванов, Иван, Иванович, 5, 100, 4, 99, 3, 98, 2, 97
    #


if __name__ == '__main__':
