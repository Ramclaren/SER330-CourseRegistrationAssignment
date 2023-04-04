
import unittest

from person_def import Person
from course_def import Course

class Test_Person(unittest.TestCase):
    def test_PersonInit_WhenAllConditionsAreMet_CreatesObject(self):
        # Arrange
        person = Person('LastName', 'FirstName', 'School', 'none', 'none', 'none')

        # Act
        person.last_name = 'Test'

        # Assert
        assert person.last_name == 'Test'

if __name__ == '__main__':
    unittest.main() 

class Test_Course(unittest.TestCase):
    def test_CourseInit_WhenAllCondtionsAreMet_CreatesObject(self):
        course = Course('Math','300','Calculus','none')   
        
        course.name = 'Algebra'
        
        assert course.name == 'Algebra'