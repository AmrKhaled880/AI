import unittest

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student('Amr')

    def test_creation(self):
        self.assertEqual(self.student.name, 'Amr')

    def test_add_grade(self):
        self.student.add_grade(1, 90)
        self.assertEqual(self.student.grades[1], 90)

    def test_enrolle_in_course(self) :
        course = Course('Math')
        self.student.enrolle_in_course(course)
        self.assertIn(course, self.student.enrolled_courses)

unittest.main(argv=['first-arg-is-ignored'], exit=False)


