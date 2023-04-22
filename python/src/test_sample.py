
import unittest

from person_def import Person
from course_def import Course
from student_def import Student
from instructor_def import Instructor
from institution_def import Institution
from course_offering_def import CourseOffering

class Test_Person(unittest.TestCase):
    def test_PersonInit_WhenAllConditionsAreMet_CreatesObject(self):
        # Arrange
        person = Person('LastName', 'FirstName', 'School', 'none', 'none', 'none')

        # Act
        person.last_name = 'Test'

        # Assert
        assert person.last_name == 'Test'

class Test_Course(unittest.TestCase):
    def test_CourseInit_WhenAllCondtionsAreMet_CreatesObject(self):
        # Arrange
        course = Course('Math','300','Calculus','none')   
        
        # Act
        course.name = 'Algebra'
        
        # Assert
        assert course.name == 'Algebra'
        
class Test_Student(unittest.TestCase):
     def test_StudentInit_WhenAllCondtionsAreMet_CreatesObject(self):
         #Arrange
         student = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')
         
         #Act 
         student.username = 'Rion.Mclaren'
         
         #Assert
         assert student.username == 'Rion.Mclaren'

class Test_Student_List_Courses(unittest.TestCase):    
    def test_StudentListCourses_WhenAllCondtionsAreMet_CreatesObject(self):
        #Arrange
        student = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')
        course1 = Course('Math','300','Calculus',3) 
        course2 = Course('Bio','101','Plant Life',3) 
        course3 = Course('English','210','Poetry',3)
        courseOffering1 = CourseOffering(course1, "15","2023","2")
        courseOffering2 = CourseOffering(course2, "15","2023","1")
        courseOffering3 = CourseOffering(course3, "15","2023","3")
        student.transcript = {courseOffering1:"A", courseOffering2:"B", courseOffering3:"A"}
        #Act
        coursesList = Student.list_courses(student)
        #Output contains english,math,bio
        
        #Assert
        assert coursesList == [courseOffering3,courseOffering1,courseOffering2]

class Test_Student_Credits(unittest.TestCase):
    def test_StudentCredits_WhenAllCondtionsAreMet_CreatesObject(self):
        #Arrange
        student = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')
        course1 = Course('Math','300','Calculus',3) 
        course2 = Course('Bio','101','Plant Life',3) 
        
        #Act
        student.course_list =[course1,course2]
        
        #Assert
        assert student.credits == 6
        
class Test_Student_String(unittest.TestCase):
    def test_StudentString_WhenAllConditionsAreMet_CreatesObject(self):
        #Arrange
        student = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')

        #Act
        string = Student.__str__(student)
        
        #Assert
        assert string == ('\n' + 'Student Name: ' + student.first_name + ' ' + student.last_name + '\n' +
            'School: ' + student.school + '\n' +
            'DOB: ' + student.date_of_birth + '\n' +
            'Username: ' + student.username + '\n' +
            'GPA: ' + str(student.gpa) + '\n' +
            'Credits: ' + str(student.credits) + '\n')
        
class Test_Instructor(unittest.TestCase):
    def test_InstructorInit_WhenAllCondtionsAreMet_CreatesObject(self):
        #Arrange
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','none','DNicolini')   
        
        # Act
        instructor.last_name = 'Smith'
        
        # Assert
        assert instructor.last_name  == 'Smith'
        
class Test_Instructor_List_Courses_Unfiltered(unittest.TestCase):
    def test_InstructorListCourses_WhenAllCondtionsAreMet_CreatesObject(self):
        #Arrange
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','none','DNicolini')   
        course1 = Course('Math','300','Calculus',3) 
        course2 = Course('Bio','101','Plant Life',3) 
        course3 = Course('English','210','Poetry',3)
        courseOffering1 = CourseOffering(course1, "15","2023","2")
        courseOffering2 = CourseOffering(course1, "15","2023","1")
        courseOffering3 = CourseOffering(course1, "15","2023","3")
        courseOfferingList = [courseOffering1,courseOffering2,courseOffering3]
        instructor.course_list = courseOfferingList
        
        # Act
        testOfferingList = Instructor.list_courses(instructor)
        
        # Assert
        assert len(courseOfferingList) ==len(testOfferingList)

class Test_Instructor_List_Courses_FilteredByYear(unittest.TestCase):
    def test_InstructorListCoursesByYear_WhenAllCondtionsAreMet_CreatesObject(self):
        #Arrange
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','none','DNicolini')   
        course1 = Course('Math','300','Calculus',3) 
        course2 = Course('Bio','101','Plant Life',3) 
        course3 = Course('English','210','Poetry',3)
        courseOffering1 = CourseOffering(course1, "15","2023","2")
        courseOffering2 = CourseOffering(course1, "15","2022","1")
        courseOffering3 = CourseOffering(course1, "15","2023","3")
        courseOfferingList = [courseOffering1,courseOffering2,courseOffering3]
        instructor.course_list = courseOfferingList
        
        # Act
        testOfferingList = Instructor.list_courses(instructor,"2023")
        
        # Assert
        assert len(testOfferingList) == 2
        
class Test_Instructor_List_Courses_FilteredByQuarter(unittest.TestCase):
    def test_InstructorListCoursesByQuarter_WhenAllCondtionsAreMet_CreatesObject(self):
        #Arrange
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','none','DNicolini')   
        course1 = Course('Math','300','Calculus',3) 
        course2 = Course('Bio','101','Plant Life',3) 
        course3 = Course('English','210','Poetry',3)
        courseOffering1 = CourseOffering(course1, "15","2023","2")
        courseOffering2 = CourseOffering(course2, "15","2022","1")
        courseOffering3 = CourseOffering(course3, "15","2023","3")
        courseOfferingList = [courseOffering1,courseOffering2,courseOffering3]
        instructor.course_list = courseOfferingList
        
        # Act
        testOfferingList = Instructor.list_courses(instructor,None,"3")
        
        # Assert
        assert len(testOfferingList) == 1
        
class Test_Instructor_String(unittest.TestCase):
    def test_InstructorString_WhenAllConditionsAreMet_CreatesObject(self):
        #Arrange
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','1/1/2000','DNicolini')   

        #Act
        str = Instructor.__str__(instructor)
        
        #Assert
        assert str == ('\n' + 'Instructor Name: Dylan Nicolini' + '\n' +
            'School: Quinnipiac'  + '\n' +
            'DOB: 1/1/2000' +  '\n' +
            'Username: DNicolini' +  '\n')

class Test_Institution(unittest.TestCase):
    def test_InstitutionInit_WhenAllCondtionsAreMet_CreatesObject(self):
        #Arrange
        institution = Institution('Quinnipiac University', "qu.edu")   
        
        # Act
        institution.name = ('Fordham University')
        
        # Assert
        assert institution.name  == 'Fordham University'
        
class Test_Institution_Enrolling_Students(unittest.TestCase):
    def test_EnrollStudent_WhenAllCondtionsAreMet_AddsStudentToList(self):
        #Arrange
        institution = Institution('Quinnipiac University', "qu.edu")   
        student = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')
        
        # Act
        Institution.enroll_student(institution,student)
        Institution.list_students(institution)
        
        # Assert
        assert institution.student_list.get("Ramclaren") == student

class Test_Institution_Hire_Instructor(unittest.TestCase):
    def test_HireInstructor_WhenAllCondtionsAreMet_AddsInstructorToList(self):
        #Arrange
        institution = Institution('Quinnipiac University', "qu.edu")   
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','none','DNicolini')   
        
        # Act
        Institution.hire_instructor(institution,instructor)
        Institution.list_instructors(institution)
        
        # Assert
        assert institution.faculty_list.get(instructor.username) == instructor

class Test_Institution_Add_Course(unittest.TestCase):
    def test_AddCourse_WhenAllCondtionsAreMet_AddsCourseToList(self):
        #Arrange
        institution = Institution('Quinnipiac University', "qu.edu")   
        course = Course('Math','300','Calculus',3) 
        courseOffering = CourseOffering(course, "15","2023","2")
        
        # Act
        Institution.add_course(institution,course)
        Institution.list_course_catalog(institution)
        
        # Assert
        assert institution.course_catalog.get(course.name) == course

class Test_Institution_Add_Course_Offering(unittest.TestCase):
    def test_AddCourseOffering_WhenAllCondtionsAreMet_AddsCourseOfferingToList(self):
        #Arrange
        institution = Institution('Quinnipiac University', "qu.edu")   
        course = Course('Math','300','Calculus',3) 
        courseOffering = CourseOffering(course, "15","2023","2")
        
        # Act
        Institution.add_course(institution,course)
        Institution.add_course_offering(institution,courseOffering)
        Institution.list_course_schedule(institution,'2023','2')
        
        # Assert
        assert len(institution.course_schedule) == 1


class Test_Institution_RegisterStudentforCourse(unittest.TestCase):
    def test_RegisterStudentforCourse_WhenAllCondtionsAreMet_AddsStudentToCourseOffering(self):
        #Arrange        
        institution = Institution('Quinnipiac University', "qu.edu")   
        student = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')
        course = Course('Math','300','Calculus',3) 
        courseOffering = CourseOffering(course, "15","2023","2")
        
        #Act
        Institution.add_course_offering(institution,courseOffering)
        Institution.register_student_for_course(institution,student,course.name,course.department,course.number,course.number,courseOffering.year,courseOffering.quarter)
        
        #Assert
        assert courseOffering.registered_students == [student]
        
class Test_CourseOffering(unittest.TestCase):
    def test_TestCourseInit_WhenAllCondtionsAreMet_CreatesObject(self):    
        #Arrange
        course = Course('Math','300','Calculus',3) 
        course2 = Course('English','210','Poetry',3)
        courseOffering = CourseOffering(course, "15","2023","2")
        
        #Act
        courseOffering.year = "2024"
            
        #Assert
        assert courseOffering.year == "2024"
        
class Test_CourseOffering_RegisterStudents(unittest.TestCase):      
    def test_RegisterStudents_WhenAllCondtionsAreMet_AddsStudentToList(self):
        #Arrange
        student1 = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')
        student2 = Student("last name", 'first name','school', 'date', 'username')
        course = Course('Math','300','Calculus',3) 
        #instructor = Instructor('Nicolini','Dylan','Quinnipiac','1/1/2000','DNicolini')   
        courseOffering = CourseOffering(course, "15","2023","2")
        students = [student1,student2]
        
        #Act
        CourseOffering.register_students(courseOffering,students)
        
        #Assert
        assert len(CourseOffering.get_students(courseOffering)) == len(students)
        assert len(student1.course_list) != 0
                   
class Test_CourseOffering_String_NoInstructor(unittest.TestCase):      
    def test_CourseOfferingString_WhenAllCondtionsAreMet_CreatesString(self):
        #Arrange
        course = Course('Math','300','Calculus',3) 
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','1/1/2000','DNicolini')   
        courseOffering = CourseOffering(course, "15","2023","2")
        
        #Act
        courseOfferingString = CourseOffering.__str__(courseOffering)
        
        #Assert
        assert courseOfferingString == 'Calculus, Math 300-15  (2 2023)' 

class Test_CourseOffering_String_WithInstructor(unittest.TestCase):      
    def test_CourseOfferingString_WhenAllCondtionsAreMet_CreatesString(self):
        #Arrange
        course = Course('Math','300','Calculus',3) 
        instructor = Instructor('Nicolini','Dylan','Quinnipiac','1/1/2000','DNicolini')   
        courseOffering = CourseOffering(course, "15","2023","2")
        
        #Act
        courseOffering.instructor = instructor
        courseOfferingString = CourseOffering.__str__(courseOffering)
        
        #Assert        
        assert courseOfferingString == 'Calculus, Math 300-15, Dylan Nicolini (2 2023)' 

class Test_CourseOffering_SubmitGrades(unittest.TestCase):      
    def test_SubmitGrades_WhenAllCondtionsAreMet_AddsGradeToTranscript(self):
        #Arrange
        student1 = Student("McLaren", 'Rion','Quinnipiac', '11/26/2003', 'Ramclaren')
        course = Course('Math','300','Calculus',3) 
        courseOffering = CourseOffering(course, "15","2023","2")
        
        #Act
        CourseOffering.submit_grade(courseOffering,student1,"A-")
        
        #Assert
        assert CourseOffering.get_grade(courseOffering,student1) == "A-"
        
if __name__ == '__main__':
    unittest.main() 
