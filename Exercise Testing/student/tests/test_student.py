from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("Plamen")
        self.student_with_course = Student("Victoria", {'python': ['note']})

    def test_correct_initialization(self):
        self.assertEqual(self.student.name, 'Plamen')
        self.assertEqual({}, self.student.courses)
        self.assertEqual(self.student_with_course.courses, {'python': ['note']})

    def test_enroll_notes_to_existing_course(self):
        result = self.student_with_course.enroll('python', ['note_one', 'note_two'])
        self.assertEqual(self.student_with_course.courses['python'], ['note', 'note_one', 'note_two'])

        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_add_course_and_course_notes_without_third_parameter(self):
        result = self.student.enroll('java', ['note_java'])

        self.assertEqual(self.student.courses['java'], ['note_java'])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_course_and_course_notes_with_Y_parameter(self):
        result = self.student.enroll('java', ['note_java'], 'Y')

        self.assertEqual(self.student.courses['java'], ['note_java'])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_course_without_notes(self):
        result = self.student.enroll('java', ['note_java'], 'j')

        self.assertEqual(self.student.courses['java'], [])
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.add_notes('python', 'new_note')

        self.assertEqual(['note', 'new_note'], self.student_with_course.courses['python'])

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', 'some_note')

        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course('python')

        self.assertEqual(self.student_with_course.courses, {})
        self.assertEqual(result, "Course has been removed")

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_course.leave_course('c++')

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    main()