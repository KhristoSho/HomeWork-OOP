class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.__average_grade()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __average_grade(self):
        sum_ = 0
        cnt = 0
        if self.grades.values():
            for grade in self.grades.values():
                    sum_ += sum(grade)
                    cnt += len(grade)
            return round(sum_/cnt, 2)
        else:
            return 'оценок нет'
 
    def add_courses(self, *course_name):
        if course_name not in self.courses_in_progress:
            self.courses_in_progress.extend(course_name)

    def fin_courses(self, course_name):
        if course_name in self.courses_in_progress:
            self.finished_courses.append(course_name)
            self.courses_in_progress.remove(course_name)
        else:
            return "ошибка"
    
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
            and grade in range(1, 11)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __lt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.__average_grade < other.__average_grade
        else:
            return "Ошибка"

    def __le__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.__average_grade <= other.__average_grade
        else:
            return "Ошибка"

    def __eq__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.__average_grade == other.__average_grade
        else:
            return "Ошибка"

    def __ne__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.__average_grade != other.__average_grade
        else:
            return "Ошибка"

    def __gt__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.__average_grade > other.__average_grade
        else:
            return "Ошибка"

    def __ge__(self, other):
        if isinstance(self, Student) and isinstance(other, Student):
            return self.__average_grade >= other.__average_grade
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses(self, *course_name):
        if course_name not in self.courses_attached:
            self.courses_attached.extend(course_name)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.grades = {}
    
    def __average_grade(self):
        sum_ = 0
        cnt = 0
        if self.grades.values():
            for grade in self.grades.values():
                    sum_ += sum(grade)
                    cnt += len(grade)
            return round(sum_/cnt, 2)
        else:
            return 'оценок нет'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.__average_grade()}')

    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.__average_grade < other.__average_grade
        else:
            return "Ошибка"

    def __le__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.__average_grade <= other.__average_grade
        else:
            return "Ошибка"

    def __eq__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.__average_grade == other.__average_grade
        else:
            return "Ошибка"

    def __ne__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.__average_grade != other.__average_grade
        else:
            return "Ошибка"

    def __gt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.__average_grade > other.__average_grade
        else:
            return "Ошибка"

    def __ge__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            return self.__average_grade >= other.__average_grade
        else:
            return "Ошибка"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_grade(course_name, *members):
    all_grades = []
    if all(list(map(lambda x: type(x) is type(members[0]), members))):
        for member in members:
            try:
                all_grades.extend(member.grades.get(course_name))
            except TypeError:
                continue
        return round(sum(all_grades)/len(all_grades), 2)
    else:
        return "Ошибка! Сравниваются студенты и лекторы."

# Создаем экземпляры классов
student1 = Student("Никита", "Леонов")
student2 = Student("Игорь", "Некифоров")
lecturer1 = Lecturer("Иван", "Кузнецов")
lecturer2 = Lecturer("Руслан", "Семенов")
reviewer1 = Reviewer("Алла", "Борисова")
reviewer2 = Reviewer("Денис", "Силков")

# Добавляем дисциплины
student1.add_courses("Основы программирования Python", "Основы SQL", "Программирование с нуля")
student1.fin_courses("Программирование с нуля")
student2.add_courses("Основы SQL")

lecturer1.add_courses("Основы программирования Python")
lecturer2.add_courses("Основы SQL")

reviewer1.add_courses("Основы программирования Python", "Основы SQL")
reviewer2.add_courses("Основы программирования Python", "Основы SQL")

# Расставляем оценки:
student1.rate_lecturer(lecturer1, "Основы программирования Python", 8)
student1.rate_lecturer(lecturer1, "Основы программирования Python", 20)
student1.rate_lecturer(lecturer1, "Основы программирования Python", 7)
student1.rate_lecturer(lecturer2, "Основы SQL", 10)
student1.rate_lecturer(lecturer2, "Основы SQL", 9)

student2.rate_lecturer(lecturer2, "Основы SQL", 9)
student2.rate_lecturer(lecturer2, "Основы SQL", 9)

reviewer1.rate_hw(student1,"Основы программирования Python", 3 )
reviewer1.rate_hw(student1,"Основы программирования Python", 4 )
reviewer1.rate_hw(student1,"Основы SQL", 5 )
reviewer1.rate_hw(student1,"Основы SQL", 5 )
reviewer1.rate_hw(student2,"Основы SQL", 4 )
reviewer1.rate_hw(student2,"Основы SQL", 4 )

reviewer2.rate_hw(student1,"Основы программирования Python", 5 )
reviewer2.rate_hw(student2,"Основы SQL", 5 )


print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)
print()
print(average_grade("Основы программирования Python", student1, student2))
print(average_grade("Основы SQL", student1, student2))
print()
print(average_grade("Основы программирования Python", lecturer1, lecturer2))
print(average_grade("Основы SQL", lecturer1, lecturer2))
print()
print(average_grade("Основы программирования Python", lecturer1, student1))