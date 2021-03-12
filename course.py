#class
import csv

class Person:
    def __init__(self,course_number, class_name, overall_grade, credit_hours): # default constructor
        self.next = None  #varables/feilds (no private feilds)
        self.course_number = course_number
        self.class_name = class_name
        self.overall_grade = float(overall_grade)  
        self.credit_hours = float(credit_hours)

    def __str__(self):
        return f"new:{self.course_number} {self.class_name} Grade:{self.overall_grade} Credit Hours:"

def import_file():
    course_info = []
    with open("data.txt", "r") as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                course_info.append(Person(row[0], row[1], row[2], row[3]))
            line_count += 1
    return course_info




    def number(self,course_number):
        self.course_number = course_number       #method (performed by calling def)

    def name(self, class_name):
        self.class_name = class_name

    def credit_hr(self, credit_hours):
        self.credit_hours = credit_hours

    def grade(self, overall_grade):
        self.overall_grade = overall_grade



course_list = import_file()
sorted_list = 

for i in course_list:
    print(i)

"""
    class student(person): #inheritance
        def __init__(self):
            person.__init__(self)
"""