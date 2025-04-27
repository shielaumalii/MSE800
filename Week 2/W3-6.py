number = int(input("Enter a positive integer: "))

class Factorial:
    def factorial(self, number: int):
        if number < 0:
            print("Non-negative integer is not allowed.")
        else:
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            print(f"The factorial of {number} is: {factorial}")


class PrimeNumber:
    def is_prime(self, number: int):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    print(f"{number} is a composite number")
                    break
            else:
                print(f"{number} is a prime number")
        else:
            print(f"{number} is a composite number")


factorial_instance = Factorial()
factorial_instance.factorial(number)

prime_instance = PrimeNumber()
prime_instance.is_prime(number)