def is_prime(number: int) -> int:
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

numbers = [int(i) for i in input().split()]
for number in numbers:
    if is_prime(number):
        print(f"{number} is prime!")