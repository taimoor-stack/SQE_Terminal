import unittest

# Sample functions for testing

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def search_student(student_list, roll):
    for student in student_list:
        if student["roll"] == roll:
            return True
    return False


class TestStudentManagementSystem(unittest.TestCase):

    # Test Case 1
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    # Test Case 2
    def test_addition_negative(self):
        self.assertEqual(add(-2, -3), -5)

    # Test Case 3
    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    # Test Case 4
    def test_subtraction_negative(self):
        self.assertEqual(subtract(5, 10), -5)

    # Test Case 5
    def test_search_student_found(self):
        students = [
            {"name": "Ali", "roll": "101"},
            {"name": "Ahmed", "roll": "102"}
        ]

        result = search_student(students, "101")

        self.assertTrue(result)

    # Test Case 6
    def test_search_student_not_found(self):
        students = [
            {"name": "Ali", "roll": "101"},
            {"name": "Ahmed", "roll": "102"}
        ]

        result = search_student(students, "999")

        self.assertFalse(result)

    # Test Case 7
    def test_string_type(self):
        self.assertTrue(isinstance("Ali", str))

    # Test Case 8
    def test_integer_type(self):
        self.assertTrue(isinstance(10, int))

    # Test Case 9
    def test_list_length(self):
        students = ["Ali", "Ahmed"]
        self.assertEqual(len(students), 2)

    # Test Case 10
    def test_uppercase(self):
        self.assertEqual("ali".upper(), "ALI")


if __name__ == '__main__':
    unittest.main()