"IDZ6 Беспалов С.И. 2586"


class Student:
    """
    representing student in list 
    """

    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.width_name = len(name)
        self.width_surname = len(surname)

    def __str__(self) -> str:
        return f'| {self.name: <{self.width_name}} | {self.surname: <{self.width_surname}} |'



class Group:
    """
    group class
    """
    col_width_name = 0
    col_width_surname = 0
    student_list = []
    def __init__(self, num) -> None:
        self.group_num = num

    def add_student(self, name, surname) -> None:
        """ add student to list """
        self.student_list.append(Student(name,surname))

    def delete_student(self, n, s) -> None:
        """ remove student from list """
        for student in self.student_list:
            if (student.name == n and student.surname == s):
                self.student_list.remove(student)
                break

    def __str__(self) -> str:
        """ representation overload """
        for stud in self.student_list:
            if stud.width_name > self.col_width_name :
                self.col_width_name = stud.width_name
            if stud.width_surname > self.col_width_surname :
                self.col_width_surname = stud.width_surname
        str_repr = "-"*(self.col_width_name + self.col_width_surname+7)+'\n'
        for  student in self.student_list:
            str_repr += f'| {student.name: <{self.col_width_name}} | {student.surname: <{self.col_width_surname}} |\n'
        str_repr += "-"*(self.col_width_name + self.col_width_surname+7)+'\n'
        return str_repr


group1 = Group(input("Введите номер группы: "))

for i in range (int(input("Введите количество студентов в группе: "))):
    group1.add_student(input(f"Введите имя студента {i+1}: "),
                        input(f"Введите фамилию студента {i+1}: "))

print(f"\nСписок студентов группы {group1.group_num}:\n", group1)

group2 = group1

print("Введите количество исключающихся студентов: ")

for i in range(int(input())):
    group2.delete_student(input(f"Введите имя студента {i+1}: "),
                          input(f"Введите фамилию студента {i+1}: "))

print(f"Скоректированный список группы {group2.group_num}\n", group2)
