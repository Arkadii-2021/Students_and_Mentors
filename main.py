class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grades_avg(self):
        list_grades = []
        for grades_list in self.grades.values():
            for grades_in_course in grades_list:
                list_grades.append(grades_in_course)
        avg_student = round(sum(list_grades) / len(list_grades), 1)
        return avg_student

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Студент не идентифицирован'
        else:
            if self.grades_avg() > other.grades_avg():
                return f'Средний бал студента {self.name} {self.surname} лучше чем у студента {other.name} {other.surname}'
            elif other.grades_avg() > self.grades_avg():
                return f'Средний бал студента {other.name} {other.surname} лучше чем у студента {self.name} {self.surname}'
            else:
                return f'Студенты: {other.name} {other.surname} и {self.name} {self.surname} равнозначны по успеваемости'

    def __str__(self):
        student_present = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.grades_avg()} \nКурсы в процессе изучения: {" | ".join(self.courses_in_progress)} \nЗавершенные курсы: {" | ".join(self.finished_courses)}'
        return student_present

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

    def grades_lector_avg(self):
        list_grades = []
        for grades_list in self.grades.values():
            for grades_in_course in grades_list:
                list_grades.append(grades_in_course)
        avg_lector = round(sum(list_grades) / len(list_grades), 1)
        return avg_lector

    def __lt__(self, other):
        if not isinstance(other, Lector):
            return 'Студент не идентифицирован'
        else:
            if self.grades_lector_avg() > other.grades_lector_avg():
                return f'Средний бал лектора {self.name} {self.surname} лучше чем у лектора {other.name} {other.surname}'
            elif other.grades_lector_avg() > self.grades_lector_avg():
                return f'Средний бал лектора {other.name} {other.surname} лучше чем у лектора {self.name} {self.surname}'
            else:
                return f'Лекторы: {other.name} {other.surname} и {self.name} {self.surname} равнозначны'

    def __str__(self):
        lector_present = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.grades_lector_avg()}'
        return lector_present

class Reviewer (Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_present = f'Имя: {self.name} \nФамилия: {self.surname}'
        return reviewer_present

best_student = Student('Kristina', 'Makarovna', 'female')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student_2 = Student('Nikolay', 'Artemovich', 'male')
best_student_2.courses_in_progress += ['Git']
best_student_2.courses_in_progress += ['Java']
best_student_2.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Timur', 'Antonovich')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer_2 = Reviewer('Maksim', 'Daniilovich')
cool_reviewer_2.courses_attached += ['Java']

cool_lector = Lector('Nikita', 'Romanovich')
cool_lector.courses_attached += ['Git']
cool_lector.courses_attached += ['Python']

cool_lector_2 = Lector('Mariya', 'Michailovna')
cool_lector_2.courses_attached += ['Git']
cool_lector_2.courses_attached += ['Java']

best_student.rate_lector(cool_lector, 'Python', 10)
best_student.rate_lector(cool_lector, 'Python', 9)
best_student.rate_lector(cool_lector, 'Git', 9)
best_student.rate_lector(cool_lector, 'Git', 10)
best_student_2.rate_lector(cool_lector_2, 'Git', 10)
best_student_2.rate_lector(cool_lector_2, 'Git', 9)
best_student_2.rate_lector(cool_lector_2, 'Java', 10)

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 10)

cool_reviewer.rate_hw(best_student_2, 'Git', 10)
cool_reviewer.rate_hw(best_student_2, 'Git', 8)
cool_reviewer.rate_hw(best_student_2, 'Git', 9)

cool_reviewer_2.rate_hw(best_student_2, 'Java', 9)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 10)
cool_reviewer_2.rate_hw(best_student_2, 'Java', 10)

print('\nСтуденты:')
print(best_student, '\n')
print(best_student_2, '\n')

print('Лекторы:')
print(cool_lector, '\n')
print(cool_lector_2, '\n')

print('Reviewers:')
print(cool_reviewer, '\n')
print(cool_reviewer_2, '\n')

print('*** Некоторые сравнения по успеваемости студентов и баллы, полученным за лекции лекторам ***')
print(best_student_2.__lt__(best_student))
print(cool_lector.__lt__(cool_lector_2), '\n')

students = [best_student, best_student_2]
lectors = [cool_lector, cool_lector_2]

def avg_grade_in_course(students, course):
    all_grades_in_course = []
    for student in students:
        if student.grades.get(course) != None:
            for student_course in student.grades.get(course):
                all_grades_in_course.append(student_course)
    avg_grade_in_course = round(sum(all_grades_in_course) / len(all_grades_in_course), 1)
    return avg_grade_in_course

def lector_avg_grade_course(lectors, course):
    all_grades_course = []
    for lector in lectors:
        if lector.grades.get(course) != None:
            for lector_course in lector.grades.get(course):
                all_grades_course.append(lector_course)
    avg_grade_course = round(sum(all_grades_course) / len(all_grades_course), 1)
    return avg_grade_course

print(f'Средняя оценка за домашние задания всех студентов в рамках курса "Python": {avg_grade_in_course(students, "Python")}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса "Python": {avg_grade_in_course(lectors, "Python")}')
print(f'Средняя оценка за домашние задания всех студентов в рамках курса "Java": {avg_grade_in_course(students, "Java")}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса "Java": {avg_grade_in_course(lectors, "Java")}')
print(f'Средняя оценка за домашние задания всех студентов в рамках курса "Git": {avg_grade_in_course(students, "Git")}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса "Git": {avg_grade_in_course(lectors, "Git")}')

