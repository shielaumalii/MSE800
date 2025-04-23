# MSE800 Activities
### **Task 1.0:**  Converting Temperatures of the Week from Celsius to Fahrenheit 
>***Description:***\
>  _The task involves analyzing the temperature data for a week. First, calculate the average temperature for the entire week. Then, identify the highest and lowest temperatures recorded during that period. After that, convert all the temperatures from Celsius to Fahrenheit and print the converted values. Lastly, determine which days (by their index) had temperatures above 20°C and highlight them._
#### **Task 1.0 Code Explanation:**
- **Line #1:** The NumPy library is imported to work in array and perform mathematical operations
- **Line #4:** A NumPy array is created to store the temperature values per day
- **Line #7:** This defines a function named 'celsius_to_fahrenheit' that takes one parameter, 'celsius_array'. 
- **Line #8:** The formula for Celsius to Fahrenheit conversion is applied to each value of the parameter 'celsius_array'.
- **Line #11~#13:** Calculates the average, lowest, and highest temperatures.
- **Line #16~#18:** Prints the calculated average, lowest, and highest temperatures. F-string was used, and integer will be shown with 1 decimal place. 
- **Line #21:** Calls the 'celsius_to_fahrenheit' function and passes the temperatures array as an argument. The function converts all the Celsius values in the array to Fahrenheit and stores the result in 'fahrenheit_temps'.
- **Line #23:** Prints all the temperature in Fahrenheit. The join method is used to combine all the formatted strings into a single string. 
- **Line #27:** Finds the indices of all temperatures in the 'temperatures' array that are greater than 20°C.\
 _[0] - extracts the first element of the result, which is the array of indices. The result is stored in 'above_20_temp'._
- **Line #28:** Loops through each index in the 'above_20_temp' array.
- **Line #29:** Prints the day number in {index + 1} and the corresponding temperature in Celsius.

### **Task 2.0:** Array of Positive Integers
>***Description:***\
>  _This task involves creating and printing a NumPy array containing the first ten positive integers. Additionally, the program should display the array's shape, its data type, and the result of multiplying each element in the array by 2._
#### **Task 2.0 Code Explanation:**
- **Line #1:** The NumPy library was imported to work with arrays.
- **Line #4:** The function np.arrange was used to create a 1D array of integers.
- **Line #5~#7:** Prints the array, it's shape, it's data type, and the result of each data multiplied by 2.
#### **Task 2.0 Result Explanation:**
- **Shape: (10,)** means that the shape of the array is one-dimensional with 10 elements.
-** Data Type: (int64)** means that the data type represents a 64-bit integer.

  ### **Task 3.0:** Test Scores
>***Description:***\
>  _Using a 2D NumPy array representing the test scores of 5 students across 3 subjects, the following tasks shall be performed: calculate and display the average score for each student and each subject, identify the student with the highest total score, and add a 5-point bonus to all students' scores in the third subject._
#### **Task 3.0 Code Explanation:**
- Line #1: The NumPy library is imported to work in array and perform mathematical operations.
- Line #4~#10: The function 'np.array'  was used to create a 2D NumPy array. [Row(axis=1) = Student , Column(axis=0) = Subject]
- Line #13~#17 & #20~#24: The function 'np.mean' was used to calculate the average scores for each student and for each subject. The function 'np.round' was used to round off the average scores. The Python function 'enumerate' is used to organize the average scores per student and per subject.
- Line #27: The function 'np.sum' is used to calculate the total score of each student along rows. The function 'np.argmax' identifies the index of the student with the highest total score.
- Line #28~#29: The student with highest total score is shown by Student No. and row index.
- Line #32: Selects all rows (:) in the third column (2), then adds 5 to each selected value.
- Line #34~35: Prints the updated array after 5 was added to the 3rd column. 
