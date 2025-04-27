class Factorial:
    def factorial(self, number: int):
        number = int(input("Enter a non-negative integer: "))       
        if number < 0:
            print("Non-negative integer is not allowed.")
        else:
            factorial = 1
        for i in range(1, number + 1):
            factorial *= i    
        print(f"The factorial of {number} is: {factorial}")
factorial_instance = Factorial()
factorial_instance.factorial(0)  