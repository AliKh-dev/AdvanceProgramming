def fibo(number: int) -> int:
    if number < 1:
        return "This number you entered is invalid!"
    if number == 1 or number == 2:
        return 1
    return fibo(number - 1) + fibo(number - 2)


print(fibo(int(input())))
