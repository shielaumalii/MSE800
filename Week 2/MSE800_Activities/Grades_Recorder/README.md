# MSE800 Activities - Week 3
# MSE800 Activities - Week 3 
### **Task 2.0:** Student Grades Recorder
>***Description:***\
>  _This task involves implementing a simple student grading system using classes. Given existing student data, the system should allow recording their grades and display the results clearly and efficiently._
- **_StudentIdentity Class:_** Class for identifying the student. It contains two methods: 1) initializes the student information and 2) presents the student information.
- _**RecordGrades Class:**_ Class for storing the grades of each student. It contains two methods: 1) initializes the grades for three subjects and 2) presents the student grades.
- _**input_grades Function:**_ Function which allows the user to input the grades for each subject of each student. Returns an instance of the 'RecordGrades' class containing the entered grades.
- _**all_students List:**_ Stores instances of 'StudentIdentity' Class for all students.
- _**grades_sheet Dictionary:**_ Stores the grades for each student's name as the key and their 'RecordGrades' instance as the value.
- **Line 32: _for student in all_students Loop:_** Iterates over the 'all_students' list. Uses student name as the unique identifier/key to store data using the 'input_grades' function.
- **Line 36: _for student in all_students Loop:_** Iterates over the 'all_students' list. Uses student name as the unique identifier/key to print the data from 'grades_sheet' dictionary.
- **Line 36: _for student in all_students Loop:_** Iterates over the 'all_students' list. Uses student name as the unique identifier/key to print the data from 'grades_sheet' dictionary. 
