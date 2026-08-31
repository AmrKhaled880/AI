class Student :
    _id_counter = 1 # class attribute

    def __init__(self, name) :
        self.student_id = Student._id_counter
        Student._id_counter += 1
        self.name = name 
        self.grades = {}
        self.enrolled_courses = []
    
    def __str__(self) :
        return f'Studnet id {self.student_id} name : {self.name}, grades : {self.grades}, courses : {self.enrolled_courses}'

    def __repr__(self) -> str :
        return f'Studnet id {self.student_id} name : {self.name}, grades : {self.grades}, courses : {self.enrolled_courses}'

    def add_grade(self, course_id, grade) :
        if not  0 <= grade <= 100 :
            raise ValueError("Grades must be between 0 and 100")
        self.grades[course_id] = grade

    def enrolle_in_course(self, course):
        if course in self.enrolled_courses:
            raise f'This Course already in enrolled courses'
        else :
            self.enrolled_courses.append(course)
