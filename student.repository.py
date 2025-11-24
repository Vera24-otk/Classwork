import csv


class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

      return f"{seif.name}-{self.age}"

class Student_repository:
    def __init__(self, path):
        self.__path = path

def get_all(self):
    students=list()
    with open(self.__path, 'r', encoding="UTF-8") as file:
        reader=csv.reader(file)
        for row in reader:
            student = Student(row[0],row[1],int(row[2]))
            students.append(student)
            return student
def get_by_id(self,id)
    with open(self.__path, 'r', encoding="UTF-8") as file:
        reader = csv.reader(file)
        for row in reader:
            student = Student(row[0], row[1], int(row[2]))
            if student.id == id:
            return student
    return None

def add(self, student,):
    with open(self.path, "a", encoding="UTF-8") as file:
        writer = csv.DictWriter(file, fieldnames:["id","name","age"])
        writer.writerow(student.__dict__())

def update(self,student):
    students =self.get_all()
    for i in students:
        if int(i.id) == int(student.id):
           i = student
    self.write_all(students)

def del_by_
    with open('users.csv', 'r+') as file:
        file.truncate(0)