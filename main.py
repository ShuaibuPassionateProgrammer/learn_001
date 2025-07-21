def is_even(num):
    return num % 2 == 0

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    try:
        number = int(input("Enter an integer: "))

        if is_even(number):
            print(f"{number} is Even.")
        else:
            print(f"{number} is Odd.")

        if is_prime(number):
            print(f"{number} is a Prime number.")
        else:
            print(f"{number} is not a Prime number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")