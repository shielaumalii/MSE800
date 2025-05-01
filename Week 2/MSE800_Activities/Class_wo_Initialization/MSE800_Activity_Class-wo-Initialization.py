class Factorial:

    @staticmethod
    def factorial(num1):  # Static method for factorial
        result = 1
        for i in range(1, num1 + 1):
            result *= i
        return result

    @staticmethod
    def check_prime(num1):  # Static method for prime check
        if num1 < 2:  # 0 and 1 are not prime numbers
            return False
        for i in range(2, int(num1 ** 0.5) + 1):  # Check up to the square root of num1
            if num1 % i == 0:
                return False
        return True

    @staticmethod
    def display(num1):  # Static method to display results
        print("Factorial of", num1, "is", Factorial.factorial(num1))
        if Factorial.check_prime(num1):
            print(f"{num1} is a prime number.")
        else:
            print(f"{num1} is not a prime number.")


Factorial.display(10)