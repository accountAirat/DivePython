from discriptions import *

class Subject:
    name = Name()
    grades = Range()
    tests = Range()
    def __init__(self, name, grades: [], tests: []):
        self.name = name
        self.grades = grades
        self.tests = tests